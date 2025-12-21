#!/usr/bin/env python3
"""Check all domain aliases for lakepakenham site"""

import keyring
import requests
import json

def get_netlify_token():
    return keyring.get_password('domain_mgr', 'netlify_token')

site_id = "0e547869-b9d2-44d8-bdba-ce78104258d9"
token = get_netlify_token()
headers = {"Authorization": f"Bearer {token}"}

print("=" * 60)
print("Checking Netlify domain configuration")
print("=" * 60)

# Get site info
response = requests.get(f"https://api.netlify.com/api/v1/sites/{site_id}", headers=headers)
if response.status_code == 200:
    site = response.json()
    print(f"\nSite ID: {site.get('id')}")
    print(f"Site Name: {site.get('name')}")
    print(f"Default URL: {site.get('url')}")
    print(f"Custom Domain: {site.get('custom_domain')}")
    print(f"SSL: {site.get('ssl')}")

    # Domain aliases
    domain_aliases = site.get('domain_aliases', [])
    print(f"\nDomain Aliases ({len(domain_aliases)}):")
    if domain_aliases:
        for alias in domain_aliases:
            print(f"  - {alias}")
    else:
        print("  (none)")

    # Check if we need to add www
    custom_domain = site.get('custom_domain')
    if custom_domain and f"www.{custom_domain}" not in domain_aliases:
        print(f"\n[WARNING] www.{custom_domain} is not in domain aliases!")
        print("This may cause issues with www subdomain")

# Try to add www subdomain if missing
print("\n" + "=" * 60)
print("Attempting to add www.lakepakenham.com as domain alias...")
print("=" * 60)

data = {"hostname": "www.lakepakenham.com"}
response = requests.post(
    f"https://api.netlify.com/api/v1/sites/{site_id}/aliases",
    headers={**headers, "Content-Type": "application/json"},
    json=data
)

if response.status_code in [200, 201]:
    print("[SUCCESS] Added www.lakepakenham.com")
elif response.status_code == 422:
    print("[INFO] www.lakepakenham.com already exists or validation failed")
    print(f"Response: {response.text}")
else:
    print(f"[ERROR] Status: {response.status_code}")
    print(f"Response: {response.text}")

print("\n" + "=" * 60)
