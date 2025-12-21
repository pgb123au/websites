# Deployment Scripts Reference

This directory contains automated deployment and management scripts for the websites project.

## Primary Deployment Script

### `deploy_website_complete.py` ⭐ **USE THIS FOR NEW DEPLOYMENTS**

Complete automated deployment script that handles everything:
- Checks prerequisites (files, nameservers)
- Deploys to Netlify
- Adds custom domain
- Configures DNS
- Provisions SSL
- Verifies deployment

**Usage:**
```bash
python deploy_website_complete.py <domain>
```

**Example:**
```bash
python deploy_website_complete.py mynewsite.com
```

**Requirements:**
- Domain directory must exist: `./mynewsite.com/`
- Must contain `index.html`
- Credentials in Windows Credential Manager

---

## DNS & Domain Management Scripts

### `setup_domains.py`
Adds custom domain to Netlify and configures DNS for multiple domains.

**Usage:**
```python
# Edit SITES list in script first
python setup_domains.py
```

### `migrate_nameservers.py`
Migrates domains from external nameservers (Wix, etc.) to GoDaddy.

**Usage:**
```python
# Edit DOMAINS_TO_MIGRATE list in script first
python migrate_nameservers.py
```

### `check_domain_nameservers.py`
Checks which nameservers a domain is using.

**Usage:**
```bash
python check_domain_nameservers.py
```

Shows nameservers for:
- irentmy.com
- trainingrobot.com
- gptbuilder.au

### `check_godaddy_forwarding.py`
Checks if a GoDaddy domain has parking/forwarding enabled.

**Usage:**
```python
# Edit domain variable in script
python check_godaddy_forwarding.py
```

---

## Site-Specific Diagnostic Scripts

### `check_lakepakenham.py`
Template for checking domain configuration (DNS, Netlify, SSL).

Shows:
- Nameservers
- DNS records
- Netlify configuration
- SSL status

**To use for another domain:**
1. Copy the file: `cp check_lakepakenham.py check_yourdomain.py`
2. Edit domain and site_id variables
3. Run: `python check_yourdomain.py`

### `fix_lakepakenham_dns.py`
Template for fixing DNS records to point to Netlify.

Updates:
- A record: @ → 75.2.60.5
- CNAME: www → sitename.netlify.app

### `enable_ssl_lakepakenham.py`
Template for provisioning SSL certificate via Netlify API.

---

## Testing Scripts

### `test_netlify_api.py`
Tests Netlify API access and shows site information.

**Usage:**
```python
# Edit site_id variable in script
python test_netlify_api.py
```

### `test_godaddy_api.py`
Tests GoDaddy API access and shows domain/DNS information.

**Usage:**
```bash
python test_godaddy_api.py
```

Shows:
- All GoDaddy domains matching target list
- DNS records for each domain
- Domain status

### `check_netlify_domains.py`
Checks Netlify domain aliases and attempts to add www subdomain.

**Usage:**
```python
# Edit site_id in script
python check_netlify_domains.py
```

---

## Troubleshooting Scripts

### `fix_trainingrobot_dns.py`
Example fix script for DNS issues after nameserver migration.

Handles:
- Domain status conflicts (409 errors)
- Retry logic for DNS updates
- Waits for domain status to stabilize

---

## Script Categories Quick Reference

| Need to... | Use this script |
|------------|-----------------|
| **Deploy a new website** | `deploy_website_complete.py` ⭐ |
| **Check nameservers** | `check_domain_nameservers.py` |
| **Migrate from Wix** | `migrate_nameservers.py` |
| **Fix DNS records** | `fix_lakepakenham_dns.py` (template) |
| **Enable SSL** | `enable_ssl_lakepakenham.py` (template) |
| **Check deployment status** | `check_lakepakenham.py` (template) |
| **Test Netlify API** | `test_netlify_api.py` |
| **Test GoDaddy API** | `test_godaddy_api.py` |
| **Add multiple domains** | `setup_domains.py` |

---

## Common Workflows

### Workflow 1: Deploy Brand New Site

