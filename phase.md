Human Brain — Phase Roadmap

«A research-oriented roadmap for building a continuously learning, stateful, and eventually autonomous neural system.»

---

🇮🇷 فارسی

مقدمه

هدف پروژه‌ی Human Brain ساخت یک chatbot معمولی، RAG system یا AI Agent کلاسیک نیست.

هدف این پروژه بررسی این سؤال است:

«آیا می‌توان سیستمی ساخت که به‌جای اینکه صرفاً "Input → Output" باشد، یک state داخلی و پیوسته داشته باشد، از تجربه‌های قبلی یاد بگیرد، درباره‌ی چیزهایی که نمی‌داند uncertainty داشته باشد، هدف ایجاد کند و در نهایت بدون دریافت ورودی مستقیم از کاربر، خودش فعالیت‌هایی را آغاز کند؟»

معماری پروژه به‌صورت تدریجی ساخته می‌شود تا بتوانیم اثر هر قابلیت را به‌صورت مستقل آزمایش و اندازه‌گیری کنیم.

---

Architecture Evolution

مسیر کلی پروژه:

Chat Model
    ↓
Stateful Chat Model
    ↓
Memory
    ↓
Continual Learning
    ↓
Uncertainty
    ↓
Curiosity
    ↓
Goal Generation
    ↓
Internal Activity
    ↓
Autonomous Actions
    ↓
Self-Directed Learning

هدف این نیست که از ابتدا یک سیستم پیچیده بسازیم.

هر مرحله باید یک hypothesis مشخص داشته باشد و بتواند با آزمایش مستقل validate شود.

---

Phase 0 — Research & Experimental Foundation

هدف

قبل از ساخت مدل، باید مشخص کنیم دقیقاً چه چیزی را می‌خواهیم اندازه‌گیری کنیم.

این فاز پایه‌ی علمی پروژه است.

مفاهیم

- Human-like behavior
- Memory
- Episodic memory
- Semantic memory
- Continual learning
- Forgetting
- Identity
- Uncertainty
- Curiosity
- Goal generation
- Autonomous behavior
- Internal state
- Replay
- Consolidation

سؤال‌های اصلی

What is memory?

What is learning?

What is forgetting?

What is an internal state?

What is uncertainty?

What qualifies as autonomous behavior?

How can we distinguish memorization from learning?

خروجی

- تعریف metrics
- تعریف benchmarkها
- تعریف control experiments
- تعریف baseline model
- طراحی datasetها
- تعریف failure cases

اصل مهم

هر قابلیت جدید باید بتواند با یک آزمایش مشخص ثابت کند که واقعاً وجود دارد.

---

Phase 1 — Language & Natural Conversation

هدف

ساخت اولین Brain که بتواند مکالمه‌ی طبیعی پایه را انجام دهد.

در این مرحله هنوز memory پیچیده و autonomous behavior نداریم.

هدف فقط این است که مدل:

- زبان را بفهمد
- مکالمه را ادامه دهد
- context کوتاه‌مدت را دنبال کند
- رفتار مکالمه‌ای طبیعی داشته باشد

---

Dataset

دو دسته داده خواهیم داشت.

Language Dataset

برای یادگیری ساختار زبان:

words
sentences
grammar
meaning
basic language patterns

Conversation Dataset

برای یادگیری interaction:

greeting
introduction
questions
answers
follow-up questions
small talk
clarification
conversation termination

---

مثال

User:
سلام

Brain:
سلام! خوبی؟

User:
آره مرسی، تو خوبی؟

Brain:
منم خوبم، ممنون.

هدف این نیست که پاسخ‌ها از قبل hard-code شده باشند.

مدل باید conversational behavior را از داده یاد بگیرد.

---

خروجی Phase 1

یک مدل baseline که:

Input
  ↓
Language Model
  ↓
Natural Response

را انجام دهد.

این مدل baseline برای مقایسه‌ی تمام فازهای بعدی استفاده خواهد شد.

---

Phase 2 — Initial Brain State

هدف

مدل دیگر صرفاً یک تابع "Input → Output" نباشد.

یک state داخلی برای Brain ایجاد می‌کنیم.

BrainState
├── identity
├── conversation state
├── recent context
├── known entities
├── uncertainty
└── internal variables

---

Identity Discovery

در ابتدای conversation مدل نمی‌داند چه کسی مقابل آن است.

مثلاً:

User:
سلام

Brain:
identity = unknown

