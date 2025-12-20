# Website Deployment Guide

All 4 websites are built and ready for deployment to their respective domains.

## Websites Built

| Domain | Status | Description |
|--------|--------|-------------|
| **irentmy.com** | ✅ Built | Peer-to-peer rental marketplace platform |
| **trainingrobot.com** | ✅ Built | Robotics training & AI education platform |
| **gptbuilder.au** | ✅ Built | Custom AI solutions for Australian business |
| **lakepakenham.com** | ✅ Built | Complete guide to all lakes in Pakenham, Victoria |

## Deployment Instructions

### Option 1: Netlify CLI (Recommended)

For each domain, navigate to its directory and deploy:

```bash
# irentmy.com
cd /c/Users/peter/Downloads/CC/websites/irentmy.com
netlify deploy --prod --dir=.

# trainingrobot.com
cd /c/Users/peter/Downloads/CC/websites/trainingrobot.com
netlify deploy --prod --dir=.

# gptbuilder.au
cd /c/Users/peter/Downloads/CC/websites/gptbuilder.au
netlify deploy --prod --dir=.

# lakepakenham.com (already has site: 0e547869-b9d2-44d8-bdba-ce78104258d9)
cd /c/Users/peter/Downloads/CC/websites/lakepakenham.com
netlify link --id 0e547869-b9d2-44d8-bdba-ce78104258d9
netlify deploy --prod --dir=.
```

**Note**: lakepakenham.com already has an existing Netlify site. Link to it first before deploying.

### Option 2: Netlify Web UI

1. Log into https://app.netlify.com
2. Click "Add new site" > "Deploy manually"
3. Drag and drop the domain folder (e.g., `irentmy.com` folder)
4. Configure custom domain in site settings

### Option 3: GitHub Integration (Best for Ongoing Updates)

1. Create separate GitHub repos for each domain (or use monorepo)
2. Connect each repo to Netlify
3. Set build settings:
   - Build command: (none)
   - Publish directory: `.`
4. Add custom domains in Netlify site settings

## DNS Configuration

After deploying to Netlify, configure DNS in GoDaddy for each domain:

### For Netlify-hosted sites:

**Add these DNS records in GoDaddy:**

```
Type: CNAME
Name: www
Value: [your-netlify-site-name].netlify.app
TTL: 1 Hour

Type: A
Name: @
Value: 75.2.60.5
TTL: 1 Hour
```

**Or use Netlify DNS (recommended):**
1. In Netlify site settings, go to "Domain management"
2. Click "Add custom domain"
3. Enter your domain (e.g., `irentmy.com`)
4. Follow instructions to update nameservers in GoDaddy

## Domain-Specific Deployment Details

### irentmy.com
- **Features**: Peer-to-peer rental marketplace
- **Sections**: Hero, How It Works, Categories (8), Benefits, Waitlist
- **Design**: Purple/violet gradient
- **Forms**: Email waitlist signup

### trainingrobot.com
- **Features**: Robotics & AI education platform
- **Sections**: Hero, Features (4), Courses (4 levels), Learning Path, Target Audience
- **Design**: Blue gradient, tech-forward
- **Forms**: Email signup

### gptbuilder.au
- **Features**: Australian AI consulting services
- **Sections**: Hero, Services (4), Use Cases (6), Why Australian (4), Process (4), Contact
- **Design**: Dark teal gradient, professional B2B
- **Forms**: Full contact form (name, email, phone, company, message)
- **Special**: Australian flag badge, AEST support emphasis

### lakepakenham.com
- **Features**: All lakes in Pakenham guide
- **Lakes Featured**:
  1. Lake Pakenham
  2. Officer Lakes
  3. Cardinia Reservoir
  4. Heritage Springs Lake
  5. Lakeside Estate Lakes
  6. Toomuc Reserve Wetlands
- **Design**: Green/blue nature gradient
- **Special**: Google Maps links for each lake
- **Sections**: Lakes (6 cards), Activities (6), Visitor Info, Community, Contact
- **Existing Site**: 0e547869-b9d2-44d8-bdba-ce78104258d9

## Post-Deployment Checklist

After deploying each site:

- [ ] Verify site loads correctly on Netlify URL
- [ ] Test all internal navigation links
- [ ] Test all Google Maps links (lakepakenham.com)
- [ ] Verify responsive design on mobile
- [ ] Configure custom domain
- [ ] Enable HTTPS (automatic with Netlify)
- [ ] Test form submissions
- [ ] Update `domains.db` with `website_status='has_site'`

## Updating Sites

All sites are in the `websites` GitHub repository:
- **Repo**: https://github.com/pgb123au/websites
- **Main branch**: master

To update a site:
1. Edit the HTML file locally
2. Commit and push to GitHub
3. If using Netlify GitHub integration, site auto-deploys
4. If using manual deployment, run `netlify deploy --prod --dir=.`

## Monitoring

Check site status:
```bash
netlify status
```

View deployment history:
```bash
netlify deploy:list
```

## Troubleshooting

**Issue**: Site not loading
- Check Netlify deployment logs
- Verify DNS propagation (can take up to 48 hours)
- Use https://dnschecker.org to verify DNS

**Issue**: Forms not working
- Forms need backend integration (Netlify Forms, custom backend, or service like Formspree)
- Consider adding Netlify Forms: Add `netlify` attribute to `<form>` tag

**Issue**: 404 errors
- Ensure `netlify.toml` is in place
- Check publish directory is set to `.` (current directory)

## Next Steps

1. Deploy all 4 sites to Netlify
2. Configure custom domains
3. Test all sites thoroughly
4. Consider adding:
   - Form backend integration
   - Analytics (Google Analytics, Plausible)
   - SEO optimization (meta tags, sitemap.xml)
   - Contact form handling
5. Update domain database to track deployment status

---

**Last Updated**: 2025-12-21
**Repository**: https://github.com/pgb123au/websites
