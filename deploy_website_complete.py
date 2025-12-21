#!/usr/bin/env python3
"""
Complete Website Deployment Script
Deploys a website from /websites/{domain}/ to Netlify with full DNS and SSL setup

Usage:
    python deploy_website_complete.py <domain>

Example:
    python deploy_website_complete.py irentmy.com
"""

import sys
import os
import keyring
import requests
import time
import subprocess
import json

# Critical Netlify IP for DNS
NETLIFY_IP = "75.2.60.5"

class Colors:
    """ANSI color codes that work in Windows Terminal"""
    GREEN = ''
    RED = ''
    YELLOW = ''
    BLUE = ''
    RESET = ''

def print_header(text):
    """Print section header"""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)

def print_success(text):
    """Print success message"""
    print(f"[SUCCESS] {text}")

def print_error(text):
    """Print error message"""
    print(f"[ERROR] {text}")

def print_warning(text):
    """Print warning message"""
    print(f"[WARNING] {text}")

def print_info(text):
    """Print info message"""
    print(f"[INFO] {text}")

def get_credentials():
    """Get API credentials from keyring"""
    try:
        netlify_token = keyring.get_password('domain_mgr', 'netlify_token')
        godaddy_key = keyring.get_password('domain_mgr', 'godaddy_key')
        godaddy_secret = keyring.get_password('domain_mgr', 'godaddy_secret')

        if not netlify_token or not godaddy_key or not godaddy_secret:
            raise Exception("Missing credentials in keyring")

        return netlify_token, godaddy_key, godaddy_secret
    except Exception as e:
        print_error(f"Failed to get credentials: {e}")
        return None, None, None

def check_prerequisites(domain, domain_dir):
    """Check if domain directory and files exist"""
    print_header("Step 1: Checking Prerequisites")

    # Check directory exists
    if not os.path.exists(domain_dir):
        print_error(f"Directory not found: {domain_dir}")
        return False
    print_success(f"Domain directory exists: {domain_dir}")

    # Check index.html exists
    index_file = os.path.join(domain_dir, 'index.html')
    if not os.path.exists(index_file):
        print_error(f"index.html not found in {domain_dir}")
        return False
    print_success("index.html found")

    # Check netlify.toml exists
    toml_file = os.path.join(domain_dir, 'netlify.toml')
    if not os.path.exists(toml_file):
        print_warning("netlify.toml not found, creating default...")
        with open(toml_file, 'w') as f:
            f.write('[[redirects]]\n  from = "/*"\n  to = "/index.html"\n  status = 200\n')
        print_success("Created netlify.toml")
    else:
        print_success("netlify.toml found")

    return True

def check_nameservers(domain, godaddy_key, godaddy_secret):
    """Check if domain uses GoDaddy nameservers"""
    print_header("Step 2: Checking Nameservers")

    headers = {"Authorization": f"sso-key {godaddy_key}:{godaddy_secret}"}
    response = requests.get(f"https://api.godaddy.com/v1/domains/{domain}", headers=headers)

    if response.status_code != 200:
        print_error(f"Failed to get domain info: {response.status_code}")
        return None

    info = response.json()
    nameservers = info.get('nameServers', [])
    print_info(f"Current nameservers for {domain}:")
    for ns in nameservers:
        print(f"  - {ns}")

    uses_godaddy = any('domaincontrol.com' in ns.lower() for ns in nameservers)

    if uses_godaddy:
        print_success("Using GoDaddy nameservers - DNS can be configured via API")
        return True
    else:
        print_warning("Using external nameservers - DNS configuration may fail")
        print_info("Consider migrating nameservers to GoDaddy first")

        response = input("\nContinue anyway? (y/N): ")
        return response.lower() == 'y'

