-- Kindly Call Database Schema
-- Database: retellai_prod
-- Prefix: kindlycall_
-- Created: 2025-12-25
--
-- This schema supports:
-- - Multi-tenant family management
-- - Elderly recipient profiles and call scheduling
-- - Call records and transcripts
-- - Health metrics tracking
-- - Emergency alerting
-- - Stripe subscription management
-- - Medication reminders

-- ============================================================================
-- CORE TABLES
-- ============================================================================

-- Users: Family members who manage accounts
CREATE TABLE IF NOT EXISTS kindlycall_users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  name TEXT NOT NULL,
  phone TEXT,
  timezone TEXT DEFAULT 'Australia/Sydney',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Recipients: Elderly people receiving calls
CREATE TABLE IF NOT EXISTS kindlycall_recipients (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_user_id UUID REFERENCES kindlycall_users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  nickname TEXT, -- What to call them during calls
  phone TEXT NOT NULL,
  timezone TEXT DEFAULT 'Australia/Sydney',
  status TEXT DEFAULT 'active', -- active, paused, cancelled
  call_time TIME, -- Preferred call time (local time)
  call_days TEXT[] DEFAULT ARRAY['mon','tue','wed','thu','fri','sat','sun'],
  health_notes JSONB DEFAULT '{}', -- Known conditions, mobility notes, etc.
  interests JSONB DEFAULT '[]', -- Hobbies, conversation topics
  emergency_contacts JSONB DEFAULT '[]', -- Contact details for emergencies
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Recipient Access: Family members with access to recipient dashboard
CREATE TABLE IF NOT EXISTS kindlycall_recipient_access (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
  user_id UUID REFERENCES kindlycall_users(id) ON DELETE CASCADE,
  role TEXT DEFAULT 'viewer', -- owner, admin, viewer
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(recipient_id, user_id)
);

-- Calls: Call records and transcripts
CREATE TABLE IF NOT EXISTS kindlycall_calls (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
  retell_call_id TEXT, -- From RetellAI
  status TEXT DEFAULT 'scheduled', -- scheduled, in_progress, completed, failed, no_answer
  scheduled_at TIMESTAMPTZ,
  started_at TIMESTAMPTZ,
  ended_at TIMESTAMPTZ,
  duration_seconds INTEGER,
  transcript JSONB, -- Full conversation transcript
  summary TEXT, -- AI-generated summary
  sentiment JSONB, -- Mood analysis from conversation
  health_flags JSONB, -- Detected concerns or issues
  recording_url TEXT, -- Optional call recording URL
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Health Metrics: Extracted from calls
CREATE TABLE IF NOT EXISTS kindlycall_health_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
  call_id UUID REFERENCES kindlycall_calls(id) ON DELETE SET NULL,
  date DATE NOT NULL,
  mood_score INTEGER CHECK (mood_score >= 1 AND mood_score <= 5), -- 1-5 scale
  sleep_quality INTEGER CHECK (sleep_quality >= 1 AND sleep_quality <= 5), -- 1-5 scale
  pain_level INTEGER CHECK (pain_level >= 0 AND pain_level <= 10), -- 0-10 scale
  appetite TEXT CHECK (appetite IN ('good', 'poor', 'normal')),
  medication_taken BOOLEAN,
  notes TEXT, -- Additional health observations
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Alerts: Emergency and concern notifications
CREATE TABLE IF NOT EXISTS kindlycall_alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
  call_id UUID REFERENCES kindlycall_calls(id) ON DELETE SET NULL,
  type TEXT NOT NULL, -- emergency, missed_call, health_concern
  severity TEXT DEFAULT 'medium' CHECK (severity IN ('low', 'medium', 'high', 'critical')),
  message TEXT NOT NULL,
  acknowledged_at TIMESTAMPTZ,
  acknowledged_by UUID REFERENCES kindlycall_users(id),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Subscriptions: Stripe subscription tracking
CREATE TABLE IF NOT EXISTS kindlycall_subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES kindlycall_users(id) ON DELETE CASCADE,
  stripe_customer_id TEXT,
  stripe_subscription_id TEXT,
  plan TEXT NOT NULL, -- starter, essential, daily, family
  status TEXT DEFAULT 'trialing', -- trialing, active, canceled, past_due
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  trial_ends_at TIMESTAMPTZ,
  canceled_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Medications: Medication reminders
CREATE TABLE IF NOT EXISTS kindlycall_medications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  schedule TEXT, -- morning, evening, with_meals, etc.
  notes TEXT,
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================================

-- Call history queries (most common: recent calls by recipient)
CREATE INDEX IF NOT EXISTS idx_kindlycall_calls_recipient_date
  ON kindlycall_calls(recipient_id, scheduled_at DESC);

-- Call status lookups
CREATE INDEX IF NOT EXISTS idx_kindlycall_calls_status
  ON kindlycall_calls(status, scheduled_at);

-- RetellAI call ID lookups
CREATE INDEX IF NOT EXISTS idx_kindlycall_calls_retell_id
  ON kindlycall_calls(retell_call_id);

-- Health metrics by recipient and date
CREATE INDEX IF NOT EXISTS idx_kindlycall_health_metrics_recipient_date
  ON kindlycall_health_metrics(recipient_id, date DESC);

-- Unacknowledged alerts (dashboard query)
CREATE INDEX IF NOT EXISTS idx_kindlycall_alerts_recipient_unack
  ON kindlycall_alerts(recipient_id)
  WHERE acknowledged_at IS NULL;

-- Alert severity filtering
CREATE INDEX IF NOT EXISTS idx_kindlycall_alerts_severity
  ON kindlycall_alerts(severity, created_at DESC)
  WHERE acknowledged_at IS NULL;

-- Subscription lookups by user
CREATE INDEX IF NOT EXISTS idx_kindlycall_subscriptions_user
  ON kindlycall_subscriptions(user_id);

-- Active subscriptions
CREATE INDEX IF NOT EXISTS idx_kindlycall_subscriptions_status
  ON kindlycall_subscriptions(status, current_period_end);

-- Stripe customer ID lookups
CREATE INDEX IF NOT EXISTS idx_kindlycall_subscriptions_stripe_customer
  ON kindlycall_subscriptions(stripe_customer_id);

-- Recipient access lookups
CREATE INDEX IF NOT EXISTS idx_kindlycall_recipient_access_user
  ON kindlycall_recipient_access(user_id);

CREATE INDEX IF NOT EXISTS idx_kindlycall_recipient_access_recipient
  ON kindlycall_recipient_access(recipient_id);

-- Active recipients by owner
CREATE INDEX IF NOT EXISTS idx_kindlycall_recipients_owner_status
  ON kindlycall_recipients(owner_user_id, status);

-- Active medications
CREATE INDEX IF NOT EXISTS idx_kindlycall_medications_recipient_active
  ON kindlycall_medications(recipient_id)
  WHERE active = true;

-- User email lookups (for authentication)
CREATE INDEX IF NOT EXISTS idx_kindlycall_users_email
  ON kindlycall_users(email);

-- ============================================================================
-- COMMENTS FOR DOCUMENTATION
-- ============================================================================

COMMENT ON TABLE kindlycall_users IS 'Family members who manage elderly care accounts';
COMMENT ON TABLE kindlycall_recipients IS 'Elderly individuals receiving daily check-in calls';
COMMENT ON TABLE kindlycall_recipient_access IS 'Multi-user access control for recipient dashboards';
COMMENT ON TABLE kindlycall_calls IS 'Call records including transcripts and AI analysis';
COMMENT ON TABLE kindlycall_health_metrics IS 'Health tracking data extracted from conversations';
COMMENT ON TABLE kindlycall_alerts IS 'Emergency and concern notifications for family members';
COMMENT ON TABLE kindlycall_subscriptions IS 'Stripe billing and subscription management';
COMMENT ON TABLE kindlycall_medications IS 'Medication reminders configured per recipient';

COMMENT ON COLUMN kindlycall_recipients.call_days IS 'Array of days to call: mon, tue, wed, thu, fri, sat, sun';
COMMENT ON COLUMN kindlycall_recipients.health_notes IS 'JSONB: Known conditions, mobility notes, hearing aids, etc.';
COMMENT ON COLUMN kindlycall_recipients.interests IS 'JSONB array: Hobbies, favorite topics for conversation';
COMMENT ON COLUMN kindlycall_recipients.emergency_contacts IS 'JSONB array: Contact details for escalation';

COMMENT ON COLUMN kindlycall_calls.transcript IS 'JSONB: Full conversation transcript from RetellAI';
COMMENT ON COLUMN kindlycall_calls.sentiment IS 'JSONB: AI mood analysis and emotional state';
COMMENT ON COLUMN kindlycall_calls.health_flags IS 'JSONB: Detected concerns or anomalies';

COMMENT ON COLUMN kindlycall_health_metrics.mood_score IS '1=very poor, 5=excellent';
COMMENT ON COLUMN kindlycall_health_metrics.sleep_quality IS '1=very poor, 5=excellent';
COMMENT ON COLUMN kindlycall_health_metrics.pain_level IS '0=no pain, 10=severe pain';

-- ============================================================================
-- GRANT PERMISSIONS (if needed)
-- ============================================================================

-- Note: Adjust permissions based on your database user setup
-- These are commented out as they may vary by environment

-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO n8n;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO n8n;
