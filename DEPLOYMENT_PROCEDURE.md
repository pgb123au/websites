# Website Deployment Procedure - Step-by-Step Guide

**Last Updated**: 2025-12-21
**Purpose**: Ensure ALL websites deploy successfully the FIRST time

---

## Issues Encountered & Lessons Learned

### lakepakenham.com Deployment Problems

1. **Old DNS Records**: DNS A record pointed to old IPs (15.197.225.128, 3.33.251.168) instead of Netlify (75.2.60.5)
2. **No SSL**: SSL certificate was not provisioned after deployment
3. **DNS Cache**: Local DNS caching caused site to appear broken even after fixes
4. **Missing Steps**: Deployed to Netlify but didn't configure DNS or SSL

### Root Cause
The deployment was done in pieces without verifying each step. DNS was configured previously (perhaps for a different host), and the deployment didn't update it.

---

## COMPLETE Deployment Checklist

Use this checklist for EVERY new website deployment:

- [ ] 1. Build website locally
- [ ] 2. Test website locally (open index.html in browser)
- [ ] 3. Check domain nameservers (must use GoDaddy or migrate first)
- [ ] 4. Deploy to Netlify production
- [ ] 5. Add custom domain to Netlify via API
- [ ] 6. Configure DNS records in GoDaddy (A + CNAME)
- [ ] 7. Provision SSL certificate via Netlify API
- [ ] 8. Wait 2-5 minutes for DNS propagation
- [ ] 9. Verify HTTP works (should redirect to HTTPS)
- [ ] 10. Verify HTTPS works with SSL
- [ ] 11. Test site content loads correctly
- [ ] 12. Update DEPLOYMENT.md status
- [ ] 13. Commit to GitHub

---

## Automated Deployment Script

Use `deploy_website_complete.py` for automated deployment:

```bash
cd /c/Users/peter/Downloads/CC/websites
python deploy_website_complete.py <domain>
```

Example:
```bash
python deploy_website_complete.py irentmy.com
```

This script does everything automatically:
1. Checks prerequisites (files exist, nameservers)
2. Deploys to Netlify
3. Adds custom domain
4. Configures DNS
5. Provisions SSL
6. Verifies deployment
7. Updates documentation

---

## Manual Deployment Steps (If Script Fails)

### Step 1: Verify Prerequisites

```bash
# Check domain exists
cd /c/Users/peter/Downloads/CC/Domains
python -c "from domain_lookup import DomainLookup; lookup = DomainLookup(); print(lookup.get_domain('yourdomain.com'))"

# Check nameservers
cd /c/Users/peter/Downloads/CC/websites
python check_domain_nameservers.py
```

**If using Wix/external nameservers**, migrate first:
```bash
python migrate_nameservers.py
# Add domain to DOMAINS_TO_MIGRATE list first
```

### Step 2: Deploy to Netlify

```bash
cd /c/Users/peter/Downloads/CC/websites/yourdomain.com

# For NEW sites:
echo "YesRight" | netlify sites:create --name yourdomain-com
netlify deploy --prod --dir=.

# For EXISTING sites (check .netlify/state.json for site ID):
netlify deploy --prod --dir=.
```

**Record the Site ID** from output!

### Step 3: Add Custom Domain to Netlify

```python
# Use Python to add domain via API
import keyring, requests

site_id = "YOUR_SITE_ID"
domain = "yourdomain.com"
token = keyring.get_password('domain_mgr', 'netlify_token')

response = requests.patch(
    f"https://api.netlify.com/api/v1/sites/{site_id}",
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    json={"custom_domain": domain}
)
print(f"Status: {response.status_code}")
```

### Step 4: Configure DNS Records

**CRITICAL: Check if GoDaddy DNS is being used**

```bash
cd /c/Users/peter/Downloads/CC/websites
python check_domain_nameservers.py
```

If using **GoDaddy nameservers** (contains `domaincontrol.com`):

```python
import keyring, requests

domain = "yourdomain.com"
site_name = "yourdomain-com"  # Netlify site name

api_key = keyring.get_password('domain_mgr', 'godaddy_key')
api_secret = keyring.get_password('domain_mgr', 'godaddy_secret')
headers = {
    "Authorization": f"sso-key {api_key}:{api_secret}",
    "Content-Type": "application/json"
}

# Get existing records (preserve NS, SOA, MX, TXT)
response = requests.get(f"https://api.godaddy.com/v1/domains/{domain}/records", headers=headers)
existing = response.json()
preserved = [r for r in existing if r['type'] in ['NS', 'SOA', 'MX', 'TXT']]

# Add Netlify records
new_records = [
    {"type": "A", "name": "@", "data": "75.2.60.5", "ttl": 3600},
    {"type": "CNAME", "name": "www", "data": f"{site_name}.netlify.app", "ttl": 3600}
]

all_records = preserved + new_records

# Update DNS
response = requests.put(
    f"https://api.godaddy.com/v1/domains/{domain}/records",
    headers=headers,
    json=all_records
)
print(f"DNS Status: {response.status_code}")
```

