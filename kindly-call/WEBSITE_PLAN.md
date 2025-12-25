# Kindly Call - Website Implementation Plan
## World-Class AI-Powered Elderly Check-In Service

**Version:** 1.0
**Date:** 2025-12-25
**Status:** PLANNING PHASE - Awaiting Approval

---

## Table of Contents

1. [Executive Overview](#1-executive-overview)
2. [Target Audiences](#2-target-audiences)
3. [Page Structure](#3-page-structure)
4. [Key Features](#4-key-features)
5. [Technical Architecture](#5-technical-architecture)
6. [Database Schema](#6-database-schema)
7. [Authentication & Authorization](#7-authentication--authorization)
8. [Payment Integration](#8-payment-integration)
9. [RetellAI Integration](#9-retellai-integration)
10. [Design System](#10-design-system)
11. [Accessibility Requirements](#11-accessibility-requirements)
12. [Security & Privacy](#12-security--privacy)
13. [Go-to-Market Features](#13-go-to-market-features)
14. [Implementation Phases](#14-implementation-phases)

---

## 1. Executive Overview

### Vision
Build a world-class website that instills trust, communicates value clearly, and provides a seamless experience for families signing up their elderly loved ones for AI-powered daily check-in calls.

### Key Differentiators from Research
1. **Australian-First Design** - Local accents, culture, emergency integration (000)
2. **Comprehensive Health Monitoring** - Not just safety, but wellness tracking
3. **Family Dashboard** - Real-time insights and daily summaries
4. **Transparency** - Clear about AI technology, builds trust
5. **Affordable** - From just $1/week vs expensive human alternatives

### Success Metrics
- Conversion rate: 3-5% visitor to trial signup
- Trial to paid: 50%+ conversion
- Load time: <2 seconds
- Accessibility: WCAG 2.1 AA compliant
- Mobile traffic performance: Same as desktop

---

## 2. Target Audiences

### Primary: Adult Children (Ages 35-60)
**Persona: "Worried Sarah"**
- Has elderly parent living alone (60km away)
- Works full-time, can't visit daily
- Worried about falls, loneliness, health decline
- Wants peace of mind without surveillance
- Tech-savvy, mobile-first

**Pain Points:**
- Guilt about not calling daily
- Fear of emergency going unnoticed
- Can't afford $50+/hour companion care
- Doesn't want to invade parent's privacy

**What They Need to See:**
- Clear explanation of how service works
- Transparent pricing
- Real testimonials from families
- Sample conversation transcripts
- Easy signup process

### Secondary: Elderly Individuals (65+)
**Persona: "Independent Don"**
- Lives alone, values independence
- Doesn't want to be a "burden" on family
- May have hearing difficulties
- Skeptical of new technology
- Uses landline phone

**Pain Points:**
- Lonely, especially mornings
- Family worries about him
- Suspicious of phone scams
- Doesn't want surveillance devices

**What They Need:**
- Reassurance about privacy
- Clear explanation it's a phone call
- No equipment to install
- Friendly, respectful tone

### Tertiary: Aged Care Providers (B2B)
**Persona: "Provider Patricia"**
- Runs home care service
- Needs scalable wellness check solution
- Interested in Support at Home funding
- Wants reporting and compliance features

---

## 3. Page Structure

### 3.1 Public Pages (No Authentication)

#### Home Page `/`
**Purpose:** Capture attention, explain value, drive signups

**Sections:**
1. **Hero**
   - Headline: "Daily Check-In Calls That Care"
   - Subheadline: "AI-powered wellness calls for elderly Australians, with family insights and peace of mind"
   - CTA: "Start Free Trial" + "See How It Works"
   - Trust badges: "Australian Made", "Privacy Protected", "No Equipment Needed"
   - Background: Warm image of elderly person on phone, smiling

2. **How It Works** (3-step visual)
   - Step 1: "Sign Up" - Choose plan, add your loved one's details
   - Step 2: "Daily Calls" - Friendly AI calls at preferred time
   - Step 3: "Stay Connected" - Get summaries, alerts, and peace of mind

3. **What Families Say** (Testimonials)
   - 3-4 rotating testimonials
   - Include photos (stock or real beta testers)
   - Star ratings
   - Location (city/state)

4. **Sample Conversation**
   - Interactive player showing example call
   - Highlights: greeting, health check, chat, farewell
   - Shows how AI sounds warm and natural

5. **Health Insights Preview**
   - Screenshot of dashboard
   - Shows: mood tracking, sleep quality, activity levels
   - Highlight anomaly detection

6. **Pricing Preview**
   - Headline: "From just $1 per week"
   - 4 plan cards (Starter, Essential, Daily, Family)
   - Highlight "Daily" as best value
   - CTA: "View Full Pricing"

7. **FAQ Snippets**
   - Top 4 questions
   - Link to full FAQ

8. **Final CTA**
   - "Give Your Family Peace of Mind"
   - Free trial button
   - Phone number for questions

---

#### How It Works Page `/how-it-works`
**Purpose:** Detailed explanation for skeptical visitors

**Sections:**
1. **Overview Video** (2-3 min explainer)
2. **Detailed Steps**
   - Sign up process walkthrough
   - Call scheduling explained
   - What happens during a call (with transcript example)
   - How family receives updates
   - Emergency protocols
3. **Technology Explanation**
   - "Powered by advanced AI voice technology"
   - "Australian accents and cultural understanding"
   - "Your loved one speaks to a consistent, caring voice"
4. **For Elderly Users**
   - "What your parent experiences"
   - Reassurance about ease of use
   - No equipment needed

---

#### Pricing Page `/pricing`
**Purpose:** Clear pricing with compelling entry point, drive conversions and upsells

**Marketing Hook:** "From just $1 per week"

**Plans:**

| Feature | Starter $1/week | Essential $19/mo | Daily $39/mo | Family $69/mo |
|---------|-----------------|------------------|--------------|---------------|
| **Marketing** | "From $1/week" | "Most Popular" | "Best Value" | "Complete Care" |
| Calls | 1/week | 3/week | Daily | Daily |
| Call duration | Up to 3 min | Up to 5 min | Up to 8 min | Up to 10 min |
| Family dashboard | No | Basic | Full | Full |
| Family members | 1 (email only) | 1 | Up to 3 | Up to 5 |
| Seniors covered | 1 | 1 | 1 | Up to 2 |
| Call summaries | Email only | Email + web | Full AI insights | Full AI insights |
| Health tracking | No | Basic | Advanced + trends | Advanced + trends |
| Emergency alerts | SMS to 1 contact | SMS to 2 contacts | Priority + push | Priority + push |
| Medication reminders | No | No | Yes | Yes |
| Call time flexibility | Fixed day/time | Choose days | Flexible window | Flexible window |
| SMS fallback on missed | No | Yes | Yes | Yes |
| Priority support | No | No | No | Yes |
| **Upsell trigger** | - | "Add more calls" | "Add family members" | "Add more seniors" |

**Pricing Psychology:**
- **Starter**: Loss leader / break-even (~$4.33/mo, ~$3.28 cost) - hooks customers
- **Essential**: First profitable tier - natural upgrade when weekly isn't enough
- **Daily**: Main revenue tier - where most customers should land
- **Family**: Premium for multi-senior households

**Free Trial:**
- **14-day free trial** on ALL plans - no credit card required
- During trial: Full access to chosen tier's features
- Trial includes 2 calls for Starter, 6 calls for Essential, 14 calls for Daily/Family
- Email reminders: Day 10 ("4 days left"), Day 13 ("Last day - add payment to continue")
- If no payment added: Service pauses, data retained 30 days
- Easy reactivation anytime

**Marketing:** "Try FREE for 14 days. From just $1/week after."

**Billing Options:**
- Starter: Weekly billing ONLY ($1/week = $4.33/mo equivalent)
- All others: Monthly or Annual (save 2 months = 16% discount)

**Upsell Prompts (In-App):**
- After 2 weeks on Starter: "Upgrade to Essential for more calls"
- If missed call concern: "Upgrade for daily peace of mind"
- If family member tries to add: "Upgrade to Daily for family access"
- After call > 3 min ends: "Your loved one wanted to chat longer. Upgrade for extended calls."

**Additional Elements:**
- Hero: "Try FREE for 14 days. Then from just $1 per week."
- Sub-hero: "No credit card required. No obligations."
- Trust: "No lock-in contracts. Cancel anytime."
- Social proof: Testimonials near each tier
- FAQ about billing, upgrades, cancellation
- Enterprise/B2B inquiry form (aged care providers: volume discounts from $8/resident/mo)

---

#### About Us Page `/about`
**Purpose:** Build trust, show humanity

**Sections:**
1. **Our Mission**
   - "Keeping families connected with care"
   - Personal story (founder motivation)
2. **The Problem We're Solving**
   - Statistics on elderly loneliness
   - Impact on health
   - Family stress
3. **Why AI?**
   - Honest about AI technology
   - Complement to family, not replacement
   - Available every day, consistently caring
4. **Australian Values**
   - Built for Australians
   - Understanding of local culture
   - Data stored in Australia
5. **Team** (if applicable)
6. **Partners & Certifications**

---

#### FAQ Page `/faq`
**Purpose:** Address objections, build trust

**Categories:**
- **Getting Started** (signup, trial, cancellation)
- **How Calls Work** (timing, duration, what's asked)
- **Technology** (AI explanation, privacy, data)
- **Pricing & Billing** (plans, upgrades, refunds)
- **For Elderly Users** (phone types, hearing issues)
- **Emergency Situations** (what happens if concern detected)
- **Family Dashboard** (access, notifications, sharing)

---

#### Contact Page `/contact`
**Purpose:** Human touchpoint

**Elements:**
- Contact form (name, email, message)
- Phone number: 1800 XXX XXX (freecall)
- Email: hello@kindlycall.com.au
- Hours: 9am-5pm AEST Mon-Fri
- Response time: "We respond within 24 hours"

---

#### Privacy Policy `/privacy`
**Purpose:** Legal compliance, trust building

**Key Sections:**
- What data we collect
- How we use data
- Call recording and transcripts
- Data storage (Australia)
- Family access to data
- Data retention
- Rights (deletion, access)
- Contact for privacy concerns

---

#### Terms of Service `/terms`
**Purpose:** Legal protection

---

### 3.2 Protected Pages (Authentication Required)

#### Dashboard Home `/dashboard`
**Purpose:** Family member overview

**Widgets:**
- **Today's Call Status**
  - Scheduled time
  - Status: Completed / Scheduled / Missed
  - Quick summary if completed
- **Health Snapshot**
  - Mood trend (7 days)
  - Sleep quality (7 days)
  - Activity level
  - Any concerns flagged
- **Recent Alerts**
  - Emergency alerts
  - Missed calls
  - Health anomalies
- **Quick Actions**
  - View today's transcript
  - Adjust call time
  - Add medication reminder

---

#### Call History `/dashboard/calls`
**Purpose:** Browse past calls

**Features:**
- Date filter
- Search transcripts
- View full transcript
- Listen to audio (if recorded)
- AI-generated summary for each call
- Flag concerning calls
- Export to PDF

---

#### Health Insights `/dashboard/health`
**Purpose:** Track trends over time

**Visualizations:**
- **Mood Tracking** (line chart, 30 days)
- **Sleep Quality** (bar chart)
- **Pain/Discomfort Reports** (timeline)
- **Medication Adherence** (percentage)
- **Social Interaction** (mentions of visitors, calls)
- **Anomaly Highlights** (AI-detected changes)

**Filters:**
- Date range
- Specific metrics
- Compare periods

---

#### Profile Settings `/dashboard/settings`
**Purpose:** Manage elderly person's profile

**Sections:**
- **Basic Info** (name, phone, timezone)
- **Call Preferences**
  - Preferred call time
  - Backup time if no answer
  - Days to call (daily, weekdays only)
- **Health Profile**
  - Known conditions (optional)
  - Medications (for reminders)
  - Mobility notes
  - Hearing notes
- **Interests & Conversation Topics**
  - Hobbies
  - Family members to ask about
  - Favorite topics
- **Emergency Contacts**
  - Primary contact
  - Secondary contacts
  - Local emergency (optional)

---

#### Family Members `/dashboard/family`
**Purpose:** Manage who can access dashboard

**Features:**
- Invite family members
- Set permission levels (view only, full access)
- Remove access
- View last login

---

#### Account Settings `/dashboard/account`
**Purpose:** Billing and account management

**Sections:**
- **Subscription**
  - Current plan
  - Upgrade/downgrade
  - Cancel subscription
- **Billing History**
  - Invoices
  - Payment method
  - Update card
- **Notifications**
  - Email preferences
  - SMS alerts
  - Push notifications (if mobile app)
- **Account Security**
  - Change password
  - Two-factor authentication

---

### 3.3 Admin Pages (Staff Only)

#### Admin Dashboard `/admin`
- Total active subscriptions
- Daily call volume
- Revenue metrics
- Alert queue

#### Customer Management `/admin/customers`
- Search customers
- View account details
- Manual actions (pause, refund)

#### Call Monitoring `/admin/calls`
- Live call status
- Failed calls queue
- Quality metrics

#### Content Management `/admin/content`
- Update FAQ
- Manage testimonials
- Blog posts

---

## 4. Key Features

### 4.1 Signup Flow

**Steps:**
1. **Start Trial**
   - Email address
   - Password
   - Verification email

2. **About Your Loved One**
   - Their name
   - Their phone number
   - Relationship to you
   - Timezone/location

3. **Call Preferences**
   - Preferred call time (morning/afternoon/evening)
   - Best days
   - What to call them (formal name vs nickname)

4. **Your Profile**
   - Your name
   - Your phone (for alerts)
   - Invite other family members (optional)

5. **Trial Confirmation**
   - Summary of setup
   - First call scheduled
   - Dashboard access granted

### 4.2 Family Dashboard Features

**Real-time Updates:**
- Call completion notifications (push/email)
- Daily summary email (configurable time)
- Instant emergency alerts

**AI-Generated Insights:**
- Sentiment analysis of conversations
- Health trend detection
- Anomaly flagging (e.g., "Mentioned not sleeping well 3 days in a row")
- Weekly summary report

**Call Customization:**
- Adjust call times
- Add specific questions to ask
- Add medication reminders
- Special occasion messages (birthday wishes)

### 4.3 Emergency Escalation

**Trigger Conditions:**
- Explicit distress ("I've fallen", "I need help")
- Health keywords ("chest pain", "can't breathe")
- No answer after 3 attempts
- Unusual responses detected by AI

**Escalation Actions:**
1. Immediate SMS to all family members
2. Auto-retry call in 5 minutes
3. Dashboard alert
4. Optional: Notify nominated emergency contact
5. Provide guidance for calling 000

### 4.4 Onboarding for Elderly

**Pre-Call Setup:**
- Family can record a voice message introducing the service
- First call acknowledges "Your [daughter/son] Sarah signed you up for daily check-in calls"
- Initial calls are shorter, building familiarity

**Gradual Engagement:**
- Week 1: Simple wellness check (2-3 min)
- Week 2: Add conversation topics (4-5 min)
- Week 3+: Full personalized calls (5-10 min)

---

## 5. Technical Architecture

### 5.1 Frontend Stack

**Framework:** Next.js 15 (App Router)
- Server Components for SEO
- Client Components for interactivity
- API Routes for backend endpoints

**Styling:** Tailwind CSS 4.0
- Utility-first approach
- Consistent design tokens
- Dark mode support (optional)

**Component Library:** shadcn/ui
- Accessible components
- Customizable
- TypeScript support

**State Management:**
- Zustand for client state
- React Query (TanStack Query) for server state

**Forms:** React Hook Form + Zod validation

### 5.2 Backend Architecture

**API:** Next.js API Routes + Route Handlers
- RESTful endpoints
- Type-safe with TypeScript
- Rate limiting via Vercel

**Database:** Supabase (PostgreSQL)
- Australian region (Sydney)
- Row Level Security for multi-tenant access
- Real-time subscriptions for live updates

**File Storage:** Supabase Storage
- Call recordings (optional)
- Profile images

**Background Jobs:** Vercel Cron + Inngest
- Daily report generation
- Scheduled call triggers
- Cleanup tasks

### 5.3 External Integrations

| Service | Purpose | Priority |
|---------|---------|----------|
| **RetellAI** | Voice agent, call management | Critical |
| **Supabase** | Database, auth, storage | Critical |
| **Stripe** | Payments, subscriptions | Critical |
| **Resend** | Transactional emails | High |
| **Twilio** | SMS notifications | High |
| **Vercel** | Hosting, edge functions | Critical |
| **Sentry** | Error monitoring | High |
| **PostHog** | Analytics | Medium |

### 5.4 Hosting & Infrastructure

**Primary:** Vercel
- Sydney edge location
- Automatic SSL
- Preview deployments
- Serverless functions

**Database:** Supabase
- Sydney region
- Automatic backups
- Connection pooling

**CDN:** Vercel Edge Network
- Australian POP
- Image optimization

---

## 6. Database Schema

### Core Tables

```sql
-- Users (family members who manage accounts)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  name TEXT NOT NULL,
  phone TEXT,
  timezone TEXT DEFAULT 'Australia/Sydney',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Elderly recipients (people receiving calls)
CREATE TABLE recipients (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  nickname TEXT, -- What to call them
  phone TEXT NOT NULL,
  timezone TEXT DEFAULT 'Australia/Sydney',
  status TEXT DEFAULT 'active', -- active, paused, cancelled
  call_time TIME, -- Preferred call time
  call_days TEXT[] DEFAULT ARRAY['mon','tue','wed','thu','fri','sat','sun'],
  health_notes JSONB DEFAULT '{}',
  interests JSONB DEFAULT '[]',
  emergency_contacts JSONB DEFAULT '[]',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Family members with access to recipient dashboard
CREATE TABLE recipient_access (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES recipients(id) ON DELETE CASCADE,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  role TEXT DEFAULT 'viewer', -- owner, admin, viewer
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(recipient_id, user_id)
);

-- Call records
CREATE TABLE calls (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES recipients(id) ON DELETE CASCADE,
  retell_call_id TEXT, -- From RetellAI
  status TEXT DEFAULT 'scheduled', -- scheduled, in_progress, completed, failed, no_answer
  scheduled_at TIMESTAMPTZ,
  started_at TIMESTAMPTZ,
  ended_at TIMESTAMPTZ,
  duration_seconds INTEGER,
  transcript JSONB,
  summary TEXT, -- AI-generated summary
  sentiment JSONB, -- Mood analysis
  health_flags JSONB, -- Detected concerns
  recording_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Health tracking (extracted from calls)
CREATE TABLE health_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES recipients(id) ON DELETE CASCADE,
  call_id UUID REFERENCES calls(id) ON DELETE SET NULL,
  date DATE NOT NULL,
  mood_score INTEGER, -- 1-5
  sleep_quality INTEGER, -- 1-5
  pain_level INTEGER, -- 0-10
  appetite TEXT, -- good, poor, normal
  medication_taken BOOLEAN,
  notes TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Emergency alerts
CREATE TABLE alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES recipients(id) ON DELETE CASCADE,
  call_id UUID REFERENCES calls(id) ON DELETE SET NULL,
  type TEXT NOT NULL, -- emergency, missed_call, health_concern
  severity TEXT DEFAULT 'medium', -- low, medium, high, critical
  message TEXT NOT NULL,
  acknowledged_at TIMESTAMPTZ,
  acknowledged_by UUID REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Subscriptions
CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  stripe_customer_id TEXT,
  stripe_subscription_id TEXT,
  plan TEXT NOT NULL, -- basic, premium, family
  status TEXT DEFAULT 'trialing', -- trialing, active, canceled, past_due
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  trial_ends_at TIMESTAMPTZ,
  canceled_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Medication reminders
CREATE TABLE medications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recipient_id UUID REFERENCES recipients(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  schedule TEXT, -- morning, evening, with_meals
  notes TEXT,
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Indexes

```sql
CREATE INDEX idx_calls_recipient_date ON calls(recipient_id, scheduled_at DESC);
CREATE INDEX idx_health_metrics_recipient_date ON health_metrics(recipient_id, date DESC);
CREATE INDEX idx_alerts_recipient_unack ON alerts(recipient_id) WHERE acknowledged_at IS NULL;
CREATE INDEX idx_subscriptions_user ON subscriptions(user_id);
```

---

## 7. Authentication & Authorization

### Provider: Clerk
**Why Clerk:**
- Pre-built UI components
- Multi-factor authentication
- Role-based access control
- Session management
- Australian data processing available

### User Roles

| Role | Access |
|------|--------|
| **Owner** | Full access to recipient, billing, can delete |
| **Admin** | Full access except billing and deletion |
| **Viewer** | View dashboard, call history, alerts only |

### Auth Flow

1. **Signup:** Email + password → Email verification → Dashboard
2. **Login:** Email + password → Optional MFA → Dashboard
3. **Password Reset:** Email link → New password
4. **Invite Family:** Email invite → Create account → Auto-linked to recipient

### Row Level Security (Supabase)

```sql
-- Users can only see their own data
CREATE POLICY "Users see own data" ON users
  FOR SELECT USING (auth.uid() = id);

-- Users can access recipients they have access to
CREATE POLICY "Access shared recipients" ON recipients
  FOR SELECT USING (
    id IN (
      SELECT recipient_id FROM recipient_access
      WHERE user_id = auth.uid()
    )
  );
```

---

## 8. Payment Integration

### Provider: Stripe Australia

**Products:**
- Starter: $1/week (AUD) - weekly recurring
- Essential: $19/month (AUD)
- Daily: $39/month (AUD)
- Family: $69/month (AUD)

**Features:**
- **14-day free trial** - no credit card required upfront
- Starter: Weekly billing (simpler, lower commitment feel)
- Other tiers: Monthly or annual billing (16% discount = 2 months free)
- Card collected at end of trial or when user ready
- Automatic card retry on failed payments
- Proration on plan upgrades
- Easy upgrade path with prorated credits
- Refund handling (pro-rata for annual)

**Trial Flow (Stripe):**
1. User signs up → Creates Stripe Customer (no payment method)
2. Trial starts → Subscription with `trial_end` set to +14 days
3. Day 10 → Email reminder to add payment
4. Day 13 → Final reminder
5. Day 14 → If payment method added: charge begins. If not: subscription pauses
6. Webhook: `customer.subscription.trial_will_end` triggers reminders

### Stripe Integration Points

1. **Checkout:** Stripe Checkout for initial subscription
2. **Customer Portal:** Stripe Customer Portal for billing management
3. **Webhooks:**
   - `checkout.session.completed` → Activate subscription
   - `invoice.paid` → Confirm payment
   - `invoice.payment_failed` → Notify user
   - `customer.subscription.updated` → Plan changes
   - `customer.subscription.deleted` → Handle cancellation

### Pricing Table UI
Use Stripe Pricing Table embed for consistent pricing display.

---

## 9. RetellAI Integration

### Webhook Endpoints

```typescript
// POST /api/retell/call-scheduled
// Receives notification when call is scheduled

// POST /api/retell/call-started
// Real-time call start notification

// POST /api/retell/call-completed
// Full call data including transcript

// POST /api/retell/emergency
// Immediate alert for detected emergencies
```

### Call Scheduling Flow

```
1. Daily cron job (5am AEDT)
   ↓
2. Get all recipients with calls today
   ↓
3. For each recipient:
   - Calculate exact call time
   - Create RetellAI scheduled call
   - Store call_id in database
   ↓
4. RetellAI executes call at scheduled time
   ↓
5. Webhook received on completion
   ↓
6. Process transcript, extract health metrics
   ↓
7. Store in database, trigger notifications
```

### Dynamic Variables Passed to Agent

```json
{
  "recipient_name": "Margaret",
  "nickname": "Marge",
  "caller_name": "Sarah",
  "relationship": "daughter",
  "health_notes": "arthritis in hands, hearing aid in left ear",
  "interests": ["gardening", "grandchildren", "cooking"],
  "medications": ["blood pressure pill in morning"],
  "last_call_summary": "Was feeling good, mentioned grandchildren visiting soon",
  "special_message": ""
}
```

---

## 10. Design System

### Color Palette

**Primary:** Warm Teal `#0D9488`
- Trust, calm, healthcare-adjacent
- Good contrast for accessibility

**Secondary:** Soft Gold `#F59E0B`
- Warmth, care, optimism
- Call-to-action highlights

**Neutral:** Warm Grays
- Background: `#F9FAFB` / `#FEFCE8` (warm white)
- Text: `#374151` (soft black)
- Borders: `#E5E7EB`

**Semantic:**
- Success: `#10B981`
- Warning: `#F59E0B`
- Error: `#EF4444`
- Info: `#3B82F6`

### Typography

**Font Family:** Inter (clean, accessible, free)

**Scale:**
- Heading 1: 48px / 3rem
- Heading 2: 36px / 2.25rem
- Heading 3: 24px / 1.5rem
- Body: 18px / 1.125rem (slightly larger for accessibility)
- Small: 14px / 0.875rem

### Spacing

Base unit: 4px
- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px

### Components (shadcn/ui)

- Buttons (primary, secondary, outline, ghost)
- Cards
- Forms (input, select, checkbox, radio)
- Tables
- Modals
- Toasts
- Tabs
- Accordions

---

## 11. Accessibility Requirements

### WCAG 2.1 AA Compliance

**Visual:**
- Color contrast ratio ≥ 4.5:1 for text
- No color-only information
- Focus indicators visible
- Resizable text up to 200%

**Motor:**
- All interactive elements keyboard accessible
- Focus order logical
- No time-limited actions (or extendable)

**Cognitive:**
- Clear, simple language
- Consistent navigation
- Error messages helpful
- Form labels visible

### Elderly-Specific Considerations

- **Large touch targets** (min 44x44px)
- **High contrast mode** option
- **Font size toggle** in dashboard
- **Simple navigation** (max 2 levels deep)
- **No hover-only interactions**
- **Clear button labels** (not just icons)

---

## 12. Security & Privacy

### Data Protection

**Encryption:**
- TLS 1.3 for data in transit
- AES-256 for data at rest (Supabase)
- Encrypted backups

**Australian Data Residency:**
- Database in Sydney region
- Backups in Australian data centers
- No data transfer outside Australia without consent

### Privacy Compliance

**Privacy Act 1988:**
- Clear privacy policy
- Consent for data collection
- Right to access and delete data
- Breach notification procedures

**Call Recording Consent:**
- Explicit consent during signup
- Clear disclosure at call start
- Option to disable recording

### Security Measures

- Rate limiting on all endpoints
- CAPTCHA on signup/login
- Session timeout (24h max)
- Audit logging for admin actions
- Regular security scans (Dependabot)

---

## 13. Go-to-Market Features

### Lead Capture

- Exit-intent popup with value proposition
- Newsletter signup (educational content)
- Webinar/demo signups

### Social Proof

- Testimonial carousel
- Trust badges (security, Australian made)
- "X families trust Kindly Call" counter

### Referral Program

- Existing customers invite friends
- $20 credit for referrer, 1 month free for referee
- Track referral source

### Content Marketing

- Blog with elderly care tips
- Resource guides (PDF downloads)
- FAQ optimization for SEO

---

## 14. Implementation Phases

### Phase 1: MVP Foundation (Weeks 1-4)
**Goal:** Core signup and dashboard

**Deliverables:**
- [ ] Project setup (Next.js, Supabase, Vercel)
- [ ] Authentication (Clerk integration)
- [ ] Database schema and RLS policies
- [ ] Home page (hero, how it works, pricing preview)
- [ ] Signup flow (trial, no payment)
- [ ] Basic dashboard (call status, summary view)
- [ ] Stripe integration (plans, checkout)
- [ ] RetellAI webhook handlers

### Phase 2: Core Features (Weeks 5-8)
**Goal:** Full dashboard functionality

**Deliverables:**
- [ ] Call history page with transcripts
- [ ] Health insights dashboard
- [ ] Profile settings (call preferences, health notes)
- [ ] Family member invites
- [ ] Email notifications (call summaries, alerts)
- [ ] Emergency alert system
- [ ] Pricing page with Stripe integration
- [ ] About, FAQ, Contact pages

### Phase 3: Polish & Launch (Weeks 9-12)
**Goal:** Production-ready

**Deliverables:**
- [ ] Mobile responsive refinements
- [ ] Accessibility audit and fixes
- [ ] Performance optimization
- [ ] Error monitoring (Sentry)
- [ ] Analytics (PostHog)
- [ ] Admin dashboard (basic)
- [ ] Documentation
- [ ] Beta testing with 10-20 families

### Phase 4: Enhancement (Post-Launch)
**Goal:** Iterate based on feedback

**Planned Features:**
- [ ] Mobile app (React Native)
- [ ] Advanced health analytics
- [ ] Integration with wearables (optional)
- [ ] B2B features for aged care providers
- [ ] Multi-language support

---

## Appendices

### A. Competitor Reference URLs
- Telecross: https://www.redcross.org.au/services/telecross/
- CareCheckers: https://www.carecheckers.com/
- CHUFFTY: https://chufftyapp.com/
- CareCallingNow: https://carecallingnow.com/

### B. Technology Documentation
- Next.js: https://nextjs.org/docs
- Supabase: https://supabase.com/docs
- Clerk: https://clerk.com/docs
- Stripe: https://stripe.com/docs/au
- RetellAI: (internal docs)

### C. Australian Compliance References
- Privacy Act 1988: https://www.legislation.gov.au/Details/C2014C00076
- Aged Care Act 1997: https://www.legislation.gov.au/Details/C2020C00054
- Support at Home: https://www.health.gov.au/our-work/support-at-home

---

**Document Status:** Ready for User Approval

**Next Steps After Approval:**
1. Create project repository
2. Set up development environment
3. Begin Phase 1 implementation

---

*Created: 2025-12-25*
*Last Updated: 2025-12-25*
