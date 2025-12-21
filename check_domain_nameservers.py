#!/usr/bin/env python3
"""Check nameservers for domains"""

import keyring
import requests

def get_godaddy_credentials():
    """Get GoDaddy API credentials"""
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    return key, secret

api_key, api_secret = get_godaddy_credentials()
base_url = "https://api.godaddy.com/v1"
headers = {"Authorization": f"sso-key {api_key}:{api_secret}"}

domains = ['irentmy.com', 'trainingrobot.com', 'gptbuilder.au']

for domain in domains:
    print(f"\n{'='*60}")
    print(f"Checking {domain}")
    print(f"{'='*60}")

    # Get domain details
    response = requests.get(f"{base_url}/domains/{domain}", headers=headers)
    if response.status_code == 200:
        info = response.json()
        print(f"Status: {info.get('status')}")
        print(f"Nameservers:")
        for ns in info.get('nameServers', []):
            print(f"  - {ns}")

        # Check if using GoDaddy nameservers
        ns_list = info.get('nameServers', [])
        uses_godaddy = any('domaincontrol.com' in ns.lower() for ns in ns_list)
        print(f"\nUsing GoDaddy DNS: {uses_godaddy}")

        if not uses_godaddy:
            print(f"[INFO] {domain} is using external nameservers - cannot manage DNS via GoDaddy API")
            print(f"       You need to configure DNS at the nameserver provider")
    else:
        print(f"Error: {response.status_code}")
