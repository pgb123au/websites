#!/usr/bin/env python3
"""Check if GoDaddy has forwarding configured for lakepakenham.com"""

import keyring
import requests

def get_godaddy_credentials():
    key = keyring.get_password('domain_mgr', 'godaddy_key')
    secret = keyring.get_password('domain_mgr', 'godaddy_secret')
    return key, secret

domain = "lakepakenham.com"
api_key, api_secret = get_godaddy_credentials()
base_url = "https://api.godaddy.com/v1"
headers = {"Authorization": f"sso-key {api_key}:{api_secret}"}

print("=" * 60)
print(f"Checking GoDaddy forwarding for {domain}")
print("=" * 60)

# Check domain details
response = requests.get(f"{base_url}/domains/{domain}", headers=headers)
if response.status_code == 200:
    info = response.json()
    print(f"\nDomain Status: {info.get('status')}")
    print(f"Locked: {info.get('locked')}")
    print(f"Privacy: {info.get('privacy')}")
    print(f"Renewauto: {info.get('renewAuto')}")

# Check for forwarding configuration
print("\nChecking for HTTP forwarding...")
response = requests.get(f"{base_url}/domains/{domain}/forwards", headers=headers)

if response.status_code == 200:
    forwards = response.json()
    if forwards:
        print(f"[WARNING] Found {len(forwards)} forwarding rules:")
        for fwd in forwards:
            print(f"  From: {fwd.get('from', 'N/A')}")
            print(f"  To: {fwd.get('to', 'N/A')}")
            print(f"  Type: {fwd.get('type', 'N/A')}")
            print()
    else:
        print("[INFO] No forwarding rules configured")
elif response.status_code == 404:
    print("[INFO] No forwarding endpoint available or no forwards configured")
else:
    print(f"[ERROR] Status: {response.status_code}")
    print(f"Response: {response.text[:200]}")

# Check parking status
print("\nChecking if domain is parked...")
if '15.197.225.128' in str(response.text) or 'afternic' in str(response.text).lower():
    print("[WARNING] Domain appears to be parked at Afternic/GoDaddy")

print("\n" + "=" * 60)
print("If domain is parked, you need to:")
print("1. Log into GoDaddy at https://dcc.godaddy.com/")
print("2. Go to domain settings for lakepakenham.com")
print("3. Disable domain parking/forwarding")
print("4. Make sure DNS records are being used (not forwarding)")
print("=" * 60)
