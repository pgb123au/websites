-- Kindly Call - Personalization Schema v2.0
-- New tables for rich personalization data
-- Created: 2025-12-25

-- ============================================================
-- NEW TABLE: Family Members
-- ============================================================
CREATE TABLE IF NOT EXISTS kindlycall_family_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipient_id UUID NOT NULL REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    relationship TEXT NOT NULL,  -- 'daughter', 'son', 'grandson', 'granddaughter', 'spouse', 'friend', 'neighbor', 'carer'
    age_range TEXT,              -- 'child', 'teen', 'adult', 'elderly'
    location TEXT,               -- 'lives nearby', 'Sydney', 'overseas'
    notes TEXT,                  -- "Visits every Sunday", "Works as a nurse"
    mention_frequency TEXT DEFAULT 'sometimes' CHECK (mention_frequency IN ('often', 'sometimes', 'rarely')),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_kindlycall_family_members_recipient ON kindlycall_family_members(recipient_id);

-- ============================================================
-- NEW TABLE: Pets
-- ============================================================
CREATE TABLE IF NOT EXISTS kindlycall_pets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipient_id UUID NOT NULL REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    type TEXT NOT NULL,          -- 'dog', 'cat', 'bird', 'fish', 'rabbit', 'other'
    breed TEXT,                  -- 'labrador', 'tabby', etc.
    notes TEXT,                  -- "Rescued, loves cuddles", "Very old, sleeps a lot"
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_kindlycall_pets_recipient ON kindlycall_pets(recipient_id);

-- ============================================================
-- NEW TABLE: Health Conditions
-- ============================================================
CREATE TABLE IF NOT EXISTS kindlycall_health_conditions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipient_id UUID NOT NULL REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
    condition TEXT NOT NULL,     -- 'arthritis', 'diabetes', 'heart condition', 'dementia', 'hearing loss'
    body_part TEXT,              -- 'knee', 'back', 'hands', 'hip', NULL for systemic
    severity TEXT CHECK (severity IN ('mild', 'moderate', 'severe')),
    can_mention BOOLEAN DEFAULT true,  -- OK to ask about in conversation?
    notes TEXT,                  -- "Had surgery last year", "Uses walker for this"
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_kindlycall_health_conditions_recipient ON kindlycall_health_conditions(recipient_id);
CREATE INDEX idx_kindlycall_health_conditions_mentionable ON kindlycall_health_conditions(recipient_id, can_mention) WHERE can_mention = true;

-- ============================================================
-- NEW TABLE: Upcoming Events
-- ============================================================
CREATE TABLE IF NOT EXISTS kindlycall_upcoming_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipient_id UUID NOT NULL REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
    event_type TEXT NOT NULL CHECK (event_type IN ('birthday', 'anniversary', 'visit', 'appointment', 'holiday', 'other')),
    event_date DATE NOT NULL,
    description TEXT NOT NULL,   -- "Grandson Tommy's 8th birthday", "Daughter Sarah visiting"
    recurring BOOLEAN DEFAULT false,  -- Annual event?
    mentioned BOOLEAN DEFAULT false,  -- Already mentioned in a call?
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_kindlycall_upcoming_events_recipient ON kindlycall_upcoming_events(recipient_id);
CREATE INDEX idx_kindlycall_upcoming_events_upcoming ON kindlycall_upcoming_events(recipient_id, event_date)
    WHERE event_date >= CURRENT_DATE AND mentioned = false;

-- ============================================================
-- NEW TABLE: SMS Onboarding State
-- ============================================================
CREATE TABLE IF NOT EXISTS kindlycall_sms_onboarding_state (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipient_id UUID NOT NULL REFERENCES kindlycall_recipients(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES kindlycall_users(id) ON DELETE CASCADE,
    phone_number TEXT NOT NULL,  -- Family member's phone for SMS
    current_step INTEGER DEFAULT 1,  -- 1-7 for the question sequence
    step_data JSONB DEFAULT '{}',    -- Accumulated answers
    last_message_at TIMESTAMPTZ,
    started_at TIMESTAMPTZ DEFAULT now(),
    completed_at TIMESTAMPTZ,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'completed', 'abandoned')),
    UNIQUE(recipient_id, user_id)
);

