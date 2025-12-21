#!/usr/bin/env python3
"""Enable SSL and verify deployment for lakepakenham.com"""

import keyring
import requests
import time

def get_netlify_token():
    return keyring.get_password('domain_mgr', 'netlify_token')

site_id = "0e547869-b9d2-44d8-bdba-ce78104258d9"
domain = "lakepakenham.com"
token = get_netlify_token()
headers = {"Authorization": f"Bearer {token}"}

print("=" * 60)
print(f"Checking Netlify deployment and SSL for {domain}")
print("=" * 60)

# Check site info
print("\n1. Checking site status...")
response = requests.get(f"https://api.netlify.com/api/v1/sites/{site_id}", headers=headers)
if response.status_code == 200:
    site = response.json()
    print(f"   Site: {site.get('name')}")
    print(f"   URL: {site.get('url')}")
    print(f"   Custom Domain: {site.get('custom_domain')}")
    print(f"   SSL Status: {site.get('ssl')}")

    published = site.get('published_deploy')
    if published:
        print(f"   Last Deploy: {published.get('published_at')}")
        print(f"   Deploy State: {published.get('state')}")

# Check SSL certificate provisioning
print("\n2. Checking SSL certificate...")
response = requests.get(f"https://api.netlify.com/api/v1/sites/{site_id}/ssl", headers=headers)
if response.status_code == 200:
    ssl = response.json()
    if ssl:
        print(f"   SSL State: {ssl.get('state', 'unknown')}")
        print(f"   SSL URL: {ssl.get('url', 'N/A')}")
    else:
        print("   No SSL certificate configured yet")
else:
    print(f"   SSL endpoint returned: {response.status_code}")
    print(f"   Response: {response.text[:200]}")

# Try to provision SSL
print("\n3. Provisioning SSL certificate...")
response = requests.post(
    f"https://api.netlify.com/api/v1/sites/{site_id}/ssl",
    headers=headers
)

if response.status_code in [200, 201]:
    print("   [SUCCESS] SSL provisioning initiated!")
    print("   Certificate will be issued in 1-2 minutes")
elif response.status_code == 422:
    print("   SSL already provisioned or in progress")
else:
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")

print("\n" + "=" * 60)
print("\nNext steps:")
print("1. DNS propagation: 1-5 minutes")
print("2. SSL certificate: 1-2 minutes after DNS propagates")
print("3. Site should be live at: https://lakepakenham.com")
print("\nCheck status in Netlify dashboard:")
print(f"https://app.netlify.com/sites/spiffy-bunny-156191/settings/domain")
print("=" * 60)
