#!/usr/bin/env python3
"""Test Netlify API access"""

import keyring
import requests
import json

def get_netlify_token():
    """Get Netlify token from keyring"""
    token = keyring.get_password('domain_mgr', 'netlify_token')
    if not token:
        raise Exception("Netlify token not found in keyring")
    return token

# Get site info to verify credentials
token = get_netlify_token()
site_id = "9d457076-1dfa-456f-952a-a8416cd2a252"

headers = {
    "Authorization": f"Bearer {token}",
}

# Try to get site info
url = f"https://api.netlify.com/api/v1/sites/{site_id}"
print(f"Testing API access to site {site_id}...")
response = requests.get(url, headers=headers)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    site_info = response.json()
    print(f"Site Name: {site_info.get('name')}")
    print(f"URL: {site_info.get('url')}")
    print(f"Custom Domain: {site_info.get('custom_domain')}")
    print(f"\nExisting domains:")
    for domain in site_info.get('domain_aliases', []):
        print(f"  - {domain}")
else:
    print(f"Error: {response.text}")

# Check what domains endpoint is correct
print("\n\nChecking domains endpoint...")
domains_url = f"https://api.netlify.com/api/v1/sites/{site_id}/domains"
response = requests.get(domains_url, headers=headers)
print(f"GET {domains_url}")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    print(f"Response: {json.dumps(response.json(), indent=2)[:500]}")
else:
    print(f"Error: {response.text}")
