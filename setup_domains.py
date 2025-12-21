#!/usr/bin/env python3
"""
Setup custom domains for Netlify sites and configure DNS in GoDaddy
"""

import keyring
import requests
import json
import time

# Site configurations
SITES = [
    {
        "domain": "irentmy.com",
        "site_id": "9d457076-1dfa-456f-952a-a8416cd2a252",
        "site_name": "irentmy-com"
    },
    {
        "domain": "trainingrobot.com",
        "site_id": "ae337466-1bd5-4e13-88ab-bf27b83b6d9f",
        "site_name": "trainingrobot-com"
    },
    {
        "domain": "gptbuilder.au",
        "site_id": "50faa887-d33d-42ee-87d8-1078d855b6a9",
        "site_name": "gptbuilder-au"
    }
]

def get_netlify_token():
    """Get Netlify token from keyring"""
    token = keyring.get_password('domain_mgr', 'netlify_token')
    if not token:
        raise Exception("Netlify token not found in keyring")
    return token

def get_godaddy_credentials():
    """Get GoDaddy API credentials"""
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    if not key or not secret:
        raise Exception("GoDaddy credentials not found in keyring")
    return key, secret

def add_netlify_domain(site_id, domain, token):
    """Add custom domain to Netlify site using PATCH updateSite endpoint"""
    url = f"https://api.netlify.com/api/v1/sites/{site_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {"custom_domain": domain}

    print(f"\nAdding {domain} to Netlify site {site_id}...")
    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"[SUCCESS] Successfully added {domain} to Netlify")
        return response.json()
    else:
        print(f"[ERROR] Failed to add {domain}: {response.status_code}")
        print(f"Response: {response.text}")
        # Continue anyway - domain might already be added
        return {"status": "error", "code": response.status_code}

def configure_godaddy_dns(domain, site_name, api_key, api_secret):
    """Configure DNS records in GoDaddy"""
    base_url = "https://api.godaddy.com/v1"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }

    # DNS records to add
    records = [
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

    print(f"\nConfiguring DNS for {domain}...")

    # Update DNS records
    url = f"{base_url}/domains/{domain}/records"

    # First, get existing records to preserve any important ones (like MX)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        existing_records = response.json()
        # Keep MX, TXT, and other important records
        preserved_records = [r for r in existing_records
                           if r['type'] in ['MX', 'TXT', 'NS', 'SOA']]

        # Combine preserved records with new ones
        all_records = preserved_records + records

        # Replace all records
        response = requests.put(url, headers=headers, json=all_records)

        if response.status_code in [200, 204]:
            print(f"[SUCCESS] Successfully configured DNS for {domain}")
            print(f"   - A record: @ -> 75.2.60.5")
            print(f"   - CNAME record: www -> {site_name}.netlify.app")
            return True
        else:
            print(f"[ERROR] Failed to configure DNS for {domain}: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    else:
        print(f"[ERROR] Failed to get existing DNS records: {response.status_code}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("Setting up custom domains for Netlify sites")
    print("=" * 60)

    # Get credentials
    try:
        netlify_token = get_netlify_token()
        godaddy_key, godaddy_secret = get_godaddy_credentials()
    except Exception as e:
        print(f"[ERROR] Error getting credentials: {e}")
        return

    # Process each site
    success_count = 0
    for site in SITES:
        domain = site['domain']
        site_id = site['site_id']
        site_name = site['site_name']

        print(f"\n{'=' * 60}")
        print(f"Processing: {domain}")
        print(f"{'=' * 60}")

        # Step 1: Add domain to Netlify
        netlify_result = add_netlify_domain(site_id, domain, netlify_token)

        if netlify_result:
            # Step 2: Configure GoDaddy DNS
            time.sleep(1)  # Rate limiting
            dns_result = configure_godaddy_dns(domain, site_name, godaddy_key, godaddy_secret)

            if dns_result:
                success_count += 1
                print(f"\n[SUCCESS] {domain} is now fully configured!")
                print(f"   Live URL: https://{domain}")
                print(f"   Netlify URL: https://{site_name}.netlify.app")

        time.sleep(2)  # Rate limiting between sites

    # Summary
    print(f"\n{'=' * 60}")
    print(f"Setup Complete: {success_count}/{len(SITES)} domains configured")
    print(f"{'=' * 60}")
    print("\nNote: DNS propagation can take up to 48 hours, but usually")
    print("completes within a few minutes to a few hours.")
    print("\nCheck status at: https://dnschecker.org")

if __name__ == "__main__":
    main()