If using **external nameservers**, you CANNOT configure DNS via API. Either:
- Migrate nameservers to GoDaddy first, OR
- Configure DNS manually at the nameserver provider

### Step 5: Provision SSL Certificate

```python
import keyring, requests

site_id = "YOUR_SITE_ID"
token = keyring.get_password('domain_mgr', 'netlify_token')

response = requests.post(
    f"https://api.netlify.com/api/v1/sites/{site_id}/ssl",
    headers={"Authorization": f"Bearer {token}"}
)
print(f"SSL Status: {response.status_code}")
```

### Step 6: Verify Deployment

Wait 2-5 minutes, then:

```bash
# Test DNS resolution
nslookup yourdomain.com 8.8.8.8
# Should return: 75.2.60.5

# Test HTTP (should redirect to HTTPS)
curl -I http://yourdomain.com

# Test HTTPS
curl -I https://yourdomain.com

# Test content
curl -sL https://yourdomain.com | head -20
```

**Expected Results**:
- DNS returns `75.2.60.5`
- HTTP returns `301 Moved Permanently` → HTTPS
- HTTPS returns `200 OK` with `Server: Netlify`
- Content shows your website HTML

---

## Common Issues & Solutions

### Issue 1: Domain resolves to wrong IP

**Symptom**: `nslookup` shows IPs other than `75.2.60.5`

**Cause**: Old DNS records still configured

**Solution**:
```bash
cd /c/Users/peter/Downloads/CC/websites
python fix_dns_records.py yourdomain.com
```

### Issue 2: Site shows "Not Found" or 404

**Symptom**: Netlify returns 404

**Cause**: Custom domain not added to Netlify

**Solution**:
```python
# Re-add custom domain via API (see Step 3)
```

### Issue 3: SSL certificate not working

**Symptom**: HTTPS doesn't work or shows certificate error

**Cause**: SSL not provisioned

**Solution**:
```bash
# Wait 2-5 minutes for DNS to propagate first
# Then provision SSL (see Step 5)
```

### Issue 4: Site shows parking page

**Symptom**: Domain redirects to Afternic or shows "for sale"

**Cause**: Domain has parking/forwarding enabled

**Solution**:
1. Log into GoDaddy: https://dcc.godaddy.com/
2. Go to domain settings
3. Disable parking/forwarding
4. Ensure "Use my nameservers" is selected

### Issue 5: DNS API returns 404

**Symptom**: GoDaddy DNS API returns 404

**Cause**: Domain is using external nameservers (not GoDaddy)

**Solution**:
```bash
# Check nameservers
python check_domain_nameservers.py

# If using external NS, migrate first:
python migrate_nameservers.py
```

### Issue 6: "Domain already exists" error

**Symptom**: Netlify API returns 422 "domain already exists"

**Cause**: Domain is already added to another Netlify site

**Solution**:
1. Check which site owns the domain in Netlify dashboard
2. Remove from old site first
3. Add to new site

---

## Critical DNS Values

**Always use these exact values for Netlify:**

| Record Type | Name | Value | TTL |
|-------------|------|-------|-----|
| A | @ | `75.2.60.5` | 3600 |
| CNAME | www | `{site-name}.netlify.app` | 3600 |

**DO NOT USE**:
- Old AWS IPs (15.x.x.x, 3.x.x.x)
- Cloudflare IPs
- Other hosting provider IPs

**ALWAYS PRESERVE**:
- NS records (nameservers)
- SOA records (DNS zone info)
- MX records (email)
- TXT records (verification, SPF, DMARC)

---

## Nameserver Decision Matrix

| Current Nameservers | Action Required |
|---------------------|-----------------|
| GoDaddy (`domaincontrol.com`) | ✅ Ready - use API to configure DNS |
| Netlify (`dns1.p0X.nsone.net`) | ✅ Configure in Netlify dashboard |
| Wix (`ns1.wix.com`) | ⚠️ Migrate to GoDaddy first |
| Cloudflare (`ns.cloudflare.com`) | ⚠️ Configure in Cloudflare dashboard OR migrate |
| FreeDNS/Other | ⚠️ Migrate to GoDaddy first |

