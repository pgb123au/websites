#!/usr/bin/env python3
"""Fix lakepakenham.com DNS to point to Netlify"""

import keyring
import requests

def get_godaddy_credentials():
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    return key, secret

domain = "lakepakenham.com"
api_key, api_secret = get_godaddy_credentials()
base_url = "https://api.godaddy.com/v1"
headers = {
    "Authorization": f"sso-key {api_key}:{api_secret}",
    "Content-Type": "application/json"
}

print("=" * 60)
print(f"Fixing DNS for {domain}")
print("=" * 60)

# Get current records
url = f"{base_url}/domains/{domain}/records"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    existing_records = response.json()
    print(f"\nCurrent A records:")
    for r in existing_records:
        if r['type'] == 'A' and r['name'] == '@':
            print(f"  {r['type']} {r['name']} -> {r['data']}")

    # Keep important records (NS, SOA, MX, TXT, _domainconnect)
    preserved_records = []
    for r in existing_records:
        if r['type'] in ['NS', 'SOA', 'MX', 'TXT']:
            preserved_records.append(r)
        elif r['type'] == 'CNAME' and r['name'] == '_domainconnect':
            preserved_records.append(r)

    # Add correct Netlify records
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
            "data": "lakepakenham.com",  # Netlify prefers apex domain CNAME
            "ttl": 3600
        }
    ]

    all_records = preserved_records + new_records

    print("\nUpdating DNS records...")
    print("  New A record: @ -> 75.2.60.5")
    print("  New CNAME: www -> lakepakenham.com")

    response = requests.put(url, headers=headers, json=all_records)

    if response.status_code in [200, 204]:
        print("\n[SUCCESS] DNS records updated!")
        print("\nPlease wait a few minutes for DNS propagation.")
        print("Then check: https://lakepakenham.com")
    else:
        print(f"\n[ERROR] Failed to update DNS: {response.status_code}")
        print(f"Response: {response.text}")
else:
    print(f"[ERROR] Failed to get DNS records: {response.status_code}")

print("\n" + "=" * 60)