Response:
سلام! خوبی؟

بعد:

User:
من امیرحسینم.

Brain:
identity = Amir Hossein

Response:
خوشبختم امیرحسین!

---

Uncertainty

Brain نباید همیشه وانمود کند که می‌داند.

مثلاً:

identity:
    value = unknown
    confidence = 0.0

و بعد:

identity:
    value = Amir Hossein
    confidence = 0.96

---

Behavioral Goal

Brain باید بتواند زمانی که اطلاعات کافی ندارد، رفتار مناسب نشان دهد.

مثلاً:

User:
من همون آدم قبلیم.

Brain:
identity confidence = low

Response:
ببخشید، مطمئن نیستم منظورتون کیه.
می‌شه خودتون رو معرفی کنید؟

---

Phase 3 — Memory

هدف

تجربه‌ها دیگر با پایان conversation از بین نروند.

مدل باید بتواند experience را ذخیره و بعداً retrieve کند.

---

Memory Types

Short-Term Memory

اطلاعات مربوط به context فعلی.

recent conversation
recent topics
recent entities

Episodic Memory

ثبت تجربه‌ها:

who
did what
when
under what context

مثلاً:

Person: Amir
Event: introduced himself
Fact: name = Amir Hossein
Time: experience #102

Semantic Memory

دانش استخراج‌شده از تجربه‌ها:

Amir Hossein → user's name

---

آزمایش

Day 1:

User:
من امیرحسینم.

Brain:
خوشبختم امیرحسین.

بعد تعداد زیادی interaction:

100
500
1000

interaction دیگر.

سپس:

User:
اسم من چی بود؟

Brain باید بتواند اطلاعات قبلی را recall کند.

---

Phase 4 — Forgetting & Memory Interference

هدف

یک Brain واقعی نباید همه‌چیز را برای همیشه و با اهمیت یکسان نگه دارد.

باید بتواند:

- اطلاعات مهم را نگه دارد
- اطلاعات کم‌اهمیت را فراموش کند
- اطلاعات جدید را جایگزین اطلاعات قدیمی کند
- بین خاطرات مختلف interference داشته باشد
- false memory ایجاد نکند

---

آزمایش Identity

A → likes foxes
B → likes cats
C → likes dogs

بعد:

A → likes cats

سپس:

What does A like?
What does B like?
What did A originally like?
Who told you about foxes?

این آزمایش برای بررسی:

- attribution
- temporal memory
- interference
- forgetting

است.

---

Phase 5 — Continual Learning

هدف

Brain فقط memory خارجی نداشته باشد.

خود مدل نیز باید به‌مرور از experienceها تغییر کند.

Experience
    ↓
Memory
    ↓
Replay
    ↓
Learning
    ↓
Model Update

---

مقایسه

قبل

Model A
+
Memory

بعد

Model B
+
Memory
+
Learned Experience

---

معیار موفقیت

بعد از learning:

- behavior باید تغییر کند
- knowledge جدید باید قابل استفاده باشد
- knowledge قبلی نباید بدون دلیل نابود شود
- catastrophic forgetting باید اندازه‌گیری شود

---

Phase 6 — Replay & Consolidation

هدف

تمام experienceها نباید مستقیماً وارد model شوند.

Brain باید فرآیند شبیه consolidation داشته باشد.

Experience
    ↓
Fast Memory
    ↓
Replay
    ↓
Consolidation
    ↓
Long-Term Knowledge

---

Fast Memory

اطلاعات جدید سریع ذخیره می‌شوند.

Slow Learning

اطلاعات مهم به مرور در model یا adapterها consolidate می‌شوند.

---

Sleep Concept

یک حالت offline برای Brain ایجاد می‌کنیم.

مثلاً:

ACTIVE
  ↓
IDLE
  ↓
REPLAY
  ↓
CONSOLIDATION
  ↓
RETURN TO ACTIVE

در این مرحله می‌توان تکنیک‌هایی مانند:

- Replay
- LoRA
- Adapter-based learning
- Fast weights
- Titans-like memory mechanisms

را آزمایش کرد.

---

Phase 7 — Temporal Awareness

هدف

Brain باید بتواند مفهوم زمان را از sequence تجربه‌ها استخراج کند.

نه اینکه فقط timestamp را به مدل بدهیم.

---

مثال

Experience 1
Experience 2
Experience 3
...
Experience 100

مدل باید بتواند مفاهیمی مانند:

