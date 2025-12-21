#!/usr/bin/env python3
"""Check lakepakenham.com configuration"""

import keyring
import requests

def get_godaddy_credentials():
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    return key, secret

def get_netlify_token():
    return keyring.get_password('domain_mgr', 'netlify_token')

domain = "lakepakenham.com"
site_id = "0e547869-b9d2-44d8-bdba-ce78104258d9"

print("=" * 60)
print(f"Checking {domain} configuration")
print("=" * 60)

# Check GoDaddy DNS
api_key, api_secret = get_godaddy_credentials()
headers = {"Authorization": f"sso-key {api_key}:{api_secret}"}

print("\n1. Checking nameservers...")
response = requests.get(f"https://api.godaddy.com/v1/domains/{domain}", headers=headers)
if response.status_code == 200:
    info = response.json()
    ns_list = info.get('nameServers', [])
    print(f"   Nameservers:")
    for ns in ns_list:
        print(f"     - {ns}")
    uses_godaddy = any('domaincontrol.com' in ns.lower() for ns in ns_list)
    print(f"   Using GoDaddy DNS: {uses_godaddy}")
else:
    print(f"   Error: {response.status_code}")

print("\n2. Checking DNS records...")
response = requests.get(f"https://api.godaddy.com/v1/domains/{domain}/records", headers=headers)
if response.status_code == 200:
    records = response.json()
    print(f"   Total DNS records: {len(records)}")
    for record in records:
        if record['type'] in ['A', 'CNAME']:
            print(f"     {record['type']} {record['name']} -> {record['data']}")
else:
    print(f"   Error getting DNS records: {response.status_code}")
    if response.status_code == 404:
        print(f"   DNS zone not found - domain may be using external nameservers")

# Check Netlify
print("\n3. Checking Netlify configuration...")
token = get_netlify_token()
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(f"https://api.netlify.com/api/v1/sites/{site_id}", headers=headers)
if response.status_code == 200:
    site = response.json()
    print(f"   Site Name: {site.get('name')}")
    print(f"   URL: {site.get('url')}")
    print(f"   Custom Domain: {site.get('custom_domain')}")
    print(f"   SSL: {site.get('ssl')}")
    print(f"   Published At: {site.get('published_deploy', {}).get('published_at')}")

    # Check domain aliases
    domain_aliases = site.get('domain_aliases', [])
    if domain_aliases:
        print(f"   Domain Aliases:")
        for alias in domain_aliases:
            print(f"     - {alias}")
else:
    print(f"   Error: {response.status_code}")

print("\n" + "=" * 60)
