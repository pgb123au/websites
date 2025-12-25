# Kindly Call Database Schema Documentation

**Database:** `retellai_prod` (PostgreSQL 17.6)
**Table Prefix:** `kindlycall_`
**Created:** 2025-12-25
**Status:** Deployed and verified

---

## Overview

The Kindly Call database schema supports a multi-tenant SaaS platform for AI-powered elderly check-in calls. The schema is designed to:

- Support multiple family members managing access to elderly recipients
- Track daily calls, transcripts, and AI-generated summaries
- Extract and monitor health metrics over time
- Generate emergency alerts and notifications
- Integrate with Stripe for subscription billing
- Manage medication reminders

---

## Tables Created

### 1. `kindlycall_users` (8 columns)
**Purpose:** Family members who create accounts and manage elderly care

**Key Columns:**
- `id` (UUID) - Primary key
- `email` (TEXT) - Unique, indexed
- `password_hash` (TEXT) - Encrypted passwords
- `name` (TEXT) - User's full name
- `phone` (TEXT) - For SMS alerts
- `timezone` (TEXT) - Default: 'Australia/Sydney'
- `created_at`, `updated_at` (TIMESTAMPTZ)

**Indexes:**
- Primary key on `id`
- Unique index on `email`
- Performance index on `email`

---

### 2. `kindlycall_recipients` (14 columns)
**Purpose:** Elderly individuals receiving daily check-in calls

**Key Columns:**
- `id` (UUID) - Primary key
- `owner_user_id` (UUID) - References `kindlycall_users(id)` CASCADE
- `name` (TEXT) - Recipient's legal name
- `nickname` (TEXT) - What the AI should call them
- `phone` (TEXT) - For calls
- `timezone` (TEXT) - Local time for call scheduling
- `status` (TEXT) - 'active', 'paused', 'cancelled'
- `call_time` (TIME) - Preferred call time (local)
- `call_days` (TEXT[]) - Days of week: ['mon', 'tue', ...]
- `health_notes` (JSONB) - Known conditions, mobility, hearing aids
- `interests` (JSONB) - Conversation topics, hobbies
- `emergency_contacts` (JSONB) - Escalation contacts

**Indexes:**
- Primary key on `id`
- Composite index on `(owner_user_id, status)` for dashboard queries

**Notes:**
- JSONB columns allow flexible health profile without schema changes
- `call_days` array enables flexible scheduling (daily, weekdays only, etc.)

---

### 3. `kindlycall_recipient_access` (5 columns)
**Purpose:** Multi-user access control for recipient dashboards

**Key Columns:**
- `id` (UUID) - Primary key
- `recipient_id` (UUID) - References `kindlycall_recipients(id)` CASCADE
- `user_id` (UUID) - References `kindlycall_users(id)` CASCADE
- `role` (TEXT) - 'owner', 'admin', 'viewer'
- `created_at` (TIMESTAMPTZ)

**Constraints:**
- Unique constraint on `(recipient_id, user_id)` - prevents duplicates

**Indexes:**
- Primary key on `id`
- Index on `user_id` for "my recipients" queries
- Index on `recipient_id` for "who has access" queries
- Unique index on `(recipient_id, user_id)`

**Use Cases:**
- Adult siblings sharing access to parent's dashboard
- Role-based permissions (view-only vs full access)
- Family invite system

---

### 4. `kindlycall_calls` (14 columns)
**Purpose:** Call records, transcripts, and AI analysis

**Key Columns:**
- `id` (UUID) - Primary key
- `recipient_id` (UUID) - References `kindlycall_recipients(id)` CASCADE
- `retell_call_id` (TEXT) - External RetellAI call ID, indexed
- `status` (TEXT) - 'scheduled', 'in_progress', 'completed', 'failed', 'no_answer'
- `scheduled_at` (TIMESTAMPTZ) - When call should happen
- `started_at`, `ended_at` (TIMESTAMPTZ) - Actual call times
- `duration_seconds` (INTEGER)
- `transcript` (JSONB) - Full conversation from RetellAI
- `summary` (TEXT) - AI-generated summary
- `sentiment` (JSONB) - Mood analysis
- `health_flags` (JSONB) - Detected concerns
- `recording_url` (TEXT) - Optional audio recording

**Indexes:**
- Primary key on `id`
- Composite index on `(recipient_id, scheduled_at DESC)` - optimizes call history queries
- Index on `(status, scheduled_at)` - for scheduled call processing
- Index on `retell_call_id` - RetellAI webhook lookups

**Query Optimization:**
- Most common query: "Show me recent calls for this recipient" → uses `idx_kindlycall_calls_recipient_date`
- Scheduled call processing: "Find all scheduled calls for today" → uses `idx_kindlycall_calls_status`

---

### 5. `kindlycall_health_metrics` (11 columns)
**Purpose:** Health tracking data extracted from call conversations