CREATE INDEX idx_kindlycall_sms_state_phone ON kindlycall_sms_onboarding_state(phone_number) WHERE status = 'active';

-- ============================================================
-- ALTER TABLE: Add personality fields to recipients
-- ============================================================
ALTER TABLE kindlycall_recipients
    ADD COLUMN IF NOT EXISTS personality_notes TEXT,
    ADD COLUMN IF NOT EXISTS topics_to_avoid TEXT[],
    ADD COLUMN IF NOT EXISTS communication_style TEXT CHECK (communication_style IN ('formal', 'casual', 'very_casual')),
    ADD COLUMN IF NOT EXISTS lives_alone BOOLEAN,
    ADD COLUMN IF NOT EXISTS has_hearing_issues BOOLEAN DEFAULT false,
    ADD COLUMN IF NOT EXISTS has_vision_issues BOOLEAN DEFAULT false,
    ADD COLUMN IF NOT EXISTS mobility_level TEXT CHECK (mobility_level IN ('independent', 'cane', 'walker', 'wheelchair', 'bedridden')),
    ADD COLUMN IF NOT EXISTS onboarding_complete BOOLEAN DEFAULT false,
    ADD COLUMN IF NOT EXISTS onboarding_method TEXT CHECK (onboarding_method IN ('web', 'phone', 'sms', 'mixed'));

-- ============================================================
-- HELPER FUNCTION: Format family members for agent
-- ============================================================
CREATE OR REPLACE FUNCTION kindlycall_format_family_members(p_recipient_id UUID)
RETURNS TEXT AS $$
DECLARE
    result TEXT := '';
    rec RECORD;
BEGIN
    FOR rec IN
        SELECT name, relationship, age_range, location
        FROM kindlycall_family_members
        WHERE recipient_id = p_recipient_id
        ORDER BY
            CASE relationship
                WHEN 'spouse' THEN 1
                WHEN 'daughter' THEN 2
                WHEN 'son' THEN 2
                WHEN 'grandson' THEN 3
                WHEN 'granddaughter' THEN 3
                ELSE 4
            END,
            name
        LIMIT 5  -- Max 5 family members per call context
    LOOP
        IF result != '' THEN
            result := result || ', ';
        END IF;

        result := result || 'your ' || rec.relationship || ' ' || rec.name;

        IF rec.age_range = 'child' THEN
            result := result || ' (little one)';
        ELSIF rec.location IS NOT NULL AND rec.location != '' THEN
            result := result || ' who lives in ' || rec.location;
        END IF;
    END LOOP;

    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- HELPER FUNCTION: Format pets for agent
-- ============================================================
CREATE OR REPLACE FUNCTION kindlycall_format_pets(p_recipient_id UUID)
RETURNS TEXT AS $$
DECLARE
    result TEXT := '';
    rec RECORD;
BEGIN
    FOR rec IN
        SELECT name, type, breed
        FROM kindlycall_pets
        WHERE recipient_id = p_recipient_id
        LIMIT 3
    LOOP
        IF result != '' THEN
            result := result || ' and ';
        END IF;

        result := result || 'your ' || rec.type || ' ' || rec.name;
    END LOOP;

    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- HELPER FUNCTION: Format health conditions for agent
-- ============================================================
CREATE OR REPLACE FUNCTION kindlycall_format_health_conditions(p_recipient_id UUID)
RETURNS TEXT AS $$
DECLARE
    result TEXT := '';
    rec RECORD;
BEGIN
    FOR rec IN
        SELECT condition, body_part
        FROM kindlycall_health_conditions
        WHERE recipient_id = p_recipient_id
          AND can_mention = true
        LIMIT 3
    LOOP
        IF result != '' THEN
            result := result || ', ';
        END IF;

        IF rec.body_part IS NOT NULL THEN
            result := result || 'your ' || rec.body_part;
            IF rec.condition IS NOT NULL AND rec.condition != '' THEN
                result := result || ' (' || rec.condition || ')';
            END IF;
        ELSE
            result := result || 'your ' || rec.condition;
        END IF;
    END LOOP;

    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- HELPER FUNCTION: Format upcoming events for agent
-- ============================================================
CREATE OR REPLACE FUNCTION kindlycall_format_upcoming_events(p_recipient_id UUID)
RETURNS TEXT AS $$
DECLARE
    result TEXT := '';
    rec RECORD;
    days_until INTEGER;
