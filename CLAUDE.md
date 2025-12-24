# Website Deployments

## Overview

Static website content and deployment scripts for various domains. This folder is a **separate git repo**.

---

## Directory Structure

```
websites/
├── gptbuilder.au/        <- GPT Builder landing page
├── irentmy.com/          <- iRentMy marketplace
├── lakepakenham.com/     <- Lake Pakenham site
├── monpangtiem.com/      <- Personal site
├── SmarterBlood/         <- SmarterBlood legacy content
├── trainingrobot.com/    <- Training Robot site
└── *.py                  <- Deployment scripts
```

---

## Key Files

| File | Purpose |
|------|---------|
| `deploy_website_complete.py` | Full deployment automation |
| `setup_domains.py` | Domain configuration |
| `migrate_nameservers.py` | NS migration |
| `DEPLOYMENT_PROCEDURE.md` | Step-by-step guide |
| `SCRIPTS_README.md` | Script documentation |

---

## Deployment Workflow

1. Create site content in subdirectory
2. Run deployment script:
```bash
python deploy_website_complete.py lakepakenham.com
```
3. Verify DNS and SSL

---

## Related Folders

- **Domains/** - Domain management and lookup
- **Netlify Sites** - Most sites deploy to Netlify

---

**Last Updated:** 2025-12-23