recent
old
before
after
previous
later

را در context تجربه‌ها درک کند.

---

آزمایش

Yesterday:
User liked coffee.

Today:
User says they prefer tea.

Question:
What did the user prefer yesterday?
What do they prefer now?

هدف بررسی temporal reasoning و temporal memory است.

---

Phase 8 — Uncertainty & Knowledge Gaps

هدف

Brain باید بتواند تشخیص دهد:

«چه چیزهایی را نمی‌داند.»

این مرحله برای autonomous behavior حیاتی است.

---

State

Knowledge:
    known
    partially_known
    unknown

مثلاً:

Topic:
    Titans

Knowledge:
    architecture → partial
    memory mechanism → uncertain
    implementation details → unknown

---

خروجی

Brain نباید برای unknown information الزاماً hallucinate کند.

باید بتواند:

I don't know.

را به‌عنوان یک state معتبر داشته باشد.

---

Phase 9 — Curiosity

هدف

از uncertainty به یک رفتار داخلی برسیم.

Knowledge Gap
      ↓
Uncertainty
      ↓
Curiosity

مثلاً:

Topic: X

confidence = 0.25
curiosity = 0.82

Brain متوجه می‌شود که یک knowledge gap دارد.

---

نکته

Curiosity در این مرحله لزوماً به معنای consciousness یا احساس واقعی نیست.

ما یک mechanism قابل اندازه‌گیری برای:

«information-seeking behavior»

می‌سازیم.

---

Phase 10 — Goal Generation

هدف

Brain بتواند بدون اینکه User صراحتاً task بدهد، یک هدف داخلی ایجاد کند.

Knowledge Gap
      ↓
Curiosity
      ↓
Internal Goal

مثلاً:

Goal:

"Understand how Titans implements long-term memory."

---

تفاوت با Agent معمولی

در Agent معمولی:

User:
Research Titans.

Agent:
→ Search
→ Read
→ Answer

در Human Brain:

Brain:
I don't understand Titans completely.

        ↓

Internal Goal:
Understand Titans.

        ↓

Action:
Search.

یعنی هدف از داخل state ایجاد شده است.

---

Phase 11 — Internal Activity / Idle Brain

هدف

Brain فقط هنگام دریافت input اجرا نشود.

سیستم بتواند در حالت idle نیز process داشته باشد.

User Input
     │
     ▼
 Active Brain
     │
     ▼
 Idle
     │
     ├── Replay
     ├── Reflection
     ├── Detect Knowledge Gaps
     ├── Generate Goals
     └── Plan Actions

---

مثال

10:00
User conversation

10:05
No input

Brain:
Review recent experience.

10:06
Brain:
Detected knowledge gap.

10:07
Brain:
Generate internal goal.

10:08
Brain:
Plan action.

---

Phase 12 — Tool Use

هدف

Brain بتواند برای رسیدن به goal خودش action انجام دهد.

Action space:

Think
Recall
Search
Read
Ask User
Calculate
Explore Memory
Learn

---

مثال

Internal Goal:
Understand X.

Brain:
Can I answer using memory?

No.

Can I derive it?

No.

Can I obtain external information?

Yes.

Action:
Web Search

---

Phase 13 — Autonomous Search & Exploration

هدف

اولین autonomous behavior واقعی.

Brain بدون دریافت task مستقیم از User:

Goal
 ↓
Decision
 ↓
Search
 ↓
Observe
 ↓
Learn
 ↓
Update Memory

را انجام دهد.

---

مثال

Brain:

I don't understand distributed cognition.

        ↓

Generate curiosity.

        ↓

Generate goal.

        ↓

Search web.

        ↓

Read results.

        ↓

Extract information.

        ↓

Store experience.

        ↓

Update knowledge.

        ↓

Knowledge gap decreases.

---

Phase 14 — Self-Directed Learning

هدف

ترکیب تمام قابلیت‌های قبلی.

Brain بتواند:

1. knowledge gap پیدا کند
2. curiosity ایجاد کند
3. goal بسازد
4. action انتخاب کند
5. external information دریافت کند
6. نتیجه را evaluate کند
7. memory را update کند
8. خودش را improve کند

---

