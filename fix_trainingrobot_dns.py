#!/usr/bin/env python3
"""
Fix DNS for trainingrobot.com after nameserver migration
"""

import keyring
import requests
import time

def get_godaddy_credentials():
    """Get GoDaddy API credentials"""
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    return key, secret

api_key, api_secret = get_godaddy_credentials()
base_url = "https://api.godaddy.com/v1"
headers = {
    "Authorization": f"sso-key {api_key}:{api_secret}",
    "Content-Type": "application/json"
}

domain = "trainingrobot.com"
site_name = "trainingrobot-com"

print(f"Configuring DNS for {domain}...")
print("Waiting 15 seconds for domain status to stabilize...")
time.sleep(15)

# Try to configure DNS with multiple retries
max_retries = 5
for attempt in range(max_retries):
    print(f"\nAttempt {attempt + 1}/{max_retries}...")

    # Get existing records
    url = f"{base_url}/domains/{domain}/records"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        existing_records = response.json()

        # Keep important records
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

        # Update DNS
        response = requests.put(url, headers=headers, json=all_records)

        if response.status_code in [200, 204]:
            print(f"\n[SUCCESS] DNS configured for {domain}")
            print(f"  - A record: @ -> 75.2.60.5")
            print(f"  - CNAME record: www -> {site_name}.netlify.app")
            print(f"\n{domain} is now fully configured!")
            print(f"  Live URL: https://{domain}")
            print(f"  Netlify URL: https://{site_name}.netlify.app")
            break
        elif response.status_code == 409:
            print(f"  Domain status still in transition, waiting 10 seconds...")
            time.sleep(10)
        else:
            print(f"  Error: {response.status_code} - {response.text}")
            if attempt < max_retries - 1:
                time.sleep(5)
    else:
        print(f"  Error getting DNS records: {response.status_code}")
        time.sleep(5)
else:
    print(f"\n[ERROR] Failed to configure DNS after {max_retries} attempts")
    print("The nameservers have been changed successfully.")
    print("DNS records can be configured manually via GoDaddy UI once the domain status stabilizes.")
