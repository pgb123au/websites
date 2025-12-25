# Kindly Call - Deployment Guide

## Status Summary

| Component | Status | Notes |
|-----------|--------|-------|
| **Database** | DEPLOYED | 8 tables in retellai_prod |
| **n8n Workflows** | DEPLOYED | 4 workflows ACTIVE |
| **Website** | READY | Static HTML/CSS/JS |
| **RetellAI Agent** | PENDING | Manual deploy required |

---

## 1. RetellAI Agent Deployment (MANUAL)

Per CLAUDE.md: Deploy scripts are broken. Use dashboard.

### Steps:

1. **Open RetellAI Dashboard**
   - URL: https://dashboard.retellai.com/
   - Use Yes AI / Production workspace (key_b790343f871e0e1e8e7e7fd06076)

2. **Import Agent**
   - Go to: Agents → Import Agent
   - File: `C:\Users\peter\Downloads\CC\retell\agents\KindlyCall_Wellness_v1.0.json`

3. **Connect Phone Number**
   - Go to: Phone Numbers section
   - Either:
     - Assign existing test number to this agent, OR
     - Purchase new Australian number (+61)

4. **Verify Configuration**
   - Voice: 11labs-Adrian
   - Speed: 0.85
   - Language: en-AU
   - Max call: 20 minutes

---

## 2. n8n Workflows (ALREADY DEPLOYED)

All 4 workflows are LIVE and ACTIVE:

| Workflow | ID | Webhook Path |
|----------|----|----|
| Call Complete | 9milFFfNppmJ8IqQ | /kindlycall/call-complete |
| Emergency Alert | d9tfArtJWqE6spaa | /kindlycall/emergency |
| Send SMS | P3X1f2zNbgoRL88J | /kindlycall/send-sms |
| Daily Report | 1j2jcmcvqFaOUsIO | Cron: 6pm AEDT daily |

Verify at: https://auto.yr.com.au/workflows

---

## 3. Test Call

**Test Patient (Peter Ball):**
- Phone: 0412111000
- Patient ID: 1805465202989210063

### To make a test call:

**Option A - Via RetellAI Dashboard:**
1. Open agent in dashboard
2. Click "Test Call"
3. Enter: +61412111000
4. Monitor console for webhook responses

**Option B - Via API:**
```bash
curl -X POST "https://api.retellai.com/v2/create-phone-call" \
  -H "Authorization: Bearer key_b790343f871e0e1e8e7e7fd06076" \
  -H "Content-Type: application/json" \
  -d '{
    "from_number": "+YOUR_RETELL_NUMBER",
    "to_number": "+61412111000",
    "agent_id": "AGENT_ID_AFTER_IMPORT",
    "metadata": {
      "recipient_id": "1805465202989210063",
      "nickname": "Peter",
      "caller_name": "Your family"
    }
  }'
```

---

## 4. Database Tables

All tables created in `retellai_prod`:

- kindlycall_users
- kindlycall_recipients
- kindlycall_recipient_access
- kindlycall_calls
- kindlycall_health_metrics
- kindlycall_alerts
- kindlycall_subscriptions
- kindlycall_medications

---

## 5. Website Deployment

Files ready at: `C:\Users\peter\Downloads\CC\websites\kindly-call\`

Deploy to Netlify:
```bash
cd websites/kindly-call
netlify deploy --prod
```

Or copy to any static hosting:
- index.html
- styles.css
- script.js

---

## Quick Test Commands

**Test webhooks:**
```bash
# Emergency webhook
curl -X POST "https://auto.yr.com.au/webhook/kindlycall/emergency" \
  -H "Content-Type: application/json" \
  -d '{"recipient_id":"test","emergency_type":"test","description":"Test"}'

# Call complete webhook
curl -X POST "https://auto.yr.com.au/webhook/kindlycall/call-complete" \
  -H "Content-Type: application/json" \
  -d '{"recipient_id":"test","call_status":"completed","call_duration":60}'
```

---

## Files Created

| File | Path |
|------|------|
| Agent JSON | `retell/agents/KindlyCall_Wellness_v1.0.json` |
| Workflow 1 | `n8n/JSON/active_workflows/kindlycall_call_complete.json` |
| Workflow 2 | `n8n/JSON/active_workflows/kindlycall_emergency.json` |
| Workflow 3 | `n8n/JSON/active_workflows/kindlycall_send_sms.json` |
| Workflow 4 | `n8n/JSON/active_workflows/kindlycall_daily_report.json` |
| Website | `websites/kindly-call/index.html` |
| CSS | `websites/kindly-call/styles.css` |
| JS | `websites/kindly-call/script.js` |
| Schema | `websites/kindly-call/database/schema.sql` |

---

**Created:** 2025-12-25
**Author:** Claude Code