**Key Columns:**
- `id` (UUID) - Primary key
- `recipient_id` (UUID) - References `kindlycall_recipients(id)` CASCADE
- `call_id` (UUID) - References `kindlycall_calls(id)` SET NULL
- `date` (DATE) - Metric date
- `mood_score` (INTEGER 1-5) - 1=very poor, 5=excellent
- `sleep_quality` (INTEGER 1-5) - 1=very poor, 5=excellent
- `pain_level` (INTEGER 0-10) - 0=none, 10=severe
- `appetite` (TEXT) - 'good', 'poor', 'normal'
- `medication_taken` (BOOLEAN)
- `notes` (TEXT) - Additional observations

**Indexes:**
- Primary key on `id`
- Composite index on `(recipient_id, date DESC)` - trend analysis queries

**Check Constraints:**
- `mood_score` between 1 and 5
- `sleep_quality` between 1 and 5
- `pain_level` between 0 and 10
- `appetite` in ('good', 'poor', 'normal')

**Use Cases:**
- 30-day mood trend charts
- Sleep quality tracking
- Pain pattern detection
- Medication adherence monitoring

---

### 6. `kindlycall_alerts` (9 columns)
**Purpose:** Emergency and concern notifications for family members

**Key Columns:**
- `id` (UUID) - Primary key
- `recipient_id` (UUID) - References `kindlycall_recipients(id)` CASCADE
- `call_id` (UUID) - References `kindlycall_calls(id)` SET NULL
- `type` (TEXT) - 'emergency', 'missed_call', 'health_concern'
- `severity` (TEXT) - 'low', 'medium', 'high', 'critical'
- `message` (TEXT) - Alert description
- `acknowledged_at` (TIMESTAMPTZ) - When family acknowledged
- `acknowledged_by` (UUID) - References `kindlycall_users(id)`
- `created_at` (TIMESTAMPTZ)

**Indexes:**
- Primary key on `id`
- Partial index on `recipient_id` WHERE `acknowledged_at IS NULL` - dashboard unread alerts
- Partial index on `(severity, created_at DESC)` WHERE `acknowledged_at IS NULL` - priority sorting

**Check Constraints:**
- `severity` in ('low', 'medium', 'high', 'critical')

**Workflow:**
1. AI detects concern during call → creates alert
2. Family sees alert in dashboard
3. Family member clicks "acknowledge" → sets `acknowledged_at` and `acknowledged_by`
4. Alert moves to archive

**Partial Index Benefits:**
- Only unacknowledged alerts indexed → faster dashboard queries
- Acknowledged alerts don't slow down lookups

---

### 7. `kindlycall_subscriptions` (12 columns)
**Purpose:** Stripe subscription and billing management

**Key Columns:**
- `id` (UUID) - Primary key
- `user_id` (UUID) - References `kindlycall_users(id)` CASCADE
- `stripe_customer_id` (TEXT) - Indexed for Stripe webhooks
- `stripe_subscription_id` (TEXT)
- `plan` (TEXT) - 'starter', 'essential', 'daily', 'family'
- `status` (TEXT) - 'trialing', 'active', 'canceled', 'past_due'
- `current_period_start`, `current_period_end` (TIMESTAMPTZ)
- `trial_ends_at` (TIMESTAMPTZ) - 14-day trial tracking
- `canceled_at` (TIMESTAMPTZ)

**Indexes:**
- Primary key on `id`
- Index on `user_id` - user subscription lookups
- Index on `stripe_customer_id` - Stripe webhook processing
- Composite index on `(status, current_period_end)` - renewal processing

**Stripe Webhook Integration:**
- `checkout.session.completed` → Create subscription
- `invoice.paid` → Update `current_period_start/end`
- `invoice.payment_failed` → Set `status = 'past_due'`
- `customer.subscription.deleted` → Set `canceled_at`

**Plan Details:**
- **Starter**: $1/week (weekly billing)
- **Essential**: $19/month
- **Daily**: $39/month (most popular)
- **Family**: $69/month (up to 2 seniors)

---

### 8. `kindlycall_medications` (7 columns)
**Purpose:** Medication reminder configuration

**Key Columns:**
- `id` (UUID) - Primary key
- `recipient_id` (UUID) - References `kindlycall_recipients(id)` CASCADE
- `name` (TEXT) - Medication name
- `schedule` (TEXT) - 'morning', 'evening', 'with_meals', etc.
- `notes` (TEXT) - Dosage, special instructions
- `active` (BOOLEAN) - Default: true
- `created_at` (TIMESTAMPTZ)

**Indexes:**
- Primary key on `id`
- Partial index on `recipient_id` WHERE `active = true` - active medications only

**Integration:**
- AI agent receives active medications before call
- AI asks: "Have you taken your [medication name] this [morning/evening]?"
- Response tracked in `health_metrics.medication_taken`

---

## Index Summary

**Total Indexes:** 24 (including primary keys and unique constraints)

### Performance Optimizations