```bash
# 1. Create website files
mkdir ./newsitee.com
cd ./newsite.com
# ... create index.html ...

# 2. Run automated deployment
cd ..
python deploy_website_complete.py newsite.com

# 3. Wait 5 minutes for DNS/SSL
# 4. Test: https://newsite.com
```

### Workflow 2: Fix Broken DNS

```bash
# 1. Check current status
python check_lakepakenham.py  # (modify for your domain)

# 2. Fix DNS records
python fix_lakepakenham_dns.py  # (modify for your domain)

# 3. Provision SSL if needed
python enable_ssl_lakepakenham.py  # (modify for your domain)

# 4. Wait 2-5 minutes and test
```

### Workflow 3: Migrate from External Nameservers

```bash
# 1. Check current nameservers
python check_domain_nameservers.py

# 2. Edit migrate_nameservers.py
#    Add domain to DOMAINS_TO_MIGRATE list

# 3. Run migration
python migrate_nameservers.py

# 4. Wait 24-48 hours for full propagation
```

### Workflow 4: Bulk Deploy Multiple Domains

```bash
# 1. Edit setup_domains.py
#    Add all domains to SITES list

# 2. Ensure nameservers are GoDaddy
python check_domain_nameservers.py

# 3. Run bulk setup
python setup_domains.py

# 4. Provision SSL for each site
# (may need to do this separately per site)
```

---

## Required Credentials

All scripts require credentials stored in Windows Credential Manager under `domain_mgr`:

| Service | Key Name | What It's For |
|---------|----------|---------------|
| Netlify | `netlify_token` | Deploy sites, add domains, SSL |
| GoDaddy | `godaddy_key` | DNS management |
| GoDaddy | `godaddy_secret` | DNS management |

**To check credentials:**
```python
import keyring
print(keyring.get_password('domain_mgr', 'netlify_token'))
print(keyring.get_password('domain_mgr', 'godaddy_key'))
print(keyring.get_password('domain_mgr', 'godaddy_secret'))
```

---

## Critical DNS Values

**Always use these for Netlify hosting:**

```
A record:     @ → 75.2.60.5 (TTL: 3600)
CNAME record: www → {sitename}.netlify.app (TTL: 3600)
```

**NEVER use:**
- Old AWS IPs (15.x.x.x, 3.x.x.x)
- Cloudflare IPs (unless using Cloudflare)
- Parking page IPs

---

## Error Handling

### "404 Not Found" from GoDaddy API
**Cause:** Domain uses external nameservers, not GoDaddy DNS
**Fix:** Migrate nameservers first or configure DNS at external provider

### "422 Unprocessable Entity" from Netlify
**Cause:** Domain already exists on another Netlify site
**Fix:** Remove domain from old site first, then add to new site

### "409 Conflict" from GoDaddy DNS API
**Cause:** Domain status is transitioning (e.g., nameservers just changed)
**Fix:** Wait 15-30 seconds and retry (see `fix_trainingrobot_dns.py`)

### "SSL provisioning failed"
**Cause:** DNS not propagated yet or pointing to wrong IP
**Fix:**
1. Verify DNS: `nslookup yourdomain.com 8.8.8.8` → should return 75.2.60.5
2. Wait 5 minutes for DNS propagation
3. Retry SSL provisioning

---

## Best Practices

1. **Always check nameservers first** before attempting DNS configuration
2. **Use templates** - copy diagnostic scripts and modify for your domain
3. **Wait for propagation** - DNS takes 1-5 minutes, nameserver changes take 24-48 hours
4. **Flush DNS cache** when testing: `ipconfig /flushdns` (Windows)
5. **Test with Google DNS**: `nslookup domain.com 8.8.8.8`
6. **Preserve existing records** - scripts keep NS, SOA, MX, TXT records
7. **Deploy first, configure DNS second** - don't configure DNS before site is deployed

---

## Documentation

- **Complete deployment procedure**: See `DEPLOYMENT_PROCEDURE.md`
- **Deployment status**: See `DEPLOYMENT.md`
- **GitHub repository**: https://github.com/pgb123au/websites

---

**Last Updated**: 2025-12-21