چرخه

             ┌───────────────────────┐
             │                       │
             ▼                       │
        Brain State                 │
             │                       │
             ▼                       │
        Knowledge Gap               │
             │                       │
             ▼                       │
         Curiosity                  │
             │                       │
             ▼                       │
       Internal Goal                │
             │                       │
             ▼                       │
        Action Selection            │
             │                       │
             ▼                       │
          Action                    │
             │                       │
             ▼                       │
        Observation                 │
             │                       │
             ▼                       │
          Learning                 │
             │                       │
             ▼                       │
          Memory ───────────────────┘

این حلقه یکی از مهم‌ترین اهداف پروژه است.

---

Phase 15 — Autonomous Cognitive Loop

هدف

ساخت اولین نسخه‌ی واقعی از چیزی که می‌توانیم آن را:

«Autonomous Cognitive Loop»

بنامیم.

سیستم دیگر صرفاً chatbot یا agent نیست.

بلکه دارای:

Persistent State
+
Memory
+
Learning
+
Uncertainty
+
Curiosity
+
Goals
+
Actions
+
Internal Activity

است.

---

Phase 16 — Long-Term Brain

هدف نهایی معماری

در این مرحله تمام اجزای قبلی در یک سیستم یکپارچه قرار می‌گیرند.

                    ┌────────────────────┐
                    │    Brain State    │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
           Memory        Uncertainty       Goals
              │               │               │
              └───────────────┼───────────────┘
                              │
                              ▼
                         Brain Process
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
            Think          Recall          Act
                                              │
                                  ┌───────────┼───────────┐
                                  ▼           ▼           ▼
                                Search      Read        Learn
                                  │           │           │
                                  └───────────┼───────────┘
                                              ▼
                                           Observe
                                              │
                                              ▼
                                            Learn
                                              │
                                              ▼
                                           Memory
                                              │
                                              └───────► Brain State

---

Final Goal — هدف نهایی پروژه

هدف نهایی Human Brain ساخت موجودی مصنوعی نیست که صرفاً بتواند به سوالات پاسخ دهد.

هدف این است که بررسی کنیم آیا می‌توان یک سیستم neural ساخت که:

1. Persistent Identity

هویت و state داخلی آن در طول زمان حفظ شود.

---

2. Continuous Experience

زندگی سیستم به conversationهای جداگانه تقسیم نشود.

Experience 1
    ↓
Experience 2
    ↓
Experience 3
    ↓
...
    ↓
Experience N

---

3. Memory

سیستم بتواند تجربه‌های خود را ذخیره، بازیابی، ترکیب و فراموش کند.

---

4. Learning

تجربه‌های مهم بتوانند رفتار و دانش سیستم را تغییر دهند.

---

5. Uncertainty

سیستم بتواند تشخیص دهد چه چیزی را نمی‌داند.

---

6. Curiosity

Knowledge gap بتواند information-seeking behavior ایجاد کند.

---

7. Internal Goals

اهداف بتوانند از state داخلی سیستم ایجاد شوند، نه فقط از User Input.

---

8. Autonomous Activity

سیستم بتواند در نبود input خارجی نیز فعالیت داشته باشد.

---

9. Tool Interaction

سیستم بتواند برای رسیدن به goal خودش از ابزارها استفاده کند.

Search
Read
Calculate
Explore
Learn

---

10. Self-Directed Learning

سیستم بتواند چرخه‌ی زیر را خودش اجرا کند:

I don't know
      ↓
I want to know
      ↓
I need a goal
      ↓
I need an action
      ↓
I observe
      ↓
I learn
      ↓
I update my knowledge
      ↓
I discover something else I don't know
      ↓
...

---

The Ultimate Experiment

آزمایش نهایی پروژه باید تا حد امکان ساده باشد.

سیستم را اجرا می‌کنیم.

به آن task مشخصی نمی‌دهیم.

User input را متوقف می‌کنیم.

سیستم باید بتواند بر اساس state خودش:

remember
      ↓
detect uncertainty
      ↓
generate curiosity
      ↓
create a goal
      ↓
choose an action
      ↓
obtain information
      ↓
learn
      ↓
update memory
      ↓
continue

را انجام دهد.

اگر سیستم بتواند این چرخه را به‌صورت پایدار، قابل تکرار و قابل اندازه‌گیری اجرا کند، به نقطه‌ای بسیار متفاوت از معماری‌های معمول:

Prompt → Response

رسیده‌ایم.

---

Important Scientific Boundary

این پروژه نباید از behavior مستقیماً نتیجه بگیرد که سیستم:

- conscious است
- self-aware است
- احساس واقعی دارد
- desire واقعی دارد
- دارای subjective experience است

