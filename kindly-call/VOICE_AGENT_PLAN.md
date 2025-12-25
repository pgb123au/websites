# Kindly Call - Voice Agent Implementation Plan
## RetellAI Agent for Elderly Wellness Check-In Calls

**Version:** 1.0
**Date:** 2025-12-25
**Status:** PLANNING PHASE - Awaiting Approval

---

## Table of Contents

1. [Executive Overview](#1-executive-overview)
2. [Voice Configuration](#2-voice-configuration)
3. [Conversation Flow Design](#3-conversation-flow-design)
4. [Node Specifications](#4-node-specifications)
5. [Dynamic Variables](#5-dynamic-variables)
6. [Emergency Detection & Escalation](#6-emergency-detection--escalation)
7. [Health Question Framework](#7-health-question-framework)
8. [Voicemail Handling](#8-voicemail-handling)
9. [Tool Definitions (Webhooks)](#9-tool-definitions-webhooks)
10. [n8n Workflow Specifications](#10-n8n-workflow-specifications)
11. [Testing Strategy](#11-testing-strategy)
12. [Anti-Patterns to Avoid](#12-anti-patterns-to-avoid)
13. [Implementation Phases](#13-implementation-phases)

---

## 1. Executive Overview

### Purpose
Create an AI voice agent that provides warm, caring daily wellness check-in calls for elderly Australians, combining safety monitoring with meaningful companionship.

### Key Design Principles

1. **Warmth Over Efficiency**
   - Prioritize feeling cared for over call duration
   - Never rush the caller
   - Allow comfortable silences

2. **Respect & Dignity**
   - No "elderspeak" or patronizing tone
   - Treat as capable adults
   - Ask, don't tell

3. **Safety Without Surveillance**
   - Gentle health monitoring
   - Emergency detection
   - Family insights without invasion

4. **Consistency & Reliability**
   - Same voice every day
   - Same greeting structure
   - Predictable, comforting routine

5. **Australian Cultural Fit**
   - Australian accent
   - Local references
   - Understands Australian expressions

### Success Metrics

| Metric | Target |
|--------|--------|
| Average call duration | 5-8 minutes |
| Call completion rate | 95%+ |
| Elderly satisfaction (survey) | 4.5/5 stars |
| False emergency alerts | <2% |
| Voicemail detection accuracy | 98%+ |
| Health flag accuracy | 90%+ |

---

## 2. Voice Configuration

### Primary Voice Settings

Based on comprehensive research for elderly callers:

```json
{
  "voice_id": "11labs-Adrian",
  "voice_model": "eleven_turbo_v2_5",
  "fallback_voice_ids": ["openai-Nova"],
  "voice_stability": 1.5,
  "voice_speed": 0.85,
  "voice_volume": 1.2,
  "responsiveness": 0.7,
  "interruption_sensitivity": 0.3,
  "enable_backchannel": true,
  "backchannel_frequency": 0.5,
  "language": "en-AU",
  "end_call_after_silence_ms": 900000,
  "max_call_duration_ms": 1200000
}
```

### Settings Rationale

| Setting | Value | Why |
|---------|-------|-----|
| `voice_speed` | 0.85 | 15% slower - research shows 124 WPM optimal for elderly comprehension |
| `voice_stability` | 1.5 | Higher stability for consistent, predictable voice |
| `voice_volume` | 1.2 | 20% louder to compensate for hearing loss |
| `responsiveness` | 0.7 | Reduced to give elderly time to finish speaking |
| `interruption_sensitivity` | 0.3 | Low - elderly may pause mid-thought |
| `backchannel_frequency` | 0.5 | Moderate "mmhmm" reassurance |
| `end_call_after_silence_ms` | 900000 | 15 minutes - extended for processing time |
| `max_call_duration_ms` | 1200000 | 20 minutes max - allows for longer chats |

### Voice Selection Criteria

**Chosen: 11labs-Adrian**
- Male, middle-aged Australian voice
- Warm, clear articulation
- Professional but friendly
- Good for hearing-impaired (lower frequency)

**Alternative Female Voice:**
- Cartesia Emma - used in Personal Call agent
- Consider for user preference option

---

## 3. Conversation Flow Design

### High-Level Flow Diagram

```
                            ┌─────────────┐
                            │   START     │
                            └──────┬──────┘
                                   │
                            ┌──────▼──────┐
                            │  node-greeting │
                            │ "Hello, this is │
                            │ Kindly Call..." │
                            └──────┬──────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
       ┌──────▼──────┐      ┌──────▼──────┐     ┌──────▼──────┐
       │ VOICEMAIL   │      │ CONFIRMED   │     │ WRONG NUMBER │
       │ detected    │      │ live person │     │ / hang up    │
       └──────┬──────┘      └──────┬──────┘     └──────┬──────┘
              │                    │                    │
       ┌──────▼──────┐      ┌──────▼──────┐     ┌──────▼──────┐
       │node-voicemail│     │node-wellness │    │   node-end   │
       │ Leave message│     │ "How are you │    │              │
       └──────┬──────┘      │  feeling?"   │    └──────────────┘
              │             └──────┬──────┘
       ┌──────▼──────┐             │
       │node-send-sms│     ┌───────┴───────┐
       │ SMS fallback│     │               │
       └──────┬──────┘ ┌───▼───┐     ┌─────▼─────┐
              │        │CONCERN │     │  NORMAL   │
       ┌──────▼──────┐ │detected│     │ response  │
       │   node-end  │ └───┬───┘     └─────┬─────┘
       └─────────────┘     │               │
                    ┌──────▼──────┐  ┌─────▼─────┐
                    │node-followup│  │node-health │
                    │ Probe gently│  │ questions  │
                    └──────┬──────┘  └─────┬─────┘
                           │               │
                    ┌──────┴───────────────┘
                    │
             ┌──────▼──────┐
             │ EMERGENCY?  │
             └──────┬──────┘
                    │
         ┌──────────┴──────────┐
         │                     │
  ┌──────▼──────┐       ┌──────▼──────┐
  │node-emergency│      │node-social  │
  │ Escalate!   │       │ Light chat  │
  └──────┬──────┘       └──────┬──────┘
         │                     │
         │              ┌──────▼──────┐
         │              │node-medication│
         │              │ (if needed)   │
         │              └──────┬──────┘
         │                     │
         │              ┌──────▼──────┐
         │              │node-farewell│
         │              │ Warm goodbye│
         │              └──────┬──────┘
         │                     │
         └──────────────┬──────┘
                        │
                 ┌──────▼──────┐
                 │   node-end  │
                 │  END CALL   │
                 └─────────────┘
```

### Flow States

| State | Description | Typical Duration |
|-------|-------------|------------------|
| Greeting | Identify service, confirm recipient | 30-60 sec |
| Wellness Check | Main "how are you" question | 1-2 min |
| Health Questions | Optional deeper questions | 1-3 min |
| Social Chat | Companionship conversation | 2-5 min |
| Medication | Reminder if applicable | 30 sec |
| Farewell | Warm closing | 30 sec |
| **Total** | | **5-12 min** |

---

## 4. Node Specifications

### 4.1 node-greeting

**Purpose:** Identify service clearly, confirm we're speaking to the right person.

```json
{
  "id": "node-greeting",
  "type": "conversation",
  "block_interruptions": true,
  "instruction": {
    "type": "prompt",
    "text": "VERBATIM: \"Hello, this is your daily check-in call from Kindly Call.\"\n\nPause for 2 seconds.\n\nThen say: \"Is that {{nickname}}?\"\n\nWait patiently for response.\n\nIf they confirm (yes, speaking, that's me) - proceed to wellness check.\n\nIf they ask who's calling, say: \"I'm calling on behalf of your {{relationship}}, {{caller_name}}, who signed you up for daily wellness calls. Is now a good time for a quick chat?\"\n\nIf silence for 5+ seconds after initial greeting, gently say: \"Take your time, I'm here whenever you're ready.\"\n\nIMPORTANT: If you hear a clear voicemail message (\"leave a message after the beep\"), go to voicemail node."
  },
  "edges": [
    {
      "id": "edge-greeting-live",
      "destination_node_id": "node-wellness-check",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Person confirms identity OR acknowledges the call OR engages in conversation"
      }
    },
    {
      "id": "edge-greeting-voicemail",
      "destination_node_id": "node-voicemail",
      "transition_condition": {
        "type": "prompt",
        "prompt": "CLEAR voicemail detected - \"leave a message after the beep\" or answering machine greeting"
      }
    },
    {
      "id": "edge-greeting-wrong",
      "destination_node_id": "node-wrong-number",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Wrong number OR person says to never call again OR hostile response"
      }
    }
  ]
}
```

### 4.2 node-wellness-check

**Purpose:** Main wellness question - warm, open-ended.

```json
{
  "id": "node-wellness-check",
  "type": "conversation",
  "instruction": {
    "type": "prompt",
    "text": "Say warmly: \"{{nickname}}, how are you feeling today?\"\n\nListen carefully to their response.\n\nUSE GENTLE BACKCHANNELS:\n- \"I see\"\n- \"That's good to hear\"\n- \"Oh, I'm sorry to hear that\"\n\nAFTER THEY RESPOND:\n- If positive (good, fine, well) - respond warmly and transition to health questions\n- If concerning (tired, pain, lonely, sad) - show empathy and ask follow-up: \"I'm sorry to hear that. Would you like to tell me more about what's going on?\"\n- If emergency keywords detected - IMMEDIATELY go to emergency node\n\nEMERGENCY KEYWORDS:\n- fallen, fell, hurt badly\n- can't breathe, chest pain, heart\n- help me, emergency, need help\n- bleeding, can't move\n\nNEVER RUSH. Take time to listen fully before responding."
  },
  "edges": [
    {
      "id": "edge-wellness-emergency",
      "destination_node_id": "node-emergency",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Emergency keywords detected: fallen, fell, hurt, can't breathe, chest pain, help me, emergency, bleeding, can't move"
      }
    },
    {
      "id": "edge-wellness-concern",
      "destination_node_id": "node-concern-followup",
      "transition_condition": {
        "type": "prompt",
        "prompt": "User expresses concerning symptoms: ongoing pain, unable to do activities, very tired, feeling unwell, sad or depressed, lonely - BUT not emergency level"
      }
    },
    {
      "id": "edge-wellness-normal",
      "destination_node_id": "node-health-questions",
      "transition_condition": {
        "type": "prompt",
        "prompt": "User responds positively or neutrally (good, fine, okay, not bad, same as usual)"
      }
    }
  ]
}
```

### 4.3 node-health-questions

**Purpose:** Gentle health monitoring through conversational questions.

```json
{
  "id": "node-health-questions",
  "type": "conversation",
  "instruction": {
    "type": "prompt",
    "text": "Ask 2-3 gentle health questions in a CONVERSATIONAL way (not like a checklist).\n\nQUESTIONS TO CHOOSE FROM (pick based on context):\n\n1. SLEEP: \"Did you sleep well last night?\"\n2. APPETITE: \"Have you had breakfast yet?\" or \"How's your appetite been?\"\n3. ACTIVITY: \"Have you been able to get out at all today?\" or \"Any plans for today?\"\n4. PAIN: Only if previously mentioned - \"How's that [knee/back/arthritis] going?\"\n5. MOOD: If seeming down - \"How are you feeling in yourself lately?\"\n\nRESPONSE GUIDELINES:\n- Positive response: \"That's wonderful to hear!\"\n- Neutral: \"That's understandable.\"\n- Negative: \"I'm sorry to hear that. Have you mentioned that to anyone?\"\n\nDO NOT:\n- Ask more than 3 questions in a row\n- Sound like you're reading a checklist\n- Ask about medical details (blood pressure, medications doses)\n\nAFTER 2-3 QUESTIONS:\nTransition naturally: \"It's lovely chatting with you, {{nickname}}.\"\n\n{{#if interests}}\nYou might want to ask about: {{interests}}\n{{/if}}"
  },
  "edges": [
    {
      "id": "edge-health-emergency",
      "destination_node_id": "node-emergency",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Emergency symptoms revealed: severe pain, fall, can't get up, breathing difficulty"
      }
    },
    {
      "id": "edge-health-social",
      "destination_node_id": "node-social-chat",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Health questions complete, user engaging in conversation"
      }
    }
  ]
}
```

### 4.4 node-social-chat

**Purpose:** Companionship - the heart of the service.

```json
{
  "id": "node-social-chat",
  "type": "conversation",
  "instruction": {
    "type": "prompt",
    "text": "Have a warm, natural conversation with {{nickname}}.\n\nTOPICS TO EXPLORE:\n{{#if interests}}\n- Their interests: {{interests}}\n{{/if}}\n- \"Have you spoken to any family or friends lately?\"\n- \"What have you been watching on TV?\"\n- \"How's the weather been there?\"\n- \"Got anything nice planned for the week?\"\n\nCONVERSATION STYLE:\n- Be genuinely interested\n- Share brief relevant comments (\"Oh, I love gardening too!\")\n- Ask follow-up questions\n- Use their name occasionally\n- Allow natural pauses\n\nDURATION:\n- Aim for 3-5 minutes of chat\n- Let the conversation flow naturally\n- If user seems to want to end, gracefully transition to farewell\n\n{{#if last_call_summary}}\nREFERENCE PREVIOUS CALL:\n\"Last time we spoke, you mentioned {{last_call_summary}}. How did that go?\"\n{{/if}}\n\n{{#if special_message}}\nSPECIAL MESSAGE FROM FAMILY:\n\"Oh, before I forget - {{caller_name}} wanted me to tell you: {{special_message}}\"\n{{/if}}\n\nTRANSITION TO END:\n- \"Well, it's been lovely chatting with you, {{nickname}}.\"\n- \"I should let you get on with your day.\""
  },
  "edges": [
    {
      "id": "edge-social-medication",
      "destination_node_id": "node-medication-reminder",
      "transition_condition": {
        "type": "equation",
        "equations": [
          {"left": "{{has_medications}}", "operator": "==", "right": "true"}
        ],
        "operator": "&&"
      }
    },
    {
      "id": "edge-social-farewell",
      "destination_node_id": "node-farewell",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Conversation winding down naturally OR user indicates wanting to end call"
      }
    }
  ]
}
```

### 4.5 node-medication-reminder

**Purpose:** Gentle medication reminder (only if configured).

```json
{
  "id": "node-medication-reminder",
  "type": "conversation",
  "instruction": {
    "type": "prompt",
    "text": "ONLY if medications are configured for this call time:\n\n\"Just a friendly reminder - have you taken your {{medications}} today?\"\n\nRESPONSES:\n- If yes: \"Wonderful, good on you for staying on top of it.\"\n- If no: \"No worries, perhaps you could take it after we chat?\"\n- If unsure: \"That's alright. Maybe check with {{caller_name}} if you're not sure.\"\n\nNEVER:\n- Be pushy or lecturing\n- Ask about dosages\n- Give medical advice\n\nThis is a gentle REMINDER, not medical supervision."
  },
  "edges": [
    {
      "id": "edge-medication-farewell",
      "destination_node_id": "node-farewell",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Medication reminder delivered, user responded"
      }
    }
  ]
}
```

### 4.6 node-farewell

**Purpose:** Warm, caring goodbye.

```json
{
  "id": "node-farewell",
  "type": "conversation",
  "instruction": {
    "type": "prompt",
    "text": "End the call warmly:\n\nVERBATIM: \"It's been lovely talking with you, {{nickname}}. I'll call again tomorrow at the same time. Take care of yourself!\"\n\nIf they say goodbye back, respond: \"Goodbye, {{nickname}}! Have a wonderful day.\"\n\nIMPORTANT:\n- Wait for them to acknowledge\n- Don't hang up abruptly\n- If they want to keep chatting, let them - then try again to wrap up gently"
  },
  "skip_response_edge": {
    "id": "edge-farewell-end",
    "destination_node_id": "node-call-complete",
    "transition_condition": {
      "type": "prompt",
      "prompt": "Skip to call completion"
    }
  }
}
```

### 4.7 node-emergency

**Purpose:** Handle detected emergencies with care.

```json
{
  "id": "node-emergency",
  "type": "conversation",
  "instruction": {
    "type": "prompt",
    "text": "EMERGENCY DETECTED - Stay calm, be reassuring.\n\nSay: \"{{nickname}}, it sounds like you might need some help. I want to make sure you're okay.\"\n\nASSESS THE SITUATION:\n\"Can you tell me what's happening?\"\n\nIF IMMEDIATE DANGER (fallen, chest pain, bleeding):\n\"I'm going to stay on the line with you. I'm alerting {{caller_name}} right now.\"\n\"Do you need me to help you call 000 for an ambulance?\"\n\nIF LESS URGENT BUT CONCERNING:\n\"I'm going to let {{caller_name}} know so they can check on you. Is that okay?\"\n\nSTAY CALM:\n- Speak slowly and clearly\n- Reassure them help is coming\n- Don't panic or sound alarmed\n- Keep them talking if possible\n\nACTIONS:\n- Trigger emergency webhook IMMEDIATELY\n- Stay on line until acknowledgment\n- If user unable to respond, still trigger alert"
  },
  "edges": [
    {
      "id": "edge-emergency-end",
      "destination_node_id": "node-emergency-complete",
      "transition_condition": {
        "type": "prompt",
        "prompt": "Emergency acknowledged, user stable, or call ending"
      }
    }
  ]
}
```

### 4.8 node-voicemail

**Purpose:** Leave a caring voicemail message.

```json
{
  "id": "node-voicemail",
  "type": "conversation",
  "instruction": {
    "type": "prompt",
    "text": "Leave a voicemail message:\n\nVERBATIM: \"Hello {{nickname}}, this is your daily check-in call from Kindly Call, on behalf of {{caller_name}}. I'm sorry I missed you today. I hope you're doing well! I'll try calling again later. If you need anything, your family is just a phone call away. Take care!\"\n\nAFTER MESSAGE:\n- End call\n- Trigger SMS notification\n- Schedule retry call"
  },
  "skip_response_edge": {
    "id": "edge-voicemail-sms",
    "destination_node_id": "node-send-sms",
    "transition_condition": {
      "type": "prompt",
      "prompt": "Skip to send SMS"
    }
  }
}
```

### 4.9 node-call-complete

**Purpose:** Silent webhook to log call completion.

```json
{
  "id": "node-call-complete",
  "type": "function",
  "tool_id": "tool-call-complete",
  "speak_during_execution": false,
  "wait_for_result": false,
  "parameters": {
    "recipient_id": "{{recipient_id}}",
    "call_status": "completed",
    "call_duration": "{{call_duration}}",
    "health_flags": "{{detected_health_flags}}",
    "mood_assessment": "{{mood_assessment}}"
  },
  "edges": [
    {
      "id": "edge-complete-end",
      "destination_node_id": "node-end",
      "transition_condition": {
        "type": "equation",
        "equations": [{"left": "1", "operator": "==", "right": "1"}],
        "operator": "&&"
      }
    }
  ]
}
```

---

## 5. Dynamic Variables

### Required Variables (Passed Every Call)

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `recipient_id` | UUID | Database ID for recipient | `abc-123-def` |
| `nickname` | String | What to call them | `"Margaret"` or `"Marge"` |
| `caller_name` | String | Family member who signed up | `"Sarah"` |
| `relationship` | String | Relationship to caller | `"daughter"` |
| `to_phone` | String | Recipient phone for SMS | `"+61412345678"` |
| `call_time` | String | Scheduled time | `"9:00 AM"` |

### Optional Variables

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `health_notes` | String | Known conditions | `"arthritis, hearing aid left ear"` |
| `interests` | Array | Hobbies to discuss | `["gardening", "grandchildren"]` |
| `medications` | String | Medication reminders | `"blood pressure pill"` |
| `has_medications` | Boolean | Whether to do med reminder | `true` |
| `last_call_summary` | String | Previous call notes | `"Mentioned garden project"` |
| `special_message` | String | Family message to deliver | `"Happy birthday!"` |

### System Variables (Auto-populated)

| Variable | Description |
|----------|-------------|
| `call_duration` | Duration in seconds |
| `detected_health_flags` | AI-extracted concerns |
| `mood_assessment` | AI sentiment analysis |

---

## 6. Emergency Detection & Escalation

### Trigger Keywords (Immediate Alert)

**Level 1 - CRITICAL (Immediate 000 suggestion):**
- "I've fallen" / "I fell"
- "can't breathe" / "breathing" + difficulty
- "chest pain" / "heart"
- "I'm bleeding"
- "help me" / "need help"
- "emergency"

**Level 2 - URGENT (Alert family immediately):**
- "I'm hurt"
- "I'm in pain" (severe)
- "I can't get up"
- "I'm dizzy"
- "I'm confused"

**Level 3 - CONCERNING (Flag for family):**
- "I haven't eaten" (multiple days)
- "I haven't slept"
- "I'm feeling very lonely"
- "I don't want to" (repeatedly)
- Unusual confusion or disorientation

### Escalation Protocol

```
CRITICAL DETECTED
    │
    ├─► AI stays on line
    ├─► Trigger emergency webhook (immediate)
    ├─► Webhook sends SMS to all emergency contacts
    ├─► Offer to help call 000
    └─► Log in dashboard as CRITICAL alert

URGENT DETECTED
    │
    ├─► AI expresses concern
    ├─► Trigger alert webhook
    ├─► SMS to primary contact only
    └─► Log in dashboard as URGENT alert

CONCERNING DETECTED
    │
    ├─► AI notes in conversation
    ├─► Include in call summary
    └─► Flag in health dashboard
```

### Emergency Webhook Payload

```json
{
  "recipient_id": "abc-123",
  "recipient_name": "Margaret Smith",
  "recipient_phone": "+61412345678",
  "alert_type": "critical",
  "alert_message": "Recipient said: 'I've fallen and I can't get up'",
  "detected_keywords": ["fallen", "can't get up"],
  "call_id": "call_xyz",
  "timestamp": "2025-12-25T09:15:30+11:00",
  "emergency_contacts": [
    {"name": "Sarah", "phone": "+61498765432", "relationship": "daughter"},
    {"name": "John", "phone": "+61487654321", "relationship": "son"}
  ]
}
```

---

## 7. Health Question Framework

### Daily Health Signals to Track

| Signal | Questions | Tracking |
|--------|-----------|----------|
| **Sleep** | "Did you sleep well?" | 1-5 scale |
| **Mood** | "How are you feeling in yourself?" | positive/neutral/negative |
| **Appetite** | "Have you eaten today?" | yes/no/partial |
| **Pain** | "Any aches or pains?" | 0-10 scale, location |
| **Activity** | "Have you been up and about?" | active/limited/bedbound |
| **Social** | "Spoken to anyone?" | yes/no, who |
| **Medication** | "Taken your medication?" | yes/no/unsure |

### Question Rotation Strategy

**Don't ask all questions every day.** Rotate to keep conversations natural:

| Day | Focus Questions |
|-----|-----------------|
| Mon | Sleep, Mood, Activity |
| Tue | Appetite, Social |
| Wed | Sleep, Pain (if relevant), Mood |
| Thu | Activity, Social |
| Fri | Mood, Weekend plans |
| Sat | Sleep, Relaxed chat |
| Sun | General wellness, Family contact |

### Non-Intrusive Question Phrasing

**Instead of:** "Rate your pain on a scale of 1-10"
**Say:** "How's that knee been treating you?"

**Instead of:** "Did you take your blood pressure medication?"
**Say:** "Have you had a chance to take your pills this morning?"

**Instead of:** "Have you experienced any falls?"
**Say:** "Have you been feeling steady on your feet?"

---

## 8. Voicemail Handling

### Detection Patterns

**Clear Voicemail Indicators:**
- "Leave a message after the beep"
- "You've reached the voicemail of..."
- "The person you are calling is not available"
- "Please leave your message after the tone"
- Extended silence after ringing (> 15 seconds)

### Voicemail Script

```
"Hello {{nickname}}, this is your daily check-in call from Kindly Call,
on behalf of {{caller_name}}. I'm sorry I missed you today!
I hope you're doing well. I'll try again [in a few hours/tomorrow].
Take care of yourself!"
```

### Post-Voicemail Actions

1. **Send SMS** (immediately):
   ```
   "Hi {{nickname}}, we tried calling for your daily check-in
   but missed you. Hope you're well! We'll try again soon.
   - Kindly Call (on behalf of {{caller_name}})"
   ```

2. **Schedule Retry** (in 2 hours)

3. **After 3 Attempts:**
   - Mark as "missed_call" in database
   - Alert family member
   - Don't try again until next scheduled day

### Voicemail vs Ambiguous Detection

From Personal Call Agent learnings:

**Go to voicemail ONLY if:**
- Explicit "leave a message" detected
- Answering machine tone heard

**Proceed with live message if:**
- Silence after hello (might be elderly processing)
- Unclear response
- Background noise without clear voicemail prompt

---

## 9. Tool Definitions (Webhooks)

### tool-call-complete

```json
{
  "name": "complete_call",
  "type": "custom",
  "url": "https://auto.yr.com.au/webhook/kindlycall/call-complete",
  "description": "Log call completion with summary and health data",
  "method": "POST",
  "parameters": {
    "type": "object",
    "properties": {
      "recipient_id": {"type": "string"},
      "call_status": {"type": "string"},
      "call_duration": {"type": "string"},
      "health_flags": {"type": "string"},
      "mood_assessment": {"type": "string"}
    },
    "required": ["recipient_id", "call_status"]
  },
  "timeout_ms": 15000,
  "tool_id": "tool-call-complete"
}
```

### tool-emergency-alert

```json
{
  "name": "emergency_alert",
  "type": "custom",
  "url": "https://auto.yr.com.au/webhook/kindlycall/emergency",
  "description": "Trigger emergency alert to family members",
  "method": "POST",
  "parameters": {
    "type": "object",
    "properties": {
      "recipient_id": {"type": "string"},
      "alert_type": {"type": "string", "enum": ["critical", "urgent", "concerning"]},
      "alert_message": {"type": "string"},
      "detected_keywords": {"type": "string"}
    },
    "required": ["recipient_id", "alert_type", "alert_message"]
  },
  "timeout_ms": 5000,
  "tool_id": "tool-emergency-alert"
}
```

### tool-send-sms

```json
{
  "name": "send_sms",
  "type": "custom",
  "url": "https://auto.yr.com.au/webhook/kindlycall/send-sms",
  "description": "Send SMS to recipient phone",
  "method": "POST",
  "parameters": {
    "type": "object",
    "properties": {
      "phone": {"type": "string"},
      "message": {"type": "string"}
    },
    "required": ["phone", "message"]
  },
  "timeout_ms": 15000,
  "tool_id": "tool-send-sms"
}
```

---

## 10. n8n Workflow Specifications

### 10.1 kindlycall_schedule_calls.json

**Purpose:** Daily job to create scheduled calls

**Trigger:** Cron - 5:00 AM AEDT daily

**Flow:**
```
1. Query database: All active recipients
2. For each recipient:
   - Calculate scheduled time (recipient timezone)
   - Get dynamic variables from profile
   - Create RetellAI scheduled call
   - Store call_id in database
3. Log summary
```

**Database Query:**
```sql
SELECT
  r.id,
  r.name,
  r.nickname,
  r.phone,
  r.timezone,
  r.call_time,
  r.health_notes,
  r.interests,
  u.name as caller_name,
  ra.role
FROM recipients r
JOIN recipient_access ra ON r.id = ra.recipient_id
JOIN users u ON ra.user_id = u.id
WHERE r.status = 'active'
AND ra.role = 'owner'
AND EXTRACT(DOW FROM NOW() AT TIME ZONE r.timezone) = ANY(
  SELECT CASE
    WHEN day = 'sun' THEN 0
    WHEN day = 'mon' THEN 1
    -- etc
  END FROM unnest(r.call_days) as day
);
```

### 10.2 kindlycall_call_complete.json

**Purpose:** Process completed calls

**Trigger:** Webhook - `/kindlycall/call-complete`

**Flow:**
```
1. Receive call data from RetellAI
2. Extract transcript
3. AI process transcript:
   - Generate summary
   - Detect health flags
   - Calculate mood score
4. Store in database:
   - Update calls table
   - Insert health_metrics
5. Send notifications:
   - Email summary to family (if configured)
   - Dashboard real-time update
6. Return success
```

**AI Processing Prompt:**
```
Analyze this elderly wellness check-in call transcript.

Extract:
1. Overall mood (positive/neutral/negative)
2. Sleep quality mentioned (1-5 or null)
3. Appetite mentioned (good/poor/normal or null)
4. Pain reported (0-10 scale, location, or null)
5. Activity level (active/limited/bedbound or null)
6. Social interaction (who they mentioned seeing/talking to)
7. Any concerning statements (list)
8. Key topics discussed (list)
9. One-paragraph summary for family

Respond in JSON format.
```

### 10.3 kindlycall_emergency.json

**Purpose:** Handle emergency alerts

**Trigger:** Webhook - `/kindlycall/emergency`

**Flow:**
```
1. Receive emergency alert
2. Get all emergency contacts for recipient
3. For each contact (parallel):
   - Send SMS with alert
   - Send email with details
4. Log alert in database
5. Push notification to dashboard
6. Return success immediately (before logging)
```

**SMS Template:**
```
URGENT - Kindly Call Alert

{{recipient_name}} may need help.

During their daily call, they said: "{{alert_message}}"

Please check on them or call 000 if needed.

- Kindly Call
```

### 10.4 kindlycall_daily_report.json

**Purpose:** Generate daily summary for families

**Trigger:** Cron - 6:00 PM AEDT daily

**Flow:**
```
1. Query all calls completed today
2. Group by recipient
3. For each recipient:
   - Get owner user email
   - Compile day's data:
     - Call summary
     - Health metrics
     - Any alerts
   - Generate email
   - Send via Resend
4. Log completion
```

**Email Template:**
```
Subject: Daily Update for {{recipient_name}} - {{date}}

Hi {{caller_name}},

Here's today's check-in summary for {{recipient_name}}:

📞 CALL SUMMARY
{{call_summary}}

💚 WELLNESS
- Mood: {{mood}}
- Sleep: {{sleep}}
- Appetite: {{appetite}}

{{#if alerts}}
⚠️ ALERTS
{{alerts}}
{{/if}}

{{#if trends}}
📊 7-DAY TRENDS
{{trends}}
{{/if}}

View full details in your dashboard: {{dashboard_link}}

---
Kindly Call
Daily check-ins with care
```

---

## 11. Testing Strategy

### 11.1 Unit Testing (Agent JSON)

Before deployment, validate:

```bash
cd /c/Users/peter/Downloads/CC/retell/scripts
python retell_agent_validator.py ../agents/KindlyCall_Wellness_v1.0.json --fix
```

Checks:
- [ ] All nodes have valid types
- [ ] All edges have `destination_node_id` (not `target`)
- [ ] All transitions have valid conditions
- [ ] All tool_ids match defined tools
- [ ] No orphan nodes
- [ ] Start node exists

### 11.2 Simulation Testing

Create test scenarios:

| Scenario | Expected Outcome |
|----------|------------------|
| Normal positive call | Complete all nodes, log wellness data |
| User mentions pain | Concern followup, flag in summary |
| Emergency keywords | Emergency node, alert webhook fired |
| Voicemail detected | Voicemail message, SMS sent |
| No answer (silence) | Retry logic triggered |
| Confused elderly | Hearing difficulty handling |
| User wants to chat long | Extended social chat |
| User wants to end early | Graceful farewell |

### 11.3 Live Testing

**Test Recipient:** Peter Ball (0412111000)

**Test Scenarios:**
1. Schedule test call
2. Answer as normal - verify full flow
3. Simulate confusion - verify handling
4. Say emergency keyword - verify alert
5. Don't answer - verify voicemail + SMS
6. Long chat - verify natural ending

### 11.4 Metrics to Monitor

| Metric | Target | Alert If |
|--------|--------|----------|
| Call completion rate | >95% | <90% |
| Average duration | 5-8 min | <3 min or >15 min |
| Emergency false positive | <2% | >5% |
| User hang up rate | <10% | >15% |
| Voicemail detection accuracy | >98% | <95% |

---

## 12. Anti-Patterns to Avoid

### From Christmas Call Project Learnings

| Anti-Pattern | Why Bad | Correct Approach |
|--------------|---------|------------------|
| Using `target` in edges | Invalid, API rejects | Use `destination_node_id` |
| Using `agent_id` in API | Uses wrong agent | Use `override_agent_id` |
| Filler words ("um", "so") | Sounds robotic | Add "NO filler words" to prompt |
| Early goodbye on voicemail | Message not delivered | ALWAYS deliver message first |
| `speak_during_execution: "false"` | Type error | Use boolean: `false` |
| Rephrasing script | Inconsistent | Use "VERBATIM:" prefix |

### Elderly-Specific Anti-Patterns

| Anti-Pattern | Why Bad | Correct Approach |
|--------------|---------|------------------|
| Speaking too fast | Can't understand | Set `voice_speed: 0.85` |
| Interrupting | Feels rude | Set `interruption_sensitivity: 0.3` |
| "Are you still there?" | Sounds accusatory | "Take your time, I'm here" |
| Rapid-fire questions | Overwhelming | 1 question, wait, respond |
| Elderspeak ("sweetie") | Patronizing | Use their actual name |
| Too quiet | Can't hear | Set `voice_volume: 1.2` |
| Complex sentences | Confusing | Short, simple sentences |

---

## 13. Implementation Phases

### Phase 1: Core Agent (Week 1-2)

**Deliverables:**
- [ ] Agent JSON with all nodes
- [ ] Tool definitions
- [ ] Basic n8n workflows:
  - [ ] call-complete
  - [ ] send-sms
- [ ] Manual testing with Peter Ball

### Phase 2: Emergency System (Week 3)

**Deliverables:**
- [ ] Emergency detection refinement
- [ ] Emergency webhook
- [ ] SMS alert system
- [ ] Dashboard alert integration
- [ ] Test all emergency scenarios

### Phase 3: Scheduling & Automation (Week 4)

**Deliverables:**
- [ ] Schedule workflow (cron)
- [ ] Retry logic for missed calls
- [ ] Daily report workflow
- [ ] Health metrics extraction
- [ ] Integration with website dashboard

### Phase 4: Polish & Beta (Week 5-6)

**Deliverables:**
- [ ] Voice tuning based on feedback
- [ ] Prompt optimization
- [ ] 10-20 beta family testing
- [ ] Iterate based on feedback
- [ ] Performance monitoring

---

## Appendices

### A. Global Prompt Template

```
You are a caring Australian AI companion calling {{nickname}} for their daily wellness check-in.

CORE PERSONALITY:
- Warm, patient, friendly
- Australian accent and expressions
- Never rushed or impatient
- Genuinely interested in their wellbeing

SPEAKING STYLE:
- Speed: 15% slower than normal
- Volume: Slightly louder than normal
- Clarity: Clear enunciation
- Pauses: 1-2 seconds between sentences

RULES:
1. NO filler words (um, uh, so, like)
2. Say VERBATIM phrases exactly as written
3. Wait for responses - never interrupt
4. Use their name naturally but not excessively
5. Show empathy with responses like "I'm sorry to hear that"
6. If they seem confused, simplify and speak clearer
7. NEVER give medical advice
8. ALWAYS stay calm, even in emergencies

SAFETY:
- If emergency keywords detected, transition immediately
- Stay on line if someone needs help
- Alert family if any concerns

You represent Kindly Call, providing daily check-ins for elderly Australians on behalf of their families.
```

### B. Voice Test Checklist

Before deploying, verify with test calls:

- [ ] Voice sounds warm, not robotic
- [ ] Speed is noticeably slower
- [ ] Volume is adequate but not loud
- [ ] Australian accent is clear
- [ ] Pauses feel natural
- [ ] Backchannels ("mmhmm") feel appropriate
- [ ] No awkward silences
- [ ] Transitions between nodes are smooth
- [ ] Emergency handling sounds calm

### C. n8n Golden Rules (From CLAUDE.md)

| Rule | Implementation |
|------|----------------|
| Database | Use `retellai_prod` |
| PostgreSQL nodes | `alwaysOutputData: true` |
| Write queries | `RETURNING *;` |
| Response order | Response node BEFORE logging |
| JSONB columns | Already parsed - never `JSON.parse()` |

---

**Document Status:** Ready for User Approval

**Next Steps After Approval:**
1. Create agent JSON file
2. Set up n8n webhooks
3. Manual dashboard deployment
4. Begin testing

---

*Created: 2025-12-25*
*Last Updated: 2025-12-25*
