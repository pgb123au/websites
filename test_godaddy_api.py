#!/usr/bin/env python3
"""Test GoDaddy API access"""

import keyring
import requests
import json

def get_godaddy_credentials():
    """Get GoDaddy API credentials"""
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    if not key or not secret:
        raise Exception("GoDaddy credentials not found in keyring")
    return key, secret

api_key, api_secret = get_godaddy_credentials()

base_url = "https://api.godaddy.com/v1"
headers = {
    "Authorization": f"sso-key {api_key}:{api_secret}",
}

# List all domains to check the exact names
print("Listing all GoDaddy domains...")
response = requests.get(f"{base_url}/domains", headers=headers)

if response.status_code == 200:
    domains = response.json()
    print(f"\nFound {len(domains)} domains:")

    target_domains = ['irentmy.com', 'trainingrobot.com', 'gptbuilder.au']
    for domain in domains:
        domain_name = domain.get('domain')
        if any(target in domain_name for target in target_domains):
            print(f"\n  {domain_name}")
            print(f"    Status: {domain.get('status')}")
            print(f"    Expires: {domain.get('expires')}")

            # Try to get DNS records
            dns_url = f"{base_url}/domains/{domain_name}/records"
            dns_response = requests.get(dns_url, headers=headers)
            print(f"    DNS records status: {dns_response.status_code}")
            if dns_response.status_code == 200:
                records = dns_response.json()
                print(f"    DNS records count: {len(records)}")
                # Show A and CNAME records
                for record in records:
                    if record['type'] in ['A', 'CNAME']:
                        print(f"      {record['type']} {record['name']} -> {record['data']}")
else:
    print(f"Error listing domains: {response.status_code}")
    print(response.text)