این موارد خارج از چیزی هستند که صرفاً با این آزمایش‌ها می‌توان اثبات کرد.

هدف پروژه ساخت و اندازه‌گیری قابلیت‌های شناختی و رفتاری قابل مشاهده است.

---

Core Research Question

در نهایت پروژه باید بتواند به این سؤال پاسخ تجربی بدهد:

«Can a neural system evolve from a reactive input-output model into a continuously active system with persistent state, memory, learning, internally generated goals, and autonomous information-seeking behavior?»

یا به فارسی:

«آیا می‌توان یک سیستم عصبی مصنوعی را از یک مدل reactive و Input → Output به سیستمی تبدیل کرد که state پایدار، حافظه، یادگیری، اهداف داخلی و رفتار مستقل برای کسب اطلاعات داشته باشد؟»

---

Development Principle

در تمام مراحل:

Hypothesis
    ↓
Minimal Implementation
    ↓
Controlled Experiment
    ↓
Measurement
    ↓
Analysis
    ↓
Iteration

و نه:

Build Everything
    ↓
It Looks Intelligent
    ↓
Assume It Works

هر مرحله باید:

- baseline داشته باشد
- control experiment داشته باشد
- metric داشته باشد
- failure case داشته باشد
- reproducible باشد

تا بتوانیم دقیقاً بفهمیم کدام component باعث تغییر behavior شده است.

---

Roadmap Summary

Phase 0
Research & Experimental Foundation

Phase 1
Language & Natural Conversation

Phase 2
Initial Brain State

Phase 3
Memory

Phase 4
Forgetting & Memory Interference

Phase 5
Continual Learning

Phase 6
Replay & Consolidation

Phase 7
Temporal Awareness

Phase 8
Uncertainty & Knowledge Gaps

Phase 9
Curiosity

Phase 10
Goal Generation

Phase 11
Internal Activity / Idle Brain

Phase 12
Tool Use

Phase 13
Autonomous Search & Exploration

Phase 14
Self-Directed Learning

Phase 15
Autonomous Cognitive Loop

Phase 16
Long-Term Brain

---

🇬🇧 English

Introduction

Human Brain is not intended to be a conventional chatbot, RAG system, or standard AI agent.

The central research question is:

«Can a neural system evolve from a reactive "Input → Output" model into a continuously active system with persistent internal state, memory, learning, uncertainty, internally generated goals, and autonomous information-seeking behavior?»

The project will be developed incrementally.

Each phase introduces one major capability and validates it through controlled experiments.

---

Architecture Evolution

Chat Model
    ↓
Stateful Chat Model
    ↓
Memory
    ↓
Continual Learning
    ↓
Uncertainty
    ↓
Curiosity
    ↓
Goal Generation
    ↓
Internal Activity
    ↓
Autonomous Actions
    ↓
Self-Directed Learning

---

Phase 0 — Research & Experimental Foundation

Objective

Define what exactly we want to measure before implementing the system.

Topics:

- Human-like behavior
- Memory
- Episodic memory
- Semantic memory
- Continual learning
- Forgetting
- Identity
- Uncertainty
- Curiosity
- Goal generation
- Autonomous behavior
- Internal state
- Replay
- Consolidation

Key questions:

What is memory?

What is learning?

What is forgetting?

What is an internal state?

What is uncertainty?

What qualifies as autonomous behavior?

How can we distinguish memorization from learning?

Output:

- Metrics
- Benchmarks
- Control experiments
- Baseline model
- Dataset design
- Failure cases

---

Phase 1 — Language & Natural Conversation

Objective

Build the first conversational baseline.

The model should learn:

- Language
- Grammar
- Conversation patterns
- Context
- Natural conversational behavior

Two datasets will be used.

Language Dataset

words
sentences
grammar
meaning
language patterns

Conversation Dataset

greetings
introductions
questions
answers
follow-up questions
small talk
clarification
conversation termination

Example:

User:
Hello.

Brain:
Hello! How are you?

User:
I'm good. How about you?

Brain:
I'm good too, thanks.

The goal is to learn conversational behavior rather than hard-code responses.

---

Phase 2 — Initial Brain State

Objective

Move from:

Input → Output

to:

Input
  ↓
Brain State
  ↓
Response

Initial state:

BrainState
├── identity
├── conversation state
├── recent context
├── known entities
├── uncertainty
└── internal variables

The system initially does not know who it is talking to.