def deploy_to_netlify(domain, domain_dir):
    """Deploy site to Netlify"""
    print_header("Step 3: Deploying to Netlify")

    # Check if site already exists
    state_file = os.path.join(domain_dir, '.netlify', 'state.json')
    site_id = None

    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            state = json.load(f)
            site_id = state.get('siteId')
        print_info(f"Found existing site: {site_id}")

    if not site_id:
        # Create new site
        site_name = domain.replace('.', '-')
        print_info(f"Creating new Netlify site: {site_name}")

        cmd = f'cd "{domain_dir}" && echo "YesRight" | netlify sites:create --name {site_name}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            print_error(f"Failed to create site: {result.stderr}")
            return None

        # Get site ID from .netlify/state.json
        if os.path.exists(state_file):
            with open(state_file, 'r') as f:
                state = json.load(f)
                site_id = state.get('siteId')

        if not site_id:
            print_error("Could not get site ID after creation")
            return None

        print_success(f"Created site: {site_id}")

    # Deploy to production
    print_info("Deploying to production...")
    cmd = f'cd "{domain_dir}" && netlify deploy --prod --dir=.'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print_error(f"Deployment failed: {result.stderr}")
        return None

    print_success("Deployed to Netlify")
    return site_id

def add_custom_domain(site_id, domain, netlify_token):
    """Add custom domain to Netlify site"""
    print_header("Step 4: Adding Custom Domain to Netlify")

    headers = {
        "Authorization": f"Bearer {netlify_token}",
        "Content-Type": "application/json"
    }

    data = {"custom_domain": domain}
    response = requests.patch(
        f"https://api.netlify.com/api/v1/sites/{site_id}",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        print_success(f"Added custom domain: {domain}")
        return True
    else:
        print_error(f"Failed to add custom domain: {response.status_code}")
        print_error(f"Response: {response.text}")
        return False

def configure_dns(domain, site_name, godaddy_key, godaddy_secret):
    """Configure DNS records in GoDaddy"""
    print_header("Step 5: Configuring DNS Records")

    headers = {
        "Authorization": f"sso-key {godaddy_key}:{godaddy_secret}",
        "Content-Type": "application/json"
    }

    # Get existing records
    print_info("Fetching existing DNS records...")
    response = requests.get(
        f"https://api.godaddy.com/v1/domains/{domain}/records",
        headers=headers
    )

    if response.status_code != 200:
        print_error(f"Failed to get DNS records: {response.status_code}")
        print_error(f"Response: {response.text}")
        return False

    existing_records = response.json()

    # Preserve important records
    preserved_records = [
        r for r in existing_records
        if r['type'] in ['NS', 'SOA', 'MX', 'TXT'] or
        (r['type'] == 'CNAME' and r['name'] == '_domainconnect')
    ]

    print_info(f"Preserving {len(preserved_records)} existing records (NS, SOA, MX, TXT)")

    # Add Netlify records
    new_records = [
        {
            "type": "A",
            "name": "@",
            "data": NETLIFY_IP,
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
    print_info(f"Updating DNS records...")
    print_info(f"  - A record: @ -> {NETLIFY_IP}")
    print_info(f"  - CNAME record: www -> {site_name}.netlify.app")

    response = requests.put(
        f"https://api.godaddy.com/v1/domains/{domain}/records",
        headers=headers,
        json=all_records
    )

    if response.status_code in [200, 204]:
        print_success("DNS records configured")
        return True
    else:
        print_error(f"Failed to update DNS: {response.status_code}")
        print_error(f"Response: {response.text}")
        return False

def provision_ssl(site_id, netlify_token):
    """Provision SSL certificate"""
    print_header("Step 6: Provisioning SSL Certificate")

    headers = {"Authorization": f"Bearer {netlify_token}"}

    response = requests.post(
        f"https://api.netlify.com/api/v1/sites/{site_id}/ssl",
        headers=headers
    )

    if response.status_code in [200, 201]:
        print_success("SSL certificate provisioning initiated")
        print_info("Certificate will be issued in 1-2 minutes")
        return True
    elif response.status_code == 422:
        print_warning("SSL already provisioned or in progress")
        return True
    else:
        print_error(f"Failed to provision SSL: {response.status_code}")
        print_error(f"Response: {response.text}")
        return False

def verify_deployment(domain):
    """Verify the deployment is working"""
    print_header("Step 7: Verifying Deployment")

    print_info("Waiting 30 seconds for DNS propagation...")
    time.sleep(30)

    # Test DNS
    print_info("Testing DNS resolution...")
    try:
        result = subprocess.run(
            ['nslookup', domain, '8.8.8.8'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if NETLIFY_IP in result.stdout:
            print_success(f"DNS resolves to {NETLIFY_IP}")
        else:
            print_warning(f"DNS may not be propagated yet")
            print_info(f"Expected: {NETLIFY_IP}")
            print_info(f"Got: {result.stdout}")
    except Exception as e:
        print_warning(f"Could not test DNS: {e}")

    # Test HTTP
    print_info("Testing HTTP access...")
    try:
        response = requests.get(f"http://{domain}", timeout=10, allow_redirects=False)
        if response.status_code == 301 and 'https' in response.headers.get('Location', ''):
            print_success("HTTP redirects to HTTPS")
        else:
            print_warning(f"HTTP returned {response.status_code}")
    except Exception as e:
        print_warning(f"Could not test HTTP: {e}")

    # Test HTTPS
    print_info("Testing HTTPS access...")
    try:
        response = requests.get(f"https://{domain}", timeout=10, verify=False)
        if response.status_code == 200:
            print_success("HTTPS is working")

            if 'netlify' in response.headers.get('Server', '').lower():
                print_success("Confirmed: Site is served by Netlify")
        else:
            print_warning(f"HTTPS returned {response.status_code}")
    except Exception as e:
        print_warning(f"HTTPS may not be ready yet: {e}")
        print_info("SSL certificate may still be provisioning (takes 1-2 minutes)")

    return True

def main():
    """Main deployment orchestrator"""
    if len(sys.argv) != 2:
        print("Usage: python deploy_website_complete.py <domain>")
        print("Example: python deploy_website_complete.py irentmy.com")
        sys.exit(1)

    domain = sys.argv[1]
    site_name = domain.replace('.', '-')

    # Get base directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    domain_dir = os.path.join(script_dir, domain)

    print_header(f"Complete Deployment: {domain}")
    print_info(f"Domain: {domain}")
    print_info(f"Site Name: {site_name}")
    print_info(f"Directory: {domain_dir}")

    # Get credentials
    netlify_token, godaddy_key, godaddy_secret = get_credentials()
    if not netlify_token:
        print_error("Cannot proceed without credentials")
        sys.exit(1)

    # Step 1: Check prerequisites
    if not check_prerequisites(domain, domain_dir):
        sys.exit(1)

    # Step 2: Check nameservers
    if not check_nameservers(domain, godaddy_key, godaddy_secret):
        print_warning("Deployment cancelled or will skip DNS configuration")
        sys.exit(1)

    # Step 3: Deploy to Netlify
    site_id = deploy_to_netlify(domain, domain_dir)
    if not site_id:
        sys.exit(1)

    # Step 4: Add custom domain
    if not add_custom_domain(site_id, domain, netlify_token):
        print_warning("Continuing despite custom domain error...")

    # Step 5: Configure DNS
    if not configure_dns(domain, site_name, godaddy_key, godaddy_secret):
        print_warning("DNS configuration failed - may need manual setup")

    # Step 6: Provision SSL
    if not provision_ssl(site_id, netlify_token):
        print_warning("SSL provisioning failed - may need manual setup")

    # Step 7: Verify
    verify_deployment(domain)

    # Summary
    print_header("Deployment Summary")
    print_success(f"Deployment completed for {domain}")
    print()
    print(f"  Live URL: https://{domain}")
    print(f"  Netlify URL: https://{site_name}.netlify.app")
    print(f"  Site ID: {site_id}")
    print(f"  Admin: https://app.netlify.com/sites/{site_name}")
    print()
    print_info("Next steps:")
    print("  1. Wait 2-5 minutes for full DNS propagation")
    print("  2. Test the site: https://{domain}")
    print("  3. Clear your browser cache if needed")
    print("  4. Update DEPLOYMENT.md status")
    print()
    print_header("Deployment Complete!")

if __name__ == "__main__":
    main()