| Query Pattern | Optimized Index |
|--------------|-----------------|
| "Show recent calls for recipient" | `idx_kindlycall_calls_recipient_date` |
| "Find scheduled calls for today" | `idx_kindlycall_calls_status` |
| "RetellAI webhook lookup" | `idx_kindlycall_calls_retell_id` |
| "Show 30-day health trends" | `idx_kindlycall_health_metrics_recipient_date` |
| "Dashboard unacknowledged alerts" | `idx_kindlycall_alerts_recipient_unack` |
| "User's subscriptions" | `idx_kindlycall_subscriptions_user` |
| "Stripe webhook processing" | `idx_kindlycall_subscriptions_stripe_customer` |
| "User login" | `idx_kindlycall_users_email` |
| "Active medications for call" | `idx_kindlycall_medications_recipient_active` |

### Partial Indexes (Conditional)
- **Alerts**: Only indexes unacknowledged alerts (reduces index size)
- **Medications**: Only indexes active medications (excludes discontinued)

---

## Foreign Key Relationships

```
kindlycall_users (owner)
  ↓
kindlycall_recipients
  ↓
  ├─→ kindlycall_calls
  │     ↓
  │     ├─→ kindlycall_health_metrics
  │     └─→ kindlycall_alerts
  ├─→ kindlycall_recipient_access (multi-user)
  └─→ kindlycall_medications

kindlycall_users
  ↓
kindlycall_subscriptions (Stripe billing)
```

**Cascade Behavior:**
- Delete user → deletes their subscriptions (CASCADE)
- Delete recipient → deletes calls, alerts, medications (CASCADE)
- Delete recipient → does NOT delete shared access users
- Delete call → sets health_metrics.call_id to NULL (SET NULL)

---

## Data Types

### JSONB Columns (Flexible Schema)

**Why JSONB over TEXT or separate tables?**
- Schema flexibility without migrations
- Queryable with PostgreSQL JSON operators
- Already parsed (no JSON.parse() needed in code)
- Supports GIN indexes if needed later

**JSONB Usage:**

1. **`recipients.health_notes`**
   ```json
   {
     "conditions": ["arthritis", "hearing impaired"],
     "mobility": "walker",
     "hearing_aid": "left ear",
     "allergies": ["penicillin"]
   }
   ```

2. **`recipients.interests`**
   ```json
   ["gardening", "grandchildren", "cooking", "cricket"]
   ```

3. **`recipients.emergency_contacts`**
   ```json
   [
     {
       "name": "Sarah (daughter)",
       "phone": "+61412345678",
       "priority": 1
     },
     {
       "name": "John (son)",
       "phone": "+61498765432",
       "priority": 2
     }
   ]
   ```

4. **`calls.transcript`**
   ```json
   {
     "utterances": [
       {"speaker": "agent", "text": "Good morning Margaret!"},
       {"speaker": "user", "text": "Hello dear, how are you?"}
     ]
   }
   ```

5. **`calls.sentiment`**
   ```json
   {
     "overall_mood": "positive",
     "mood_score": 4,
     "keywords": ["happy", "looking forward"],
     "concerns": []
   }
   ```

6. **`calls.health_flags`**
   ```json
   {
     "concerns": ["mentioned not sleeping well", "pain in knee"],
     "severity": "medium",
     "requires_attention": true
   }
   ```

---

## Schema Version Control

**File:** `C:\Users\peter\Downloads\CC\websites\kindly-call\database\schema.sql`

**Idempotent Design:**
- All `CREATE TABLE` statements use `IF NOT EXISTS`
- All `CREATE INDEX` statements use `IF NOT EXISTS`
- Safe to re-run without errors

**Future Migrations:**
- Use separate migration files: `001_add_column.sql`, `002_add_index.sql`
- Always include rollback scripts
- Test on staging before production

---

## Testing Queries

### Verify all tables exist
```sql
SELECT tablename,
       (SELECT COUNT(*) FROM information_schema.columns
        WHERE table_name = t.tablename) as column_count
FROM pg_tables t
WHERE schemaname = 'public'
  AND tablename LIKE 'kindlycall_%'
ORDER BY tablename;
```

### Verify all indexes
```sql
SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
  AND tablename LIKE 'kindlycall_%'
ORDER BY tablename, indexname;
```

### Check foreign key constraints
```sql
SELECT
    tc.table_name,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name,
    tc.constraint_name
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_name LIKE 'kindlycall_%'
ORDER BY tc.table_name;
```

---

## Next Steps

1. **Row Level Security (RLS)**: Add Supabase RLS policies for multi-tenant security
2. **Seed Data**: Create test users, recipients, and sample calls
3. **API Integration**: Build Next.js API routes
4. **RetellAI Webhooks**: Connect webhook handlers to populate calls table
5. **Stripe Webhooks**: Connect subscription webhook handlers

---

**Deployment Date:** 2025-12-25
**Deployed To:** AWS EC2 (52.13.124.171), Docker container: n8n-postgres-1
**Database:** retellai_prod (PostgreSQL 17.6)
**Status:** ✅ Verified and documented