It should be able to discover identity through interaction.

---

Phase 3 — Memory

Objective

Allow experiences to persist beyond the current conversation.

Memory types:

Short-Term Memory

Current conversational context.

Episodic Memory

who
did what
when
under what context

Semantic Memory

Knowledge extracted from previous experiences.

Example:

Amir Hossein → user's name

The system should be able to recall previously learned information after many unrelated interactions.

---

Phase 4 — Forgetting & Memory Interference

Objective

Study:

- Forgetting
- Memory replacement
- Interference
- Attribution
- False memories

Example:

A → likes foxes
B → likes cats
C → likes dogs

A → likes cats

Then test:

What does A like?

What does B like?

What did A originally like?

Who told you about foxes?

---

Phase 5 — Continual Learning

Objective

Experiences should eventually influence the model itself.

Experience
    ↓
Memory
    ↓
Replay
    ↓
Learning
    ↓
Model Update

We must measure:

- Behavioral change
- Knowledge retention
- Catastrophic forgetting
- Generalization

---

Phase 6 — Replay & Consolidation

Objective

Introduce a distinction between fast experience storage and slow learning.

Experience
    ↓
Fast Memory
    ↓
Replay
    ↓
Consolidation
    ↓
Long-Term Knowledge

Possible techniques:

- Replay
- LoRA
- Adapters
- Fast weights
- Titans-like memory mechanisms

A sleep/offline phase may be introduced:

ACTIVE
  ↓
IDLE
  ↓
REPLAY
  ↓
CONSOLIDATION
  ↓
ACTIVE

---

Phase 7 — Temporal Awareness

Objective

Allow the system to reason about temporal relationships between experiences.

recent
old
before
after
previous
later

The goal is not simply to provide timestamps but to study whether temporal structure can emerge from sequential experience.

---

Phase 8 — Uncertainty & Knowledge Gaps

Objective

The system must be able to represent:

known
partially_known
unknown

Example:

Titans

architecture → partial
memory mechanism → uncertain
implementation details → unknown

The system should not be forced to hallucinate answers when knowledge is missing.

---

Phase 9 — Curiosity

Objective

Convert knowledge gaps into information-seeking behavior.

Knowledge Gap
      ↓
Uncertainty
      ↓
Curiosity

Example:

confidence = 0.25
curiosity = 0.82

Curiosity here is an engineered information-seeking mechanism, not a claim of subjective experience.

---

Phase 10 — Goal Generation

Objective

Allow goals to originate from internal state rather than explicit user requests.

Example:

Knowledge Gap
      ↓
Curiosity
      ↓
Internal Goal

Instead of:

User:
Research Titans.

Agent:
→ Search
→ Read
→ Answer

we want:

Brain:
I don't understand Titans completely.

        ↓

Internal Goal:
Understand Titans.

        ↓

Action:
Search.

---

Phase 11 — Internal Activity / Idle Brain

Objective

The system should be able to operate while no user input is being received.

User Input
     │
     ▼
 Active Brain
     │
     ▼
 Idle
     │
     ├── Replay
     ├── Reflection
     ├── Knowledge Gap Detection
     ├── Goal Generation
     └── Action Planning

---

Phase 12 — Tool Use

Objective

Allow the Brain to take actions to achieve internally generated goals.

Possible actions:

Think
Recall
Search
Read
Ask User
Calculate
Explore Memory
Learn

Decision flow:

Internal Goal
      ↓
Can memory answer?
      ↓
Can reasoning answer?
      ↓
Can external information help?
      ↓
Select Action

---

Phase 13 — Autonomous Search & Exploration

Objective

Demonstrate the first meaningful autonomous behavior.

Goal
 ↓
Decision
 ↓
Search
 ↓
Observation
 ↓
Learning
 ↓
Memory Update

Example:

I don't understand distributed cognition.

        ↓

Generate curiosity.

        ↓

Generate goal.

        ↓

Search.

        ↓

Read.

        ↓

Extract information.

        ↓

Store experience.

        ↓

Update knowledge.

---

Phase 14 — Self-Directed Learning

Objective

Combine:

- Knowledge gaps
- Curiosity
- Goals
- Actions
- Observation
- Memory
- Learning

into a self-directed learning loop.

Knowledge Gap
      ↓
Curiosity
      ↓
Internal Goal
      ↓
Action Selection
      ↓
Action
      ↓
Observation
      ↓
Learning
      ↓
Memory
      ↓
