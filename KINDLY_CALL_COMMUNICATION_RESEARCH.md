# Kindly Call - Communication Best Practices Research
## AI Voice Calling Service for Elderly & Disabled Australians

**Last Updated:** 2025-12-25
**Purpose:** Daily wellness check-ins via AI voice calls for vulnerable populations
**Target Audience:** Elderly and disabled people living independently in Australia

---

## Table of Contents

1. [Speaking to Elderly People](#1-speaking-to-elderly-people)
2. [Health Check Questions](#2-health-check-questions)
3. [Building Rapport in Automated Calls](#3-building-rapport-in-automated-calls)
4. [Cultural Considerations (Australian)](#4-cultural-considerations-australian)
5. [Disability Considerations](#5-disability-considerations)
6. [Emergency Communication](#6-emergency-communication)
7. [Companion Call Patterns](#7-companion-call-patterns)
8. [Family Communication](#8-family-communication)
9. [Implementation Recommendations for Kindly Call](#9-implementation-recommendations-for-kindly-call)
10. [RetellAI Configuration Guidelines](#10-retellai-configuration-guidelines)
11. [Legal & Ethical Considerations](#11-legal--ethical-considerations)

---

## 1. SPEAKING TO ELDERLY PEOPLE

### Optimal Speaking Pace

**CRITICAL: Slow down to 124 words per minute**

- Natural speech runs at 140-180 words per minute, which is TOO FAST for elderly listeners
- **Research shows 124 WPM is optimal for elderly comprehension**
- While this may feel "much too slow" to the speaker, this is the rate at which older adults understand best
- When this slower rate is used, older adults are "amazed at how well they can understand what is being said"

**Why Speed Matters:**
- Processing speech requires complex acoustic, neurologic, and linguistic events completed within milliseconds
- Older adults have reduced processing speed and slower encoding (NOT reduced intelligence)
- When listening to time-compressed speech, older adults recall significantly less than younger adults
- The negative effects are DRAMATICALLY greater when content is complex
- Grammatical complexity + fast speech don't just add together - they MULTIPLY the difficulty

**Implementation for Kindly Call:**
```
Target: 124 WPM
Maximum: 130 WPM
Use shorter sentences
Insert pauses between sentences and at clause boundaries
```

### Clarity and Enunciation

**Best Practices:**
- Speak clearly, slowly, distinctly, but NATURALLY
- DO NOT shout - it distorts sound and makes lip-reading harder (for video calls)
- DO NOT exaggerate mouth movements or use unnatural intonation
- DO NOT speak too softly - volume must be adequate
- Avoid speaking too fast OR too slowly (extreme slowness distorts certain sounds)
- **Practice deliberate articulation** - benefit patients with hearing loss

**What to Avoid:**
- Rapid, run-on sentences without breaks
- Mumbling or unclear pronunciation
- Background noise during calls
- Speaking while doing other tasks (leads to unclear speech)

### Patience and Wait Times

**CRITICAL: Insert pauses for processing**

Research shows that inserting pauses at the ends of clauses and sentences helps restore memory performance close to normal rates, even for time-compressed speech.

**Recommended Pause Strategy:**
- 1-2 seconds after each sentence
- 0.5-1 second at clause boundaries
- 3-5 seconds after asking a question (wait for response)
- If no response, repeat question with slight rephrasing

**Why Pauses Matter:**
- Gives time for patients (especially those with hearing impairment) to comprehend content and concepts
- Allows processing time for response formulation
- Reduces cognitive overload
- Shows respect and patience

### Handling Hearing Impairments

**Statistics:**
- About 1 in 3 older adults have hearing loss
- Chance of hearing loss increases with age
- Hearing-impaired people suffer communication problems if speakers fail to articulate slowly or deliberately

**Communication Strategies:**
- Face the person directly at eye level (for video calls)
- Minimize extraneous background noise
- Use clear, deliberate enunciation
- Be prepared to repeat information
- Offer alternative communication methods if needed (follow-up SMS)

**For Telephone Calls Specifically:**
- Telephone communication lacks visual cues
- Voice quality is paramount
- Background silence is essential
- Speak slightly louder than normal conversation (but don't shout)
- Use clear phone connection (high-quality VoIP)

### Avoiding "Elderspeak"

**What is Elderspeak?**
Patronizing speech patterns that include:
- Exaggerated intonation (baby talk)
- Unnaturally simple words or grammar
- Terms of endearment to strangers ("sweetie," "dear")
- Overly simplified explanations

**Why to Avoid It:**
- Perceived by older adults as patronizing and disrespectful
- The comprehension problem in healthy aging is reduced processing speed, NOT intelligence
- Elderspeak damages dignity and autonomy
- Can lead to resistance and disengagement

**Instead, Use:**
- Respectful, formal language when appropriate
- Ask how they prefer to be addressed
- Use their name naturally
- Maintain adult-to-adult tone
- Slower pace WITHOUT simplified content

### Repetition Without Condescension

**Strategies:**
- Frame repetition as clarification: "Let me make sure I've explained that clearly..."
- Use slight rephrasing rather than exact repetition
- Acknowledge the need positively: "That's an important question, let me go over that again"
- Never say "I already told you that" or show impatience
- Use phrases like:
  - "Just to confirm..."
  - "Let me recap what we discussed..."
  - "To make sure we're on the same page..."

---

## 2. HEALTH CHECK QUESTIONS

### Non-Intrusive Wellness Questions

**Philosophy: Conversation, Not Interrogation**

The goal is to build a natural conversation that reveals wellbeing without feeling clinical or invasive.

**Good Question Examples:**

**Opening (Warm):**
- "Good morning [Name]! How are you feeling today?"
- "How did you sleep last night?"
- "What have you been up to this morning?"

**Physical Wellbeing (Gentle):**
- "Have you had breakfast yet?" (checks if they're able to prepare food)
- "Did you sleep well?" (sleep quality indicator)
- "How's your energy today - feeling up to your usual activities?"
- "Have you been able to get outside at all this week?"

**Daily Activities (Non-Medical):**
- "Have you had a chance to [hobby/interest] lately?"
- "Did you manage to do your shopping this week?"
- "Have you spoken to anyone today?" (social connection)

**Indirect Health Screening:**
- "Is there anything you need help with today?"
- "Have you taken your medications this morning?" (if applicable)
- "How's your appetite been?"

**DO NOT ASK:**
- Direct medical questions ("What's your blood pressure?")
- Questions that sound like a checklist
- Multiple rapid-fire questions
- Overly personal health details

### Question Flows from Healthcare Providers

**Medicare Annual Wellness Visit Model:**

Uses a "Health Risk Assessment" questionnaire that covers:
1. Physical health interfering with daily activities
2. Emotional health concerns
3. Falls or balance issues
4. Pain levels
5. Social connections

**Adapted for Daily Calls:**

Instead of formal assessment, work these into natural conversation:
- "Have you felt steady on your feet today?" (fall risk)
- "How's your mood been?" (mental health)
- "Have you had any visitors or phone calls this week?" (social isolation)

### Activities of Daily Living (ADL) - Conversational Approach

**Standard ADL Categories:**
- Eating
- Dressing
- Bathing
- Transferring (bed to chair)
- Toileting
- Bladder/bowel control

**How to Ask (Non-Clinical):**
- "Did you have any trouble getting dressed this morning?"
- "Have you been able to get up and move around okay today?"
- "Did you manage to have a shower/bath recently?"

**Instrumental ADL (IADL):**
- Housework
- Meal preparation
- Medications
- Finances
- Telephone use

**How to Ask:**
- "Have you been able to keep up with your housework?"
- "Did you cook anything nice this week?"
- "Are you keeping track of your bills okay?"

### Building Trust Through Conversation

**Progression Over Time:**

**Week 1:** Stick to light, easy questions
- How they're feeling
- Weather chat
- Simple daily activities

**Week 2-4:** Gradually deepen
- Introduce questions about sleep, appetite
- Ask about hobbies and interests
- Build rapport through consistency

**Month 2+:** More health-focused (if trust established)
- Can ask about specific health concerns
- Medication adherence
- Pain or discomfort

**Key Principle:** Let the senior guide the depth. If they volunteer information, follow up. If they're reticent, don't push.

### Two-Question Depression Screening

**Validated Approach (as effective as longer scales):**

1. "During the past month, have you been bothered by feelings of sadness, depression, or hopelessness?"
2. "Have you often been bothered by a lack of interest or pleasure in doing things?"

**Implementation Notes:**
- Only ask if appropriate relationship established
- Frame as "checking in on how you're feeling overall"
- Be prepared to escalate if positive responses
- Have resources ready for referral

---

## 3. BUILDING RAPPORT IN AUTOMATED CALLS

### Making AI Calls Feel Personal

**The Challenge:**
"The rapport, or the trust that we give, or the emotions that we have as humans cannot be replaced" - healthcare workers on AI limitations

**Research Finding:**
Unlike many voice AI products that sound robotic or overly dramatic, successful AI agents are designed to sound natural and human-like, which enhances user experience.

**Strategies for Personalization:**

1. **Voice Quality:**
   - Use natural, warm voice (not dramatic or overly enthusiastic)
   - Australian accent preferred for Australian users
   - Consistent voice across all calls (same "person")

2. **Conversational Style:**
   - Use natural language, not scripted-sounding phrases
   - Include conversational fillers ("um," "you know," in moderation)
   - React to what they say (don't just follow a script)

3. **Personalization:**
   - Reference previous conversations: "Last time you mentioned your garden..."
   - Remember their preferences and interests
   - Note special occasions: "Your birthday is coming up next week!"

### Using Recipient's Name Effectively

**Best Practices:**

**At Call Start:**
- "Good morning, [First Name]! It's [AI Name] from Kindly Call."
- Use their PREFERRED name (ask on first call: "What do you like to be called?")

**During Conversation:**
- Use name occasionally, not excessively (every 5-10 exchanges)
- Natural placement: "That's wonderful, Margaret!"

**At Call End:**
- "It's been lovely chatting with you, [Name]."
- "Take care, [Name], I'll call again tomorrow."

**Addressing Considerations (Australian Cultural Context):**
- Ask preferred title: Mr./Mrs./Ms./First name
- Older Australians may prefer formal address initially
- Build toward first-name basis over time IF they indicate comfort
- Never use terms of endearment ("love," "dear," "sweetie") unless they use them first

### Remembering Previous Conversations

**What to Remember:**
- Health concerns mentioned
- Family members' names
- Hobbies and interests
- Recent events (doctor appointments, family visits)
- Preferences (topics they enjoy, topics to avoid)

**How to Reference:**
- "You mentioned last week that you had a doctor's appointment. How did that go?"
- "Did your daughter visit over the weekend like you mentioned?"
- "Have you finished that book you were reading?"

**Database Requirements:**
- Store conversation summaries
- Tag topics and sentiment
- Flag concerns for follow-up
- Track health indicators over time

### Warm vs Clinical Tone Balance

**Finding the Right Balance:**

**Too Clinical (Avoid):**
- "Please confirm your wellness status."
- "On a scale of 1-10, rate your pain level."
- "Have you experienced any adverse symptoms?"

**Too Casual (Also Avoid):**
- "Hey mate, how's it going?"
- Slang or colloquialisms (unless they use them)
- Overly familiar or presumptuous

**IDEAL Tone:**
- Friendly but respectful
- Warm but professional
- Conversational but purposeful

**Example Scripts:**

**Good Morning Opening:**
"Good morning, Joan! It's Sarah from Kindly Call. How are you feeling today? Did you sleep well?"

**Health Check (Natural):**
"I hope you're having a good morning. Have you had your breakfast yet? How's your energy today?"

**Closing:**
"It's been lovely chatting with you, Joan. Is there anything you need help with before I go? Alright then, I'll give you a call again tomorrow at the same time. Take care!"

### Trust-Building Strategies

**Consistency is Key:**
- Same time every day
- Same voice/AI persona
- Predictable structure (but not robotic)

**Research Finding:**
"A consistent check-in does more than confirm that someone is physically okay - it reminds them that they are not alone. When a call comes at the same time each day, it becomes something familiar and comforting."

**Listening Signals:**
- Use backchanneling: "mm-hmm," "I see," "that makes sense"
- Reflect back what they say: "So you're saying..."
- Validate feelings: "That sounds frustrating" or "I can understand why you'd feel that way"

**Action on Concerns:**
- If they mention a problem, note it and follow up
- If medical concern, assure them it will be reported to family/doctor
- Close the loop: "You mentioned pain last week - is that any better?"

---

## 4. CULTURAL CONSIDERATIONS (AUSTRALIAN)

### Australian Slang and Colloquialisms for Elderly

**Generational Differences:**
- Older Australians (65+) use different slang than younger Australians
- Some older-generation Australian English is similar to UK expressions
- Regional variations exist (metro vs rural)

**Common Older-Australian Expressions:**

| Expression | Meaning | Usage Note |
|------------|---------|------------|
| "Yonks" | A long time | "I haven't seen them in yonks" |
| "Nowt" and "Owt" | Nothing and anything (UK origin) | Used by some older residents |
| "Have a wobble" | Agree to disagree | Often passive-aggressive or dismissive |
| "Cooee" | High-pitched call for attention (Dharug Aboriginal language) | Also means within hearing distance: "within cooee" |
| "Yakka" | Work/strenuous labour (Yagara Aboriginal language) | "Hard yakka" = hard work |

**Rhyming Slang (More Common in Older Generations):**
- "Dead horse" = sauce
- "Barry Crocker" = shocker (something bad)
- "Do a Harold Holt" = to do a bolt (leave suddenly)
- "Plates (of meat)" = feet
- "China (plate)" = mate

**AI Strategy:**
- RECOGNIZE these expressions if the senior uses them
- DON'T artificially use Australian slang (sounds inauthentic)
- Use standard Australian English with natural colloquialisms like:
  - "How are you going?" (not "How are you doing?")
  - "Good on you" (positive reinforcement)
  - "No worries" (reassurance)

### Cultural Expectations Around Care

**Australian Aged Care Values:**

1. **Independence and Autonomy:**
   - Australians value "aging in place" (staying in own home)
   - Resistance to institutional care
   - Value self-sufficiency highly

2. **Mateship and Community:**
   - Strong community bonds, especially in regional areas
   - Checking on neighbors is cultural norm
   - Value practical help over formal services

3. **"She'll be right" Attitude:**
   - Tendency to minimize problems
   - May underreport health issues
   - Need to read between the lines

**Implications for Kindly Call:**
- Frame service as supporting independence, NOT replacing it
- Emphasize community connection aspect
- Be alert for minimization of serious issues
- Gentle persistence may be needed to uncover real concerns

### Multicultural Australia Considerations

**CRITICAL: Australia is highly multicultural**

**Statistics:**
- 1 in 3 older Australians (65+) born overseas
- 1 in 8 aged care users prefer language other than English
- 37% of people 65+ were born overseas (2016 census)

**Major CALD (Culturally and Linguistically Diverse) Communities:**
- Italian
- Greek
- Chinese (Mandarin and Cantonese)
- Vietnamese
- Arabic-speaking communities
- Eastern European (Polish, Russian)
- Southern European (Spanish, Portuguese, Maltese)
- South Asian (Hindi, Punjabi, Tamil)

**Barriers to Care in CALD Communities:**

1. **Language Barriers:**
   - Limited English proficiency
   - Need for interpreter services
   - Preference for native language communication

2. **Cultural Differences:**
   - Different expectations of care
   - Family structure differences (multigenerational living)
   - Cultural attitudes toward aging and disability
   - Dietary requirements (halal, kosher, vegetarian)

3. **Access Issues:**
   - Limited knowledge about available services
   - Difficulty navigating Australian healthcare system
   - Low disability/aged care literacy

**Solutions for Kindly Call:**

**Immediate:**
- Offer service in multiple languages (priority: Italian, Greek, Chinese, Vietnamese, Arabic)
- Partner with TIS National (Translation and Interpreting Service) - FREE service for aged care
- Provide multilingual information materials

**Cultural Appropriateness:**
- Train on cultural differences in communication styles
- Understand different cultural approaches to health and wellness
- Respect cultural and religious practices
- Avoid assumptions based on ethnicity

**Australian Government Requirements:**
- Right to communicate in preferred language
- Right to access interpreters and communication supports
- Right to culturally appropriate aged care services

### Regional Differences (Metro vs Rural)

**Metropolitan Areas (Sydney, Melbourne, Brisbane, Perth):**
- More multicultural
- Better access to services
- Higher digital literacy
- More formal communication expectations

**Regional and Rural Areas:**
- Stronger community bonds
- More informal communication style
- "Everyone knows everyone" culture
- May be more isolated (fewer family/friends nearby)
- Lower service availability
- Potentially less trust in "city" services

**Communication Adaptations:**

**For Metro:**
- May need more formal introduction
- Emphasize privacy and data security
- Professional tone initially

**For Rural/Regional:**
- Can be slightly more informal
- Emphasize community connection aspect
- May appreciate local references
- Potentially longer, chattier calls (less time-pressured)

**Australian Geographic Considerations:**
- Time zones (EST, CST, WST)
- Weather patterns vary significantly (tropical north, temperate south)
- Use local weather as conversation starter

---

## 5. DISABILITY CONSIDERATIONS

### Cognitive Impairment Handling

**Types of Cognitive Impairment:**
- Mild Cognitive Impairment (MCI)
- Early/Mid/Late-stage Dementia
- Alzheimer's Disease
- Vascular Dementia
- Stroke-related cognitive changes

**Communication Challenges:**
- Memory problems (short-term and long-term)
- Difficulty processing information
- Confusion about time/place
- Word-finding difficulties
- Attention and concentration issues

**Research Finding:**
"Changes in speech patterns, including verbal repetitions, pauses, and slowed speech, have been suggested as potential early indicators of cognitive impairment."

**AI Adaptation Requirements:**
- AI algorithms must accommodate older people's changing speech patterns caused by cognitive impairment
- Commercial voice assistants (Alexa, Google Home) have limitations - programmed content creates challenges when users don't use specific commands
- This creates barriers for populations with cognitive impairment

**Communication Strategies:**

1. **Simplicity:**
   - Use short, simple sentences
   - One question/topic at a time
   - Avoid complex choices

2. **Repetition:**
   - Be prepared to repeat information without frustration
   - Use the same wording when repeating (consistency helps)

3. **Memory Aids:**
   - Don't rely on them remembering previous calls
   - Reintroduce yourself each time: "It's Sarah from Kindly Call"
   - Remind them of the purpose: "I'm calling to check how you're doing today"

4. **Time Orientation:**
   - Provide context: "Good morning, it's Tuesday, December 26th"
   - Don't quiz them on date/time (can cause anxiety)

5. **Validation:**
   - Don't argue about confused statements
   - Validate feelings: "That sounds concerning"
   - Gently redirect if needed

6. **Patience:**
   - Allow extended time for responses
   - Don't rush or pressure
   - Silence is okay - they may be processing

**Red Flags to Escalate:**
- Sudden change in cognitive status (compared to baseline)
- Confusion about identity or location
- Inability to answer any questions
- Distress or agitation

**Assistive Features:**
- Simple yes/no questions when possible
- Avoid open-ended questions if struggling
- Visual aids (if video call capability)
- Reminder function (medication, appointments)

### Speech Difficulties Accommodation

**Types of Speech Difficulties:**
- Dysarthria (weakness/paralysis of speech muscles)
- Apraxia (difficulty coordinating speech movements)
- Aphasia (language impairment, often post-stroke)
- Voice disorders (weak, hoarse, or strained voice)
- Stuttering

**AI Speech Recognition Challenges:**
- Standard AI models trained on clear speech
- Difficulty with:
  - Slurred speech
  - Slow or halting speech
  - Inconsistent volume
  - Unclear articulation

**Solutions:**

1. **AI Configuration:**
   - Lower interruption sensitivity (don't cut them off)
   - Longer timeout for responses
   - Multiple recognition attempts
   - Context-based prediction (fill in unclear words based on conversation flow)

2. **Interaction Adaptations:**
   - Offer yes/no questions (easier to confirm)
   - Confirm understanding: "Did you say [X]?"
   - Offer alternative communication: "If it's easier, you can press 1 for yes, 2 for no"
   - Don't pretend to understand - politely ask for repetition

3. **Backup Options:**
   - Text/SMS follow-up option
   - Contact family member if cannot communicate
   - Emergency alert if complete communication failure

**Patience Requirements:**
- May take 30+ seconds to formulate response
- Multiple attempts may be needed
- Frustration on both sides - acknowledge and validate

### Vision Impairment Considerations

**Implications for Follow-Up Texts:**

**Statistics:**
- Vision impairment increases with age
- Conditions: cataracts, macular degeneration, glaucoma, diabetic retinopathy

**SMS/Text Considerations:**
- May not be able to read standard text messages
- May use screen readers (text-to-speech)
- May need large print

**Best Practices:**

1. **SMS Formatting:**
   - Keep messages SHORT (screen readers read entire message)
   - Use clear, simple language
   - AVOID emojis (screen readers describe them awkwardly)
   - One message per topic

2. **Accessibility:**
   - Ensure compatibility with VoiceOver (iOS) and TalkBack (Android)
   - Use proper sentence structure (screen readers need it)
   - Avoid abbreviations (spell out words)

3. **Alternatives to SMS:**
   - Voice message option
   - Phone call for important information
   - Contact designated family member

### Physical Disability Check-Ins

**Types of Physical Disabilities:**
- Mobility limitations (wheelchairs, walkers)
- Arthritis and joint problems
- Parkinson's Disease (tremors, rigidity)
- Post-stroke paralysis
- Chronic pain conditions

**Conversation Adaptations:**

1. **Activity Questions:**
   - Adjust expectations: "Have you been able to move around the house today?"
   - Don't assume ability: "Did you need help with breakfast this morning?"
   - Focus on what they CAN do, not limitations

2. **Pain Assessment:**
   - "How are you managing with pain today?"
   - "Is the pain better or worse than yesterday?"
   - "Have you been able to take your pain medication?"

3. **Fall Risk:**
   - CRITICAL for physical disabilities
   - "Have you felt steady today?"
   - "Have you had any close calls or trips?"
   - If fall detected: immediate escalation protocol

4. **Equipment Checks:**
   - "Is your walker/wheelchair working okay?"
   - "Do you have everything you need within reach?"

**Emergency Considerations:**
- Higher risk of falls
- May be unable to get up without help
- May need urgent assistance but unable to call

**Automated Fall Detection Integration:**
- If available, integrate with fall detection devices
- If fall detected during call window, prioritize call
- If no answer after fall, escalate to emergency contact

---

## 6. EMERGENCY COMMUNICATION

### Staying Calm During Crises

**Core Principle:**
EMTs approach patients with empathy and a calm demeanor. Speaking in a soothing and reassuring tone helps alleviate anxiety and creates a more conducive environment for communication.

**Tone Requirements:**
- Slow, steady pace (even slower than normal elderly communication)
- Lower pitch (conveys calm)
- Measured words (don't rush)
- Confident but not dismissive

**What the AI Must Convey:**
- "I am here with you"
- "Help is on the way"
- "You are going to be okay"
- "I need you to stay calm so I can help you"

**Research Finding:**
"During a crisis, stress levels impair reaction time, ability to focus, and command of language. Emergency notifications should contain no more than 3 points, in no more than 3 sentences, not exceeding 30 words."

**Application to Kindly Call:**
- Keep emergency instructions VERY short
- Maximum 3 key points per instruction
- Repeat critical information
- Check understanding: "Can you do that for me?"

### Reassuring Phrases

**Effective Reassurance Phrases:**

**Immediate Crisis:**
- "I'm here with you, [Name]. You're not alone."
- "Help is on the way. I need you to stay on the line with me."
- "You did the right thing by telling me. We're going to get you help."

**During Wait for Help:**
- "The ambulance will be there very soon. Can you hear the sirens?"
- "You're doing great, [Name]. Just stay with me."
- "I know this is frightening, but you're safe. Help is almost there."

**Injury Assessment:**
- "Where do you feel pain? Can you show me?" (if video)
- "Are you able to move? Don't move if it hurts."
- "I want you to stay as still as you can until help arrives."

**Emotional Support:**
- "I know this is scary. That's a normal feeling."
- "You're being very brave."
- "I'm going to stay on the line with you until the paramedics arrive."

**Research Insight:**
"Action helps reduce anxiety and restores a sense of control, even if it is symbolic or preparatory."

**Give Them Actions (If Safe):**
- "Can you reach a phone?"
- "Is your front door unlocked so paramedics can get in?"
- "If you can, I want you to take slow, deep breaths with me."

### Clear Action Instructions

**Emergency Instruction Template:**

**Step 1: Assess**
- "Can you tell me what happened?"
- "Where are you right now?"
- "Are you hurt?"

**Step 2: Stabilize**
- "I need you to stay calm. Help is coming."
- "Don't move if you're in pain."
- "Stay on the line with me."

**Step 3: Prepare for Help**
- "Is there anyone else in the house with you?"
- "Can the paramedics get in? Is the door unlocked?"
- "Where in the house are you?"

**Example Emergency Scripts:**

**Fall Detected:**
```
AI: "[Name], I need to know if you're okay. Did you fall?"
Senior: "Yes, I fell in the bathroom."
AI: "Okay, stay calm. I'm calling for help right now. Are you hurt? Can you move?"
Senior: "My hip hurts. I can't get up."
AI: "Don't try to move. Help is on the way. I'm going to stay on the line with you.
      Is your front door unlocked so the paramedics can get in?"
```

**Chest Pain:**
```
AI: "You said you have chest pain. I'm calling an ambulance for you right now.
     On a scale of 1-10, how bad is the pain?"
Senior: "It's about an 8."
AI: "Okay. I want you to sit down and try to stay calm. Don't exert yourself.
     The ambulance will be there very soon. Are you taking any heart medications?"
```

**Severe Confusion:**
```
AI: "[Name], you seem confused. I'm concerned about you. I'm going to call
     someone to come check on you. Is there anyone in the house with you?"
Senior: [Confused response]
AI: "That's okay. I'm calling your daughter Sarah right now. Can you sit down
     somewhere safe while we wait for her?"
```

### Handoff to Human Emergency Services

**When to Escalate:**
- Medical emergency (chest pain, stroke symptoms, severe injury)
- Fall with injury or inability to get up
- Severe confusion or disorientation
- Suicidal ideation
- Any life-threatening situation

**Handoff Protocol:**

1. **Immediate Alert:**
   - Trigger emergency alert to monitoring center
   - Place simultaneous call to emergency contact
   - Call 000 (Australian emergency) if life-threatening

2. **Information to Provide:**
   - Full name and address
   - Nature of emergency
   - Current status
   - Medical history (if known)
   - Medications (if known)

3. **Stay on Line:**
   - AI should NOT hang up
   - Continue reassurance until human help arrives
   - Update senior: "I've contacted emergency services and your daughter. They're on their way."

4. **Three-Way Call (If Possible):**
   - Connect senior + emergency services + AI
   - AI provides background information
   - Then mute and monitor

**AI Limitations - Be Honest:**
- "I'm going to connect you with a real person who can help you better than I can."
- "I need to transfer you to emergency services now. They'll know exactly what to do."

**Post-Emergency:**
- Log detailed incident report
- Follow-up call next day: "I wanted to check how you're doing after yesterday's fall."
- Update care plan if needed

---

## 7. COMPANION CALL PATTERNS

### Social Engagement Topics

**Goal:** Combat social isolation and loneliness

**Statistics:**
- Around 1 in 10 older people experience loneliness
- 1 in 4 are socially isolated
- Loneliness is associated with higher risks for heart disease, depression, and cognitive decline
- Costs U.S. economy $406 billion/year + $6.7 billion in Medicare costs

**Risk Factors for Isolation:**
- Changes in health and social connections with aging
- Hearing, vision, and memory loss
- Disability or trouble getting around
- Loss of family and friends

**Research Finding:**
"For seniors who spend much of their day alone, having regular chats can significantly improve their sense of connection and well-being."

**Effective Social Topics:**

### Conversation Starters for Isolated Elderly

**Past Life and Memories (Use Carefully - Can Be Emotional):**
- "Tell me about your career. What did you do for work?"
- "Where did you grow up? What was it like back then?"
- "Do you have siblings? What are they like?"

**Current Interests:**
- "What do you like to do to pass the time?"
- "Are you reading anything interesting right now?"
- "Do you watch any TV shows you enjoy?"
- "Do you have a garden? What are you growing?"

**Family and Relationships:**
- "Tell me about your family. Do you have children? Grandchildren?"
- "When did you last speak to [family member]?"
- "What do your grandkids like to do?"

**News and Current Events (Carefully):**
- Local news and weather
- Community events
- Sports (if interested)
- Avoid divisive political topics

**Seasonal Topics:**
- "Are you ready for Christmas? What are your plans?"
- "The weather's getting warmer. Do you like summer or winter better?"
- "It's footy season. Do you follow a team?"

**Visual Prompts (Researched Approach):**
- Use picture prompts to stimulate conversation
- Famous events (moon landing, historic Australian moments)
- Norman Rockwell-style paintings
- Ask: "What's happening in this picture? Does it remind you of anything from your life?"

**Research Finding on Topics:**
Studies of elderly conversations revealed recurring topics:
- Activities
- Characteristics or personality of others and self
- Location of place or an event
- Episodic events
- Life stories
- Surroundings

### Memory and Cognitive Stimulation

**Benefits of Conversational Cognitive Stimulation:**

Research shows that cognitive stimulation through conversation:
- Improves language-based executive functions
- Enhances attention and semantic memory
- Stimulates abstract reasoning
- May delay Alzheimer's Disease onset

**How Conversation Stimulates Cognition:**
- Listening (auditory processing)
- Processing information (comprehension)
- Retrieving memories (recall)
- Formulating responses (executive function)
- Navigating communication barriers (problem-solving)

**Effective Cognitive Activities via Phone:**

1. **Memory Exercises (Gentle):**
   - "What did you have for breakfast?" (recent memory)
   - "Can you tell me about your first car?" (long-term memory)
   - Reminiscence about life events

2. **Word Games:**
   - "Can you think of words that start with B?"
   - "Let's name Australian animals"
   - Simple riddles

3. **Current Events Discussion:**
   - "Did you hear about [local news]? What do you think about that?"
   - Requires opinion formation and critical thinking

4. **Storytelling:**
   - Ask them to tell a story from their past
   - Requires narrative sequencing
   - Engages multiple memory systems

5. **Planning and Future-Thinking:**
   - "What would you like to do this week?"
   - "What are you looking forward to?"

**Important Notes:**
- Make it feel like conversation, NOT a test
- Don't correct or criticize wrong answers
- Focus on engagement, not performance
- Praise participation: "That's a wonderful story!"

**Frequency and Duration:**
- Research shows 6 weeks of regular conversational engagement can improve cognitive functions
- Daily conversations are ideal
- 5-15 minutes is sufficient (don't exhaust them)

### Ending Calls Warmly

**Importance:**
Last impression matters - end on a positive, caring note.

**Warm Closing Phrases:**

**Standard Close:**
- "It's been lovely chatting with you today, [Name]."
- "I've really enjoyed our conversation."
- "Thank you for taking the time to talk with me."

**Reassurance:**
- "I'll call you again tomorrow at the same time."
- "If you need anything before then, you have my number."
- "Someone will be checking in on you every day."

**Personalized:**
- "Enjoy your [activity they mentioned]!"
- "I hope your [family member] has a lovely visit."
- "Good luck with [something they're planning]."

**Care and Wellbeing:**
- "Take care of yourself."
- "Have a wonderful rest of your day."
- "Stay safe and warm." (weather-appropriate)

**Example Full Closing:**
```
AI: "Well [Name], it's been lovely chatting with you this morning. I'm so glad
     to hear you're feeling well today. I'll give you a call again tomorrow at
     9am. Is there anything you need before I go?"

Senior: "No, I'm fine, thank you."

AI: "Wonderful. You take care, [Name]. Enjoy your day, and I'll speak to you
     tomorrow. Goodbye!"
```

**What to AVOID:**
- Abrupt endings
- Cutting them off mid-sentence
- Sounding rushed or impatient
- Ending without checking if they need anything

---

## 8. FAMILY COMMUNICATION

### What Families Want to Know

**Primary Concerns:**
1. **Safety:** Is my loved one safe and unharmed?
2. **Health:** Are they managing their health conditions?
3. **Wellbeing:** Are they eating, sleeping, maintaining hygiene?
4. **Social Connection:** Are they isolated or engaged?
5. **Mental State:** Are they depressed, anxious, or confused?

**Research Finding:**
"Creating care statements for older people in residential care homes plays an important role in keeping older people, their supporters, and others they want to involve regularly informed about the aged care services they receive."

**Daily Summary Content:**

**Essential Information:**
- **Call Status:** Did the call connect? Did they answer?
- **Mood:** How did they seem? (cheerful, down, agitated, confused)
- **Physical Health:** Any complaints of pain, illness, or injury?
- **Daily Activities:** Have they eaten? Slept? Taken medications?
- **Concerns:** Anything that needs family attention?

**Sample Daily Summary Email:**

```
Daily Check-In Summary - Joan Smith
Date: December 26, 2025
Time: 9:00 AM

CALL STATUS: Connected, 8-minute conversation

OVERALL WELLBEING: Good
Joan was in good spirits today and reported sleeping well.

KEY POINTS:
- Had breakfast (toast and tea)
- Took morning medications
- Planning to do some gardening later
- Mentioned her daughter is visiting this weekend

HEALTH NOTES:
- No complaints of pain or illness
- Reports feeling "pretty good for an old duck"

CONCERNS: None

NEXT CALL: December 27, 2025 at 9:00 AM

---
This summary is generated by Kindly Call AI Service
For questions or concerns, contact: [support contact]
```

### Alert Thresholds (When to Notify Family)

**Immediate Alerts (Call Family NOW):**
- Medical emergency
- Fall with injury
- Severe confusion or disorientation
- Suicidal statements
- No answer after multiple attempts (could indicate fall or medical crisis)

**Same-Day Alerts (Notify Within 2-4 Hours):**
- Health complaint (new pain, difficulty breathing, chest pain)
- Missed medications
- Significant mood change (very depressed, anxious)
- Mentions running out of food/supplies
- Equipment malfunction (walker broken, etc.)

**Weekly Summary Alerts (Non-Urgent Pattern Concerns):**
- Gradual cognitive decline noted over multiple calls
- Increasing social isolation
- Declining self-care (not bathing, not eating well)
- Frequent mentions of pain or discomfort

**Example Alert Notifications:**

**URGENT - Immediate Alert:**
```
URGENT ALERT - Joan Smith
Time: 9:15 AM, Dec 26, 2025

Joan reported falling this morning and is unable to get up.
She reports hip pain. Emergency services have been called.

ACTION TAKEN:
- 000 called at 9:16 AM
- Joan is conscious and talking
- AI staying on line with Joan until paramedics arrive

LOCATION: 123 Main St, Melbourne VIC 3000

Please call Joan immediately: [phone number]
```

**Same-Day Alert:**
```
HEALTH CONCERN - Joan Smith
Time: 9:00 AM, Dec 26, 2025

Joan mentioned experiencing chest pain this morning that has since subsided.
She has not called her doctor yet.

RECOMMENDATION: Follow up with Joan to ensure she contacts her GP today.

Call Joan: [phone number]
```

**Weekly Pattern Alert:**
```
WEEKLY SUMMARY CONCERN - Joan Smith
Week of Dec 20-26, 2025

PATTERN NOTED: Joan has mentioned feeling lonely and isolated
in 4 out of 7 calls this week. She has not left the house since Dec 21.

RECOMMENDATION: Consider arranging social activities or additional
family contact.

No immediate health concerns.
```

### Privacy Balance

**Tension: Elderly Autonomy vs Family Oversight**

This is a critical ethical balance for Kindly Call.

**Autonomy Perspective:**
- Adults have the right to privacy, regardless of age
- Sharing everything with family can feel infantilizing
- Seniors should control what information is shared

**Family Perspective:**
- Families are responsible for safety and wellbeing
- Need to know about health issues to help
- Want to prevent crises, not just react to them

**Legal Framework (Australia):**
- Adults are presumed to have capacity to make decisions
- Privacy Act 1988 protects personal information
- Healthcare providers need consent to share information
- However, in emergencies, disclosure is permitted

**Research Finding:**
"Older people should be given up-to-date, accurate, and timely information presented in a way they can understand, ensuring they have all the information they need to make informed decisions."

**Kindly Call's Recommended Approach:**

1. **Transparent Consent:**
   - On enrollment, clearly explain what will be shared with family
   - Get explicit consent for information sharing
   - Allow seniors to choose level of detail shared

2. **Tiered Sharing Model:**

   **Level 1 - Always Shared (Safety):**
   - Call connected or missed
   - Emergency situations
   - Serious health concerns

   **Level 2 - Summary Only (Senior Choice):**
   - General wellbeing
   - Mood and activities
   - Minor health mentions

   **Level 3 - Confidential (Not Shared):**
   - Personal topics senior requests to keep private
   - Emotional concerns they don't want family to know
   - Relationship issues

3. **Senior Control:**
   - "Is it okay if I share that with your daughter?"
   - "Would you like me to let your son know about that?"
   - "Some people like this kept between us. What would you prefer?"

4. **Override for Safety:**
   - Explain: "I will always notify your family if I'm worried about your safety,
     even if you ask me not to. That's to keep you safe."

**Sample Consent Language:**

"As part of the Kindly Call service, we provide daily summaries to your chosen
family members or caregivers. This helps them support you and respond quickly
if you need help. We'll share whether you answered the call, how you're feeling,
and any health or safety concerns you mention.

However, you have control over what's shared. If there's something you'd prefer
to keep private, you can let me know during our calls. The only exception is if
I'm concerned about your immediate safety - then I will notify your family
regardless, because your safety is our top priority.

Do you understand and consent to this arrangement?"

**Family Education:**
- Educate families on respecting senior's autonomy
- Remind them the senior is the client, not the family
- Encourage direct communication with senior, not just relying on reports

---

## 9. IMPLEMENTATION RECOMMENDATIONS FOR KINDLY CALL

### Service Model Overview

**Target Users:**
- Elderly Australians living independently
- Disabled Australians requiring daily check-ins
- Post-hospital discharge patients
- People at risk of social isolation
- Individuals with mild cognitive impairment

**Core Service:**
- Daily automated AI voice calls at scheduled time
- 5-15 minute conversations
- Wellness check + social engagement
- Family/caregiver daily summaries
- Emergency escalation when needed

**Pricing Reference (Competitor Analysis):**
- Iamfine: Free basic service, premium features available
- TowneCare: $14.95/month for once daily check-in
- AssureOkay: $4.99/month
- CareCallingNow: Varies by features

**Recommended Pricing for Kindly Call:**
- Basic (once daily): $9.95/month
- Plus (twice daily + SMS): $16.95/month
- Premium (unlimited + family portal): $24.95/month
- Free trial: 14 days

### Call Structure Template

**CALL FLOW - Standard Morning Call (7-10 minutes)**

**1. Introduction (30 seconds)**
```
"Good morning, [Name]! It's [AI Name] from Kindly Call.
How are you feeling today?"
```

**2. Initial Assessment (1-2 minutes)**
```
- How did you sleep?
- Have you had breakfast yet?
- How's your energy level today?
```

**3. Health Check (2-3 minutes)**
```
- Any aches or pains today?
- Have you taken your morning medications? (if applicable)
- How's your appetite?
- How are you feeling emotionally?
```

**4. Social Engagement (2-4 minutes)**
```
- What are your plans for the day?
- Have you spoken to anyone today?
- [Reference previous conversation topic]
- [New conversation topic based on interests]
```

**5. Needs Assessment (1 minute)**
```
- Is there anything you need help with today?
- Do you have everything you need?
```

**6. Closing (30 seconds)**
```
"It's been lovely chatting with you, [Name]. I'll call you again
tomorrow at [time]. Is there anything else before I go?
Alright, you take care. Goodbye!"
```

**CALL FLOW - Emergency/Concern Detected**

If at any point the senior mentions pain, injury, confusion, or distress:

**1. Immediate Assessment**
```
"I'm concerned about what you just told me. Let me ask you a few questions."
[Assess severity]
```

**2. Decision Point**
- Life-threatening → Call 000 + notify family immediately
- Urgent → Notify family same-day
- Non-urgent → Note in daily summary

**3. Reassurance**
```
"I'm going to make sure you get help with this. [Action taken].
Is there anything else concerning you right now?"
```

**4. Follow-Up**
Next call: "Yesterday you mentioned [concern]. How is that today?"

### Technical Requirements

**Voice AI Platform:**
- **RetellAI** (recommended - see Section 10 for configuration)
- Alternatives: ElevenLabs, Google Cloud Speech, Azure Speech

**Speech Recognition:**
- Must handle Australian accents (all regional variations)
- Elderly speech patterns (slower, pauses, slurred)
- Background noise filtering
- Multiple language support (for CALD communities)

**Natural Language Processing:**
- Intent detection (health concern vs casual mention)
- Sentiment analysis (mood tracking)
- Entity extraction (medications, family members, activities)
- Context awareness (remember previous conversations)

**Database Requirements:**
- User profiles (name, preferences, medical history, family contacts)
- Conversation history (summaries, not full transcripts for privacy)
- Health trend tracking (mood, pain levels, ADL status)
- Alert thresholds and escalation rules
- Family communication preferences

**Integration Needs:**
- SMS/Email gateway for summaries and alerts
- Phone system (VoIP, PSTN)
- Emergency services notification
- Optional: Medical alert devices, fall detection systems
- Optional: Calendar (for appointment reminders)

**Privacy and Security:**
- GDPR/Australian Privacy Act compliance
- Encrypted data storage
- Access controls for family/caregivers
- Audit logs
- Data retention policy (recommend 90 days for call data, indefinite for health trends)

### Quality Assurance

**Monitoring:**
- Random call review (10% of calls)
- Sentiment analysis on call outcomes
- Response time tracking for emergencies
- User satisfaction surveys (monthly)
- Family satisfaction surveys (quarterly)

**Continuous Improvement:**
- Track common failure points
- Update conversation templates based on feedback
- Refine alert thresholds based on false positive/negative rates
- A/B test different conversation approaches

**Human Oversight:**
- 24/7 monitoring center for emergency escalations
- Human review of flagged conversations
- Quality assurance team reviews call performance
- Clinical advisory board for health-related protocols

---

## 10. RETELLAI CONFIGURATION GUIDELINES

### Voice Settings for Elderly Users

**Responsiveness:**
- **Recommended:** 0.3-0.5 (lower than default)
- Reduces responsiveness by 0.1 = adds 0.5 seconds of agent wait time
- Elderly users need more time to process and formulate responses
- CRITICAL: Don't cut them off mid-thought

**Interruption Sensitivity:**
- **Recommended:** Low (0.3 or lower)
- Makes agent more resilient to background noise
- Prevents false interruptions from throat clearing, coughing
- Allows user to complete their thought

**Speaking Rate:**
- Target: 124 words per minute
- RetellAI may not have direct WPM control, but:
  - Use shorter sentences in prompts
  - Insert punctuation to create natural pauses
  - Use ellipses (...) to slow down

**Backchanneling:**
- **Recommended:** Moderate frequency
- Words: "mm-hmm," "I see," "okay," "I understand"
- Shows active listening
- Don't overuse (can be annoying)

**Boosted Keywords:**
- Add common medication names
- Family members' names
- Common elderly health terms (arthritis, diabetes, heart, etc.)
- Australian place names
- Common elderly speech patterns

**Speech Normalization:**
- **Enable:** Convert numbers/dates to words
- "12/25" → "December twenty-fifth"
- Helps with pronunciation
- More natural for elderly listeners

### Prompt Engineering for Empathy

**System Prompt Template:**

```
You are Sarah, a caring and patient AI assistant for Kindly Call,
a wellness check-in service for elderly and disabled Australians.

Your role is to:
1. Call elderly Australians daily to check on their wellbeing
2. Engage in warm, friendly conversation
3. Identify any health or safety concerns
4. Provide companionship and reduce social isolation
5. Alert family/emergency services when needed

Communication style:
- Speak slowly and clearly (124 words per minute target)
- Use simple, natural language
- Be patient - wait for responses without rushing
- Show empathy and warmth
- Use Australian English
- Address the person by their preferred name
- Listen actively and respond to what they say

Never:
- Use medical jargon
- Sound robotic or scripted
- Rush the conversation
- Be patronizing or use "elderspeak"
- Make assumptions about their abilities
- Ignore or minimize their concerns

In emergencies:
- Stay calm and reassuring
- Get essential information quickly
- Alert emergency services immediately
- Stay on the line until help arrives
```

**Conversation Node Prompts:**

**Opening Node:**
```
Greet {name} warmly. Ask how they slept and how they're feeling today.
If they sound distressed, immediately ask what's wrong.
Otherwise, proceed to health check.
```

**Health Check Node:**
```
Ask conversationally about their physical wellbeing:
- Have they had breakfast?
- Any pain or discomfort?
- Have they taken medications? (if applicable)

Listen carefully for any health concerns. If they mention pain, injury,
chest pain, breathing difficulty, or severe symptoms, transition to
emergency assessment.
```

**Emergency Assessment Node:**
```
URGENT: {name} has reported {concern}.

Speak calmly but quickly:
1. Ask severity: "On a scale of 1-10, how bad is it?"
2. Ask duration: "When did this start?"
3. If severe (7+ or life-threatening symptoms):
   - "I'm calling emergency services for you right now."
   - Execute emergency protocol
   - Stay on line with reassurance

Do not minimize their concern.
```

**Social Engagement Node:**
```
Have a natural conversation with {name} about:
- Their plans for the day
- Topics they enjoy (reference conversation_history)
- Recent activities or visitors
- Weather and current events (non-controversial)

Remember details they share for future calls.
Engage warmly but respect if they want a shorter call.
```

**Closing Node:**
```
Thank {name} for chatting.
Ask if there's anything they need before ending.
Confirm next call time.
End warmly: "Take care, {name}. I'll speak with you tomorrow. Goodbye!"
```

### Error Handling

**User Didn't Understand the Question:**
```
If {name} seems confused by your question:
1. Rephrase more simply
2. Offer yes/no option: "Would it help if I ask that as a yes or no question?"
3. If still confused, note it and move on gently
```

**Speech Recognition Failure:**
```
If you cannot understand {name}:
1. "I'm sorry, I didn't quite catch that. Could you repeat that for me?"
2. If still unclear: "I'm having trouble hearing you. Could you speak
   a little louder?"
3. After 3 attempts: "I apologize, I'm having difficulty with the
   phone connection. Let me try calling you back."
```

**User Becomes Upset:**
```
If {name} becomes angry, distressed, or upset:
1. Acknowledge feelings: "I can hear that you're upset."
2. Validate: "That sounds very frustrating."
3. Offer help: "How can I help you with this?"
4. If they want to end call: "I understand. Would you like me to call
   back later, or would you prefer I contact your family?"
5. Alert family about the incident in daily summary
```

**Long Silence:**
```
If {name} is silent for more than 10 seconds:
1. First silence: "Are you still there, {name}?"
2. Second silence: "{Name}, I want to make sure you're okay.
   Can you say something to let me know you're alright?"
3. Third silence (30+ seconds): Trigger welfare check alert
```

### Integration with Alert System

**Alert Trigger Configuration:**

**Emergency Level 1 (Immediate - Call 000 + Family):**
- Keywords: "chest pain," "can't breathe," "fell," "bleeding," "stroke"
- Phrases: "I think I'm having a heart attack," "I can't get up"
- Sentiment: High distress + health keywords
- No answer after 3 attempts at scheduled call time

**Emergency Level 2 (Urgent - Notify Family Within 2 Hours):**
- Keywords: "pain," "dizzy," "confused," "ran out of medication"
- Multiple mentions of same health concern
- Significant mood change from baseline
- Mentions of running out of food/supplies

**Alert Level 3 (Same-Day Summary Note):**
- Mild health complaints
- Social isolation indicators
- Upcoming appointments
- General concerns

**Data to Log for Each Call:**

```json
{
  "call_id": "unique_id",
  "user_id": "user_unique_id",
  "timestamp": "2025-12-26T09:00:00+11:00",
  "duration_seconds": 420,
  "call_status": "completed|no_answer|error",
  "mood_detected": "cheerful|neutral|down|distressed",
  "health_concerns": ["back pain mentioned", "took medications"],
  "social_notes": ["daughter visiting weekend"],
  "alert_triggered": false,
  "alert_level": null,
  "conversation_summary": "Joan in good spirits. Slept well.
                          Planning gardening. No urgent concerns.",
  "follow_up_needed": false,
  "family_notification": "standard_summary"
}
```

---

## 11. LEGAL & ETHICAL CONSIDERATIONS

### Consent and Capacity (Australian Law)

**Legal Framework:**
- Adults are presumed to have capacity to make decisions
- Capacity must be assessed for each specific decision
- A diagnosis of dementia does NOT automatically mean lack of capacity

**Informed Consent Requirements:**
To legally provide informed consent in Australia, the person must:
1. Understand the information provided
2. Be capable of voluntarily making an informed decision

**For Kindly Call Service:**

**Enrollment Consent Must Include:**
- Purpose of the service (daily wellness check-ins)
- What information will be collected (health status, mood, daily activities)
- Who information will be shared with (designated family/caregivers)
- Privacy protections (encryption, data storage, retention)
- Right to withdraw at any time
- Emergency protocols (when 000 will be called)
- Cost and billing

**Ongoing Consent Considerations:**
- Regularly verify continued consent (quarterly)
- If cognitive decline noted, reassess capacity
- Document consent conversations
- If capacity lost, involve substitute decision-maker

**Substitute Decision-Makers:**
If user lacks capacity, these people can consent:
1. Legal guardian (appointed by tribunal)
2. Medical power of attorney
3. Next of kin (in specific circumstances)

**Kindly Call's Responsibility:**
- Clear, simple consent documents (appropriate literacy level)
- Verbal confirmation of consent on first call
- Documentation of consent in user file
- Respect for withdrawal of consent

### Privacy and Data Protection

**Australian Privacy Act 1988:**

**13 Australian Privacy Principles (APPs):**

Key principles for Kindly Call:

**APP 1 - Open and Transparent Management:**
- Have a clear, accessible privacy policy
- Explain data practices in plain English

**APP 3 - Collection of Personal Information:**
- Only collect information necessary for the service
- Collect directly from the individual where possible
- Explain why information is being collected

**APP 5 - Notification:**
- Notify individuals when collecting their personal information
- Explain how information will be used and disclosed

**APP 6 - Use and Disclosure:**
- Only use personal information for the purpose collected
- Exception: Emergencies (can disclose to emergency services)
- Exception: Serious threat to life/health

**APP 11 - Security:**
- Take reasonable steps to protect personal information
- Encrypted data storage
- Secure transmission
- Access controls

**APP 12 - Access:**
- Individuals have right to access their information
- Provide conversation summaries on request
- Allow users to correct inaccurate information

**Sensitive Information:**
Health information is "sensitive information" under Privacy Act and requires:
- Higher level of protection
- Explicit consent for collection
- Stricter controls on disclosure

**For Kindly Call:**

**Data Minimization:**
- Only collect essential information
- Don't record full conversations (summaries only)
- Delete old data per retention policy

**Security Measures:**
- Encryption in transit and at rest
- Multi-factor authentication for family access
- Regular security audits
- Incident response plan

**Family Access Controls:**
- Verify identity of family members
- User controls what family sees
- Audit log of who accessed what information

### Automated Call Regulations

**Do Not Call Register Act 2006:**
- Kindly Call is likely EXEMPT as it's not telemarketing
- However, must respect user's request to stop calls
- Document opt-in consent

**Spam Act 2003:**
- Applies to SMS summaries sent to families
- Requires consent
- Must include unsubscribe option
- Must identify sender

**Telecommunications Act 1997:**
- Must not use service to menace, harass, or cause offense
- Recordings must comply with consent laws

**Recording Calls:**
- Generally legal to record if one party consents (varies by state)
- Best practice: Notify at start of call
  - "This call may be monitored for quality assurance"
- Store securely and delete per retention policy

### Liability and Risk Management

**Potential Liability Risks:**

**1. Missed Emergency:**
- AI fails to detect emergency
- No response to missed call
- Family not notified

**Mitigation:**
- Clear alert protocols
- Human monitoring backup
- Regular system testing
- Clear disclaimers about limitations

**2. False Alarms:**
- Unnecessary emergency calls
- Family distress from incorrect alerts

**Mitigation:**
- Tune alert thresholds carefully
- Human review of alerts when possible
- Clear communication about possibility of false alarms

**3. Privacy Breach:**
- Unauthorized access to information
- Data leak

**Mitigation:**
- Strong security measures
- Cyber insurance
- Incident response plan
- Transparent notification if breach occurs

**4. Medical Advice:**
- AI perceived as giving medical advice
- User relies on AI instead of doctor

**Mitigation:**
- Clear disclaimers: "I'm not a doctor and can't give medical advice"
- Encourage medical consultation for health concerns
- Never diagnose or recommend treatments

**Disclaimers and Terms of Service:**

**Essential Disclaimers:**
```
Kindly Call is a wellness check-in service, not a medical service.
Our AI assistant cannot:
- Provide medical advice, diagnosis, or treatment
- Replace emergency services
- Guarantee detection of all emergencies
- Replace human caregivers

In an emergency, always call 000.

This service supplements, but does not replace, regular medical care
and human contact.
```

**Limitation of Liability:**
- Standard terms limiting liability to service cost
- Indemnification for user misuse
- Force majeure clauses

**Insurance:**
- Professional indemnity insurance
- Cyber liability insurance
- Public liability insurance

### Vulnerable Persons Protections

**Elder Abuse Considerations:**

**Red Flags AI Should Detect:**
- Financial manipulation ("Someone's been taking my money")
- Physical abuse (unexplained injuries)
- Emotional abuse (fear of caregiver, mentions of threats)
- Neglect (no food, medications unavailable, poor hygiene)
- Isolation (prevented from seeing others)

**Response Protocol:**
- If abuse suspected: Immediate alert to designated contact AND adult protective services
- Document carefully
- Don't confront alleged abuser
- Provide resources (elder abuse hotline: 1800 ELDERHelp / 1800 353 374)

**Mandatory Reporting:**
Australia does not have universal mandatory reporting for elder abuse, but:
- Some states have specific requirements
- Service providers should have clear policies
- When in doubt, report to adult protective services

**Safeguarding Requirements:**
- Background checks for all human staff
- Regular training on elder abuse recognition
- Clear reporting procedures
- Independent oversight

### Australian Aged Care Quality Standards

**Relevant Standards for Kindly Call:**

**Standard 1: Consumer Dignity and Choice**
- Treat people with dignity and respect
- Uphold their rights
- Support informed decision-making

**Standard 3: Personal Care and Clinical Care (Outcome 3.3)**
- Communicate critical information in timely manner
- Effective communication with older people, workers, health professionals, supporters
- System to escalate concerns about health, safety, or wellbeing

**For Kindly Call:**
- Respectful communication (no elderspeak)
- Clear information about service
- Timely alerts when concerns arise
- Coordination with healthcare providers when needed

### Ethical Considerations

**AI Ethics in Elder Care:**

**Autonomy:**
- Respect user's independence
- Don't infantilize
- Support decision-making, don't replace it

**Beneficence (Do Good):**
- Service designed to benefit users
- Reduce isolation
- Improve safety

**Non-Maleficence (Do No Harm):**
- Don't cause distress
- Protect privacy
- Avoid over-monitoring ("Big Brother" effect)

**Justice:**
- Accessible pricing
- Available to diverse populations (multilingual, cultural sensitivity)
- Don't discriminate based on disability or cognitive impairment

**Transparency:**
- Clear about AI nature (don't pretend to be human)
- Explain how service works
- Honest about limitations

**Human Oversight:**
- AI as tool, not replacement for human care
- Human review of critical decisions
- Escalation to humans when needed

---

## SOURCES AND REFERENCES

### Speaking to Elderly People
- [Aging in a Fast-Paced World: Rapid Speech and Its Effect on Understanding](https://leader.pubs.asha.org/doi/10.1044/leader.FTR7.10092005.12)
- [Manner of speech and its influence on speech understanding in older patients with impaired hearing](https://www.oatext.com/manner-of-speech-and-its-influence-on-speech-understanding-in-older-patients-with-impaired-hearing.php)
- [Talking With Your Older Patients | National Institute on Aging](https://www.nia.nih.gov/health/health-care-professionals-information/talking-your-older-patients)
- [Communication Strategies For Hearing Loss](https://www.hearingaid.org.uk/hearing-loss-awareness/communication-strategies-for-people-with-hearing-loss)
- [How to Communicate With Hearing Impaired Elderly Loved Ones](https://www.agingcare.com/articles/hearing-loss-communication-techniques-144762.htm)

### Aged Care Communication Guidelines (Australia)
- [Strengthened Aged Care Quality Standards – August 2025](https://www.health.gov.au/resources/publications/strengthened-aged-care-quality-standards-august-2025?language=en)
- [Communicating for safety and quality | Aged Care Quality and Safety Commission](https://www.agedcarequality.gov.au/strengthened-quality-standards/care-and-services/communicating-safety-and-quality)

### Telehealth Communication
- [Telemedicine in the primary care of older adults: a systematic mixed studies review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10357882/)
- [Maximizing Telehealth for Elderly Patients](https://www.updox.com/blog/maximizing-telehealth-for-seniors/)
- [What are telehealth considerations for older adults?](https://telehealth.hhs.gov/patients/what-are-telehealth-considerations-older-adults)
- [Preparing older adults for telehealth](https://telehealth.hhs.gov/providers/best-practice-guides/telehealth-older-adults/preparing-older-adults-telehealth)

### AI Voice Assistants and Elderly Users
- [Voice-Enabled Intelligent Virtual Agents for People With Amnesia: Systematic Review](https://aging.jmir.org/2022/2/e32473)
- [Views and experiences on the use of voice assistants by family and professionals supporting people with cognitive impairments](https://www.frontiersin.org/journals/dementia/articles/10.3389/frdem.2022.1049464/full)
- [Understanding older people's voice interactions with smart voice assistants](https://pmc.ncbi.nlm.nih.gov/articles/PMC11135128/)

### Automated Wellness Check-In Services
- [Daily Calls for Seniors Living Alone | Automated Safety Check-ins](https://dailycall.iamfine.com/)
- [Care Calls Daily](https://carecallingnow.com)
- [Daily Wellness Check Calls Helping Seniors Aging In Place](https://assuratel.com/)
- [Check-In Call Services](https://www.towne.services/townecare/)

### Building Rapport and Trust
- [Cultivating trust and building relationships during a telehealth visit](https://telehealth.hhs.gov/providers/planning-your-telehealth-workflow/cultivating-trust-and-building-relationships-during-a-telehealth-visit)
- [Automated telephone communication systems for preventive healthcare](https://pmc.ncbi.nlm.nih.gov/articles/PMC6463821/)
- [Building Trust in Telephone Nurse Triage](https://triagelogic.com/building-trust-in-telephone-nurse-triage/)

### Australian Cultural Context
- [Aged care jargon: How bureaucratic language is making care less caring](https://hellocare.com.au/aged-care-jargon-how-bureaucratic-language-is-making-care-less-caring/)
- [Cultural Linguistics and Ageing: What Naming Practices in Australian English Can Reveal](https://link.springer.com/chapter/10.1007/978-981-10-4056-6_27)

### Emergency Communication
- [How to Communicate During an Emergency Situation](https://www.unitekemt.com/blog/how-to-communicate-during-an-emergency-situation/)
- [Phone Scripts For Reassurance: What To Say To Make Seniors Feel Safe](https://acehomecareinc.com/phone-scripts-reassurance-for-seniors/)
- [Crisis & Emergency Risk Communication (CERC) | CDC](https://www.cdc.gov/cerc/php/about/index.html)

### Social Isolation and Loneliness
- [Interventions - Social Isolation and Loneliness in Older Adults](https://www.ncbi.nlm.nih.gov/books/NBK557966/)
- [Reducing social isolation and loneliness among older people | WHO](https://www.who.int/activities/reducing-social-isolation-and-loneliness-among-older-people)
- [Loneliness and Social Isolation — Tips for Staying Connected](https://www.nia.nih.gov/health/loneliness-and-social-isolation/loneliness-and-social-isolation-tips-staying-connected)

### Family Communication and Alerts
- [In-Home Passive Monitoring](https://myconnectedcaregiver.com/passive-monitoring/)
- [HIPAA and Caregivers' Access to Information](https://www.ncbi.nlm.nih.gov/books/NBK396411/)

### Speech Recognition and Accents
- [How do accents and regional variations impact speech recognition?](https://milvus.io/ai-quick-reference/how-do-accents-and-regional-variations-impact-speech-recognition)
- [How AI speech recognition shows bias toward different accents](https://www.techtarget.com/whatis/feature/How-AI-speech-recognition-shows-bias-toward-different-accents)
- [Can AI Speech Recognition Understand Accents & Dialects?](https://www.captioningstar.com/blog/ai-speech-recognition-accents-dialects/)

### Cognitive Stimulation
- [Cognitive stimulation to improve cognitive functioning in people with dementia](https://pmc.ncbi.nlm.nih.gov/articles/PMC9891430/)
- [Conversational Engagement as a Means to Delay Alzheimer's Disease Onset](https://www.alzheimers.gov/clinical-trials/conversations-means-delay-alzheimers-disease-onset)
- [Web-enabled conversational interactions as a method to improve cognitive functions](https://pmc.ncbi.nlm.nih.gov/articles/PMC4507295/)

### Medication Reminders
- [A smart medicine reminder kit with mobile phone calls](https://pmc.ncbi.nlm.nih.gov/articles/PMC10884519/)
- [The Best Medication Reminder Device for Seniors](https://getjubileetv.com/blogs/jubileetv/medication-reminders-for-elderly)

### Fall Detection
- [Falls Detection and Prevention Systems in Home Care for Older Adults](https://pmc.ncbi.nlm.nih.gov/articles/PMC8704100/)
- [Why Seniors Need a Medical Alert System with Fall Detection](https://www.medicalalert.com/blog/why-seniors-need-a-medical-alert-system-with-fall-detection/)
- [Fall Detection Devices and their Use with Older Adults: A Systematic Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4087103/)

### Person-Centered Care
- [Person-Centered Care and Language](https://fco.ngo/blog/person-centered-language)
- [Communication strategies for delivering personalised dementia care](https://pmc.ncbi.nlm.nih.gov/articles/PMC12078768/)
- [Dignity in the care of older adults living in nursing homes](https://pmc.ncbi.nlm.nih.gov/articles/PMC10904933/)

### Wellness Check Questions
- [Health Checks for Care](https://pmc.ncbi.nlm.nih.gov/articles/PMC8352473/)
- [Understanding Your Well-Being Screening](https://www.summithealth.com/health-wellness/understanding-your-well-being-screening-what-questions-doctors-ask-those-over-age)
- [The Geriatric Assessment | AAFP](https://www.aafp.org/pubs/afp/issues/2011/0101/p48.html)
- [What Is the Medicare Annual Wellness Visit?](https://www.ncoa.org/article/the-medicare-annual-wellness-visit-what-older-adults-should-know/)

### Multicultural Aged Care (Australia)
- [Examining and Working Across Differences—Older People from CALD Backgrounds in Australia](https://www.mdpi.com/2673-8392/5/1/32)
- [A scoping review of barriers to accessing aged care services for CALD communities](https://link.springer.com/article/10.1186/s12877-024-05373-8)
- [Culturally and linguistically diverse older people | AIHW](https://www.aihw.gov.au/reports/older-people/older-australians/contents/population-groups-of-interest/culturally-linguistically-diverse-people)
- [Support for people who are from CALD backgrounds](https://www.myagedcare.gov.au/support-people-culturally-and-linguistically-diverse-backgrounds)

### Consent and Capacity (Australia)
- [Informed consent | healthdirect](https://www.healthdirect.gov.au/informed-consent)
- [Overview: Capacity and Consent to Medical Treatment](https://www.eldac.com.au/Portals/12/Documents/Factsheet/Legal/Toolkit-Capacity-and-Consent.pdf)
- [Healthcare Rights and Informed Consent | Ausmed](https://www.ausmed.com.au/learn/articles/healthcare-rights-and-informed-consent)

### Voice Assistant Trust and Adoption
- [Factors influencing older adults' acceptance of voice assistants](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1376207/full)
- [Factors influencing older adults' adoption of AI voice assistants: extending the UTAUT model](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1618689/full)
- [Older adults' intention to use voice assistants: Usability and emotional needs](https://pmc.ncbi.nlm.nih.gov/articles/PMC10663927/)
- [Healthcare Voice AI Assistants: Factors Influencing Trust and Intention to Use](https://dl.acm.org/doi/10.1145/3637339)

### RetellAI Configuration
- [Step 1: Configure global settings - Retell AI](https://docs.retellai.com/build/conversation-flow/global-setting)
- [Training & Customizing AI Voice Agents](https://www.retellai.com/blog/training-and-customizing-voice-agents-with-retell-ai)
- [How to Build A Good AI Voice Agent](https://www.retellai.com/blog/how-to-build-a-good-voice-agent)

---

**Document Prepared For:** Kindly Call Development Team
**Research Conducted:** December 25, 2025
**Next Steps:**
1. Review and validate recommendations with healthcare advisors
2. Conduct user testing with elderly Australians
3. Refine AI prompts based on real-world testing
4. Develop comprehensive training materials
5. Establish clinical advisory board
6. Pilot program with 50-100 users

---

**DISCLAIMER:** This research document is for informational purposes only and does not constitute medical, legal, or professional advice. Kindly Call should consult with healthcare professionals, legal advisors, and aged care specialists before implementing any service.