**When to Migrate Nameservers:**
- When domain uses Wix, FreeDNS, or other external NS
- When you want centralized DNS management
- When GoDaddy API automation is desired

**When NOT to Migrate:**
- Domain actively uses services tied to current NS (e.g., Cloudflare CDN)
- Email services configured at current provider
- Unless you're sure migration won't break anything

---

## Testing Checklist

After deployment, verify ALL of these:

```bash
# 1. DNS resolution
nslookup yourdomain.com 8.8.8.8
# Expected: 75.2.60.5

# 2. HTTP redirect
curl -I http://yourdomain.com
# Expected: 301 Moved Permanently → https://yourdomain.com/

# 3. HTTPS with SSL
curl -I https://yourdomain.com
# Expected: 200 OK, Server: Netlify

# 4. WWW subdomain
curl -I http://www.yourdomain.com
# Expected: Redirects to https://yourdomain.com

# 5. Content loads
curl -sL https://yourdomain.com | grep "<title>"
# Expected: Your page title

# 6. Netlify headers
curl -I https://yourdomain.com | grep "X-Nf-Request-Id"
# Expected: X-Nf-Request-Id present (confirms Netlify)

# 7. SSL certificate valid
openssl s_client -connect yourdomain.com:443 -servername yourdomain.com < /dev/null 2>/dev/null | grep "Verify return code"
# Expected: Verify return code: 0 (ok)
```

All 7 tests must pass!

---

## DNS Propagation Times

| Change Type | Expected Time | Max Time |
|-------------|---------------|----------|
| A record update (same NS) | 1-5 minutes | 1 hour |
| CNAME record update | 1-5 minutes | 1 hour |
| Nameserver change | 1-24 hours | 48 hours |
| SSL certificate issuance | 1-2 minutes | 10 minutes |

**Pro tip**: Use https://dnschecker.org to check propagation worldwide.

---

## Deployment Time Estimate

**Per Website** (if everything goes smoothly):

| Step | Time |
|------|------|
| Check prerequisites | 1 min |
| Deploy to Netlify | 1-2 min |
| Add custom domain | 30 sec |
| Configure DNS | 30 sec |
| Provision SSL | 30 sec |
| DNS propagation | 2-5 min |
| Verification | 1 min |
| **Total** | **6-10 minutes** |

**If nameserver migration needed**: Add 30 minutes to 48 hours for propagation.

---

## Quick Reference Commands

```bash
# Deploy new site
cd /c/Users/peter/Downloads/CC/websites/yourdomain.com
echo "YesRight" | netlify sites:create --name yourdomain-com
netlify deploy --prod --dir=.

# Check nameservers
python /c/Users/peter/Downloads/CC/websites/check_domain_nameservers.py

# Check DNS records
python /c/Users/peter/Downloads/CC/websites/check_lakepakenham.py  # Modify for your domain

# Test site
curl -I https://yourdomain.com

# Flush local DNS cache (if site appears broken)
ipconfig /flushdns  # Windows
```

---

## Files & Scripts Reference

| Script | Purpose |
|--------|---------|
| `deploy_website_complete.py` | **USE THIS** - Full automated deployment |
| `setup_domains.py` | Add domain to Netlify + configure DNS |
| `migrate_nameservers.py` | Migrate from external NS to GoDaddy |
| `check_domain_nameservers.py` | Check which NS a domain uses |
| `check_lakepakenham.py` | Template for checking domain config |
| `enable_ssl_lakepakenham.py` | Template for provisioning SSL |

---

## When Things Go Wrong

### Emergency Rollback

If deployment breaks an existing site:

1. **Restore old DNS** (if you have backup)
2. **Remove custom domain** from Netlify
3. **Check GoDaddy forwarding** isn't enabled
4. **Wait for DNS cache** to clear (5-60 min)

### Get Help

1. Check Netlify dashboard: https://app.netlify.com/
2. Check DNS at authoritative nameserver: `nslookup yourdomain.com ns1.domaincontrol.com`
3. Check deployment logs in Netlify
4. Test with direct IP: `curl -H "Host: yourdomain.com" http://75.2.60.5`

---

## Success Criteria

Deployment is successful when:

✅ DNS resolves to `75.2.60.5`
✅ HTTP redirects to HTTPS
✅ HTTPS works with valid SSL
✅ Website content loads correctly
✅ www subdomain works
✅ No parking page / forwarding
✅ Netlify headers present

**DO NOT** mark deployment as complete until all criteria are met!

---

**Remember**: The goal is to deploy once correctly, not debug for an hour afterward!