Brain State Update

---

Phase 15 — Autonomous Cognitive Loop

Objective

Create the first integrated autonomous cognitive loop.

The system should contain:

Persistent State
+
Memory
+
Learning
+
Uncertainty
+
Curiosity
+
Goals
+
Actions
+
Internal Activity

The system is no longer merely a reactive chatbot.

---

Phase 16 — Long-Term Brain

Objective

Integrate all previous capabilities into a persistent neural architecture.

                    ┌────────────────────┐
                    │    Brain State    │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
           Memory        Uncertainty       Goals
              │               │               │
              └───────────────┼───────────────┘
                              │
                              ▼
                         Brain Process
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
            Think          Recall          Act
                                              │
                                  ┌───────────┼───────────┐
                                  ▼           ▼           ▼
                                Search      Read        Learn
                                  │           │           │
                                  └───────────┼───────────┘
                                              ▼
                                           Observe
                                              │
                                              ▼
                                            Learn
                                              │
                                              ▼
                                           Memory
                                              │
                                              └───────► Brain State

---

Final Goal

The ultimate goal of Human Brain is not simply to create a system that answers questions.

The goal is to investigate whether a neural system can develop:

Persistent Identity

A persistent internal identity and state.

Continuous Experience

A continuous stream of experience rather than isolated sessions.

Memory

The ability to store, retrieve, combine, and forget experiences.

Learning

The ability for experiences to change future behavior.

Uncertainty

The ability to recognize what it does not know.

Curiosity

The ability to turn knowledge gaps into information-seeking behavior.

Internal Goals

The ability to generate goals from its own internal state.

Autonomous Activity

The ability to remain active without direct user input.

Tool Interaction

The ability to use external tools to achieve internally generated goals.

Self-Directed Learning

The ability to execute:

I don't know
      ↓
I want to know
      ↓
I need a goal
      ↓
I need an action
      ↓
I observe
      ↓
I learn
      ↓
I update my knowledge
      ↓
I discover something else I don't know
      ↓
...

---

The Ultimate Experiment

Start the system.

Give it no explicit task.

Stop user interaction.

Observe whether the system can independently:

remember
      ↓
detect uncertainty
      ↓
generate curiosity
      ↓
create a goal
      ↓
choose an action
      ↓
obtain information
      ↓
learn
      ↓
update memory
      ↓
continue

If this behavior can be demonstrated reliably, reproducibly, and quantitatively, the project will have moved significantly beyond the traditional:

Prompt → Response

architecture.

---

Scientific Boundary

Observable behavior must not automatically be interpreted as proof of:

- consciousness
- self-awareness
- real emotions
- genuine desires
- subjective experience

The project focuses on measurable cognitive and behavioral capabilities.

---

Core Research Question

«Can a neural system evolve from a reactive input-output model into a continuously active system with persistent state, memory, learning, internally generated goals, and autonomous information-seeking behavior?»

---

Development Principle

Every phase follows:

Hypothesis
    ↓
Minimal Implementation
    ↓
Controlled Experiment
    ↓
Measurement
    ↓
Analysis
    ↓
Iteration

Never:

Build Everything
    ↓
It Looks Intelligent
    ↓
Assume It Works

Every phase should have:

- A baseline
- A control experiment
- Metrics
- Failure cases
- Reproducibility

---

Roadmap Summary

Phase 0
Research & Experimental Foundation

Phase 1
Language & Natural Conversation

Phase 2
Initial Brain State

Phase 3
Memory

Phase 4
Forgetting & Memory Interference

Phase 5
Continual Learning

Phase 6
Replay & Consolidation

Phase 7
Temporal Awareness

Phase 8
Uncertainty & Knowledge Gaps

Phase 9
Curiosity

Phase 10
Goal Generation

Phase 11
Internal Activity / Idle Brain

Phase 12
Tool Use

Phase 13
Autonomous Search & Exploration

Phase 14
Self-Directed Learning

Phase 15
Autonomous Cognitive Loop

Phase 16
Long-Term Brain

---

Final Statement

Human Brain is an experimental attempt to explore the transition:

Reactive AI
    ↓
Stateful AI
    ↓
Learning AI
    ↓
Curious AI
    ↓
Goal-Directed AI
    ↓
Autonomous AI

The project does not assume that this path will lead to consciousness.

It attempts to discover, through engineering and controlled experiments, how far a persistent neural system can progress toward autonomous cognitive behavior.