BEGIN
    FOR rec IN
        SELECT event_type, event_date, description
        FROM kindlycall_upcoming_events
        WHERE recipient_id = p_recipient_id
          AND event_date BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days'
          AND mentioned = false
        ORDER BY event_date
        LIMIT 2
    LOOP
        days_until := rec.event_date - CURRENT_DATE;

        IF result != '' THEN
            result := result || ', and ';
        END IF;

        result := result || rec.description;

        IF days_until = 0 THEN
            result := result || ' today';
        ELSIF days_until = 1 THEN
            result := result || ' tomorrow';
        ELSE
            result := result || ' coming up on ' || to_char(rec.event_date, 'Day');
        END IF;
    END LOOP;

    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- MASTER FUNCTION: Get full call context for a recipient
-- ============================================================
CREATE OR REPLACE FUNCTION kindlycall_get_call_context(p_recipient_id UUID)
RETURNS JSONB AS $$
DECLARE
    result JSONB;
    rec RECORD;
BEGIN
    SELECT INTO rec
        r.id,
        r.nickname,
        r.interests,
        r.health_notes,
        r.personality_notes,
        r.topics_to_avoid,
        r.communication_style,
        r.has_hearing_issues,
        r.mobility_level,
        kindlycall_format_family_members(r.id) as family_members,
        kindlycall_format_pets(r.id) as pets,
        kindlycall_format_health_conditions(r.id) as health_conditions,
        kindlycall_format_upcoming_events(r.id) as upcoming_events
    FROM kindlycall_recipients r
    WHERE r.id = p_recipient_id;

    IF NOT FOUND THEN
        RETURN NULL;
    END IF;

    result := jsonb_build_object(
        'recipient_id', rec.id,
        'nickname', COALESCE(rec.nickname, 'Friend'),
        'interests', COALESCE(rec.interests::text, ''),
        'health_notes', COALESCE(rec.health_notes::text, ''),
        'personality_notes', COALESCE(rec.personality_notes, ''),
        'topics_to_avoid', COALESCE(rec.topics_to_avoid, ARRAY[]::TEXT[]),
        'communication_style', COALESCE(rec.communication_style, 'casual'),
        'has_hearing_issues', COALESCE(rec.has_hearing_issues, false),
        'mobility_level', COALESCE(rec.mobility_level, 'independent'),
        'family_members', COALESCE(rec.family_members, ''),
        'pets', COALESCE(rec.pets, ''),
        'health_conditions', COALESCE(rec.health_conditions, ''),
        'upcoming_events', COALESCE(rec.upcoming_events, '')
    );

    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- Grant permissions
-- ============================================================
GRANT ALL ON kindlycall_family_members TO n8n;
GRANT ALL ON kindlycall_pets TO n8n;
GRANT ALL ON kindlycall_health_conditions TO n8n;
GRANT ALL ON kindlycall_upcoming_events TO n8n;
GRANT ALL ON kindlycall_sms_onboarding_state TO n8n;
GRANT EXECUTE ON FUNCTION kindlycall_format_family_members(UUID) TO n8n;
GRANT EXECUTE ON FUNCTION kindlycall_format_pets(UUID) TO n8n;
GRANT EXECUTE ON FUNCTION kindlycall_format_health_conditions(UUID) TO n8n;
GRANT EXECUTE ON FUNCTION kindlycall_format_upcoming_events(UUID) TO n8n;
GRANT EXECUTE ON FUNCTION kindlycall_get_call_context(UUID) TO n8n;

-- ============================================================
-- Summary
-- ============================================================
-- New tables: 5
--   - kindlycall_family_members
--   - kindlycall_pets
--   - kindlycall_health_conditions
--   - kindlycall_upcoming_events
--   - kindlycall_sms_onboarding_state
--
-- New columns on kindlycall_recipients: 9
--   - personality_notes, topics_to_avoid, communication_style
--   - lives_alone, has_hearing_issues, has_vision_issues, mobility_level
--   - onboarding_complete, onboarding_method
--
-- Helper functions: 5
--   - kindlycall_format_family_members()
--   - kindlycall_format_pets()
--   - kindlycall_format_health_conditions()
--   - kindlycall_format_upcoming_events()
--   - kindlycall_get_call_context() - Master function for call prep
