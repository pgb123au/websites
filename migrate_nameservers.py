#!/usr/bin/env python3
"""
Migrate domains from Wix nameservers to GoDaddy nameservers and configure DNS
"""

import keyring
import requests
import time

# Domains to migrate
DOMAINS_TO_MIGRATE = [
    {
        "domain": "irentmy.com",
        "site_name": "irentmy-com"
    },
    {
        "domain": "trainingrobot.com",
        "site_name": "trainingrobot-com"
    }
]

# GoDaddy default nameservers
GODADDY_NAMESERVERS = [
    "ns11.domaincontrol.com",
    "ns12.domaincontrol.com"
]

def get_godaddy_credentials():
    """Get GoDaddy API credentials"""
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    return key, secret

def change_nameservers(domain, api_key, api_secret):
    """Change domain nameservers to GoDaddy"""
    base_url = "https://api.godaddy.com/v1"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }

    print(f"\nChanging nameservers for {domain} to GoDaddy...")

    url = f"{base_url}/domains/{domain}"
    data = {"nameServers": GODADDY_NAMESERVERS}

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code in [200, 204]:
        print(f"[SUCCESS] Nameservers changed for {domain}")
        print(f"  - ns11.domaincontrol.com")
        print(f"  - ns12.domaincontrol.com")
        return True
    else:
        print(f"[ERROR] Failed to change nameservers: {response.status_code}")
        print(f"Response: {response.text}")
        return False

def configure_dns(domain, site_name, api_key, api_secret):
    """Configure DNS records after nameserver migration"""
    base_url = "https://api.godaddy.com/v1"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }

    print(f"\nConfiguring DNS records for {domain}...")

    # Wait for DNS zone to be created (may take a few seconds after nameserver change)
    max_retries = 10
    for attempt in range(max_retries):
        # Try to get existing records
        url = f"{base_url}/domains/{domain}/records"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(f"  DNS zone is ready")
            existing_records = response.json()

            # Keep important records (NS, SOA, MX, TXT)
            preserved_records = [r for r in existing_records
                               if r['type'] in ['NS', 'SOA', 'MX', 'TXT']]

            # Add Netlify records
            new_records = [
                {
                    "type": "A",
                    "name": "@",
                    "data": "75.2.60.5",
                    "ttl": 3600
                },
                {
                    "type": "CNAME",
                    "name": "www",
                    "data": f"{site_name}.netlify.app",
                    "ttl": 3600
                }
            ]

            all_records = preserved_records + new_records

            # Update DNS records
            response = requests.put(url, headers=headers, json=all_records)

            if response.status_code in [200, 204]:
                print(f"[SUCCESS] DNS configured for {domain}")
                print(f"  - A record: @ -> 75.2.60.5")
                print(f"  - CNAME record: www -> {site_name}.netlify.app")
                return True
            else:
                print(f"[ERROR] Failed to configure DNS: {response.status_code}")
                print(f"Response: {response.text}")
                return False

        elif response.status_code == 404:
            print(f"  Waiting for DNS zone creation... (attempt {attempt + 1}/{max_retries})")
            time.sleep(3)
        else:
            print(f"[ERROR] Unexpected error: {response.status_code}")
            return False

    print(f"[ERROR] DNS zone not created after {max_retries} attempts")
    return False

def main():
    """Main migration function"""
    print("=" * 60)
    print("Migrating domains from Wix to GoDaddy nameservers")
    print("=" * 60)

    api_key, api_secret = get_godaddy_credentials()

    for domain_info in DOMAINS_TO_MIGRATE:
        domain = domain_info['domain']
        site_name = domain_info['site_name']

        print(f"\n{'=' * 60}")
        print(f"Processing: {domain}")
        print(f"{'=' * 60}")

        # Step 1: Change nameservers
        ns_success = change_nameservers(domain, api_key, api_secret)

        if ns_success:
            # Wait a moment for nameserver change to propagate
            print("\nWaiting 5 seconds for nameserver change to register...")
            time.sleep(5)

            # Step 2: Configure DNS
            dns_success = configure_dns(domain, site_name, api_key, api_secret)

            if dns_success:
                print(f"\n[SUCCESS] {domain} is now fully configured!")
                print(f"  Live URL: https://{domain}")
                print(f"  Netlify URL: https://{site_name}.netlify.app")
        else:
            print(f"\n[ERROR] Skipping DNS configuration for {domain} due to nameserver change failure")

        time.sleep(2)

    print(f"\n{'=' * 60}")
    print("Migration Complete")
    print(f"{'=' * 60}")
    print("\nIMPORTANT NOTES:")
    print("1. Nameserver changes can take 24-48 hours to fully propagate")
    print("2. Your sites will be accessible at their .netlify.app URLs immediately")
    print("3. Custom domains will work once DNS propagates")
    print("4. Check propagation status at: https://dnschecker.org")
    print("\n5. Previous Wix sites (if any) will stop working after nameserver change")

if __name__ == "__main__":
    main()
