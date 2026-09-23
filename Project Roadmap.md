# Human Brain — Project Roadmap

## Research Goal

هدف پروژه ساخت یک chatbot بهتر نیست.

هدف ساخت یک **continuous neural system** است که بتواند:

* تجربه دریافت کند
* state داخلی داشته باشد
* memory تشکیل دهد
* فراموش کند
* از تجربه یاد بگیرد
* uncertainty داشته باشد
* curiosity ایجاد کند
* goal بسازد
* بدون input خارجی فعالیت داخلی داشته باشد
* گاهی پاسخ ندهد
* در زمان مناسب action انجام دهد
* و در طول زمان رفتار خود را تغییر دهد

اصل بنیادی:

```text
Input is a stimulus, not a command.

Output is a choice, not a requirement.

No Input does not mean No Activity.

Idle is not inactivity.

Session is not Life.

Memory is part of the Brain.

Goal is not necessarily a User Request.

Action should emerge from the internal state of the Brain.
```

---

# Phase 0 — Research Foundation

## Goal

ساخت foundation برای آزمایش‌های reproducible.

## Tasks

* [ ] تعریف Research Question
* [ ] تعریف Research Constraints
* [ ] تعریف Experimental Protocol
* [ ] ساخت project structure
* [ ] ساخت configuration system
* [ ] ساخت seed management
* [ ] ساخت experiment runner
* [ ] ساخت checkpoint system
* [ ] ساخت metrics system
* [ ] ساخت evaluation harness
* [ ] ساخت baseline framework
* [ ] ساخت control-model framework
* [ ] ساخت ablation framework
* [ ] تعریف logging
* [ ] تعریف experiment artifacts
* [ ] تعریف reproducibility rules
* [ ] تعریف CPU training pipeline

## Success Criteria

* [ ] یک experiment از ابتدا تا انتها reproducibly اجرا شود.
* [ ] نتایج experiment قابل ذخیره و مقایسه باشند.
* [ ] بتوانیم Baseline / Control / Ablation را جداگانه اجرا کنیم.

---

# Phase 1 — Persian Language Brain

## Goal

ساخت کوچک‌ترین Brain زبانی قابل استفاده.

## Dataset

* [ ] Persian text normalization
* [ ] TinyStories-Farsi preprocessing
* [ ] Persian general corpus preprocessing
* [ ] Conversation dataset اولیه
* [ ] Dataset cleaning
* [ ] Deduplication
* [ ] Dataset filtering
* [ ] Dataset mixing
* [ ] Train / validation / test split
* [ ] Dataset statistics

## Tokenizer

* [ ] Unicode normalization
* [ ] Persian character normalization
* [ ] ZWNJ handling
* [ ] punctuation normalization
* [ ] BPE / Unigram tokenizer
* [ ] Vocabulary ~8K–16K
* [ ] tokenizer evaluation

## Model

Target:

```text
~5M – 10M parameters
```

* [ ] Transformer implementation
* [ ] 5M baseline
* [ ] 10M baseline
* [ ] CPU training
* [ ] checkpointing
* [ ] validation
* [ ] generation

## Evaluation

* [ ] Perplexity
* [ ] Persian language probes
* [ ] Text continuation
* [ ] Basic coherence
* [ ] Basic conversation probes

## Success Criteria

```text
Brain can generate basic Persian text.
```

در این Phase هنوز Memory و Autonomy نداریم.

---

# Phase 2 — Continuous Core

## Goal

Brain دیگر در هر interaction از صفر شروع نکند.

## Tasks

* [ ] Persistent neural state
* [ ] State representation
* [ ] State initialization
* [ ] State update mechanism
* [ ] State serialization
* [ ] State persistence
* [ ] Continuous execution
* [ ] No-session execution
* [ ] `step(observation)`
* [ ] `step(None)`
* [ ] State drift experiment
* [ ] Reset vs No-reset experiment

## Success Criteria

بررسی شود که:

```text
Brain(t + 1)
```

واقعاً به:

```text
Brain(t)
```

وابسته است.

---

# Phase 3 — Episodic Memory

## Goal

Brain بتواند تجربه‌های قبلی را نگه دارد و دوباره فعال کند.

## Tasks

* [ ] Memory interface
* [ ] Neural memory baseline
* [ ] Episodic memory representation
* [ ] Memory write
* [ ] Memory retrieval
* [ ] Memory strength
* [ ] Temporal association
* [ ] Experience representation
* [ ] Person representation
* [ ] Memory integration with core state

## Experiments

* [ ] Single-event recall
* [ ] Delayed recall
* [ ] Poetry recall
* [ ] Cross-person recall
* [ ] Unrelated-cue recall
* [ ] Memory retrieval accuracy

## Success Criteria

Memory باید بخشی از Brain باشد، نه یک external database.

---

# Phase 4 — Forgetting & Interference

## Goal

Memory واقعی باید بتواند ضعیف شود و تحت تأثیر تجربه‌های جدید قرار بگیرد.

## Tasks

* [ ] Memory decay
* [ ] Memory strength update
* [ ] Competing memories
* [ ] Interference
* [ ] Controlled forgetting
* [ ] Memory replacement
* [ ] False-memory detection

## Evaluation

* [ ] Retention curves
* [ ] Interference experiments
* [ ] False-memory probes
* [ ] Confabulation probes
* [ ] Recall degradation measurement

---

# Phase 5 — Continual Learning

## Goal

تجربه باید بتواند رفتار Brain را تغییر دهد.

## Tasks

* [ ] Online learning
* [ ] Experience-based learning
* [ ] Learning without reset
* [ ] Continual training
* [ ] Checkpoint comparison
* [ ] Behavior-change measurement
* [ ] New knowledge acquisition
* [ ] Old knowledge retention
* [ ] Catastrophic forgetting measurement

## Controls

* [ ] No-learning control
* [ ] Frozen-model control
* [ ] Ablation

## Success Criteria

```text
Experience
    ↓
Learning
    ↓
Behavior Change
```

---

# Phase 6 — Sleep & Consolidation

## Goal

Brain در زمان Idle بتواند تجربه‌ها را replay و consolidate کند.

## Tasks

* [ ] Idle state
* [ ] Sleep state
* [ ] Replay buffer
* [ ] Replay mechanism
* [ ] Replay policy
* [ ] Consolidation mechanism
* [ ] Slow memory / adapter
* [ ] Wake state
* [ ] Sleep → Wake transition

## Lifecycle

```text
AWAKE
  ↓
IDLE
  ↓
SLEEP
  ↓
REPLAY
  ↓
CONSOLIDATE
  ↓
AWAKE
```

## Experiments

* [ ] Wake-only baseline
* [ ] Sleep-enabled model
* [ ] Long-term retention
* [ ] Catastrophic forgetting
* [ ] Replay effectiveness

---

# Phase 7 — Temporal Brain

## Goal

Brain بتواند زمان و ترتیب تجربه‌ها را از جریان تجربه یاد بگیرد.

## Tasks

* [ ] Temporal state
* [ ] Temporal context
* [ ] Temporal drift
* [ ] Recency representation
* [ ] Sequence ordering
* [ ] Before / after representation
* [ ] Elapsed-time representation

## Experiments

* [ ] Order probe
* [ ] Recency probe
* [ ] Before / after probe
* [ ] Delayed retrieval
* [ ] Long-gap experiment

## Success Criteria

Brain بتواند تفاوت بین:

```text
A happened before B
```

و:

```text
B happened before A
```

را یاد بگیرد.

---

# Phase 8 — Uncertainty

## Goal

Brain بتواند تشخیص دهد که چه چیزی را می‌داند و چه چیزی را نمی‌داند.

## Tasks

* [ ] Uncertainty representation
* [ ] Confidence estimation
* [ ] Knowledge-gap representation
* [ ] Known / Unknown state
* [ ] Partial knowledge
* [ ] Uncertainty persistence
* [ ] Calibration

## Evaluation

* [ ] Known-answer probes
* [ ] Unknown-answer probes
* [ ] Partial-information probes
* [ ] Calibration metrics

## Target Behavior

```text
I know.
I partially know.
I don't know.
```

---

# Phase 9 — Curiosity

## Goal

Knowledge gap بتواند به یک internal signal تبدیل شود.

## Tasks

* [ ] Novelty representation
* [ ] Curiosity signal
* [ ] Information-gap signal
* [ ] Intrinsic reward
* [ ] Curiosity persistence
* [ ] Curiosity decay
* [ ] Curiosity ablation

## Core Hypothesis

```text
Knowledge Gap
      ↓
Curiosity
```

## Evaluation

* [ ] Novelty experiment
* [ ] Information-gap experiment
* [ ] Curiosity vs random exploration
* [ ] Curiosity ablation

---

# Phase 10 — Internal Goals

## Goal

Brain بتواند از internal state خودش Goal تولید کند.

## Tasks

* [ ] Goal representation
* [ ] Goal creation
* [ ] Goal persistence
* [ ] Goal priority
* [ ] Goal interruption
* [ ] Goal completion
* [ ] Unresolved-goal memory
* [ ] Goal decay
* [ ] Goal ablation

## Target Flow

```text
Question
    ↓
Knowledge Gap
    ↓
Curiosity
    ↓
Internal Goal
```

Goal نباید صرفاً برابر با User Request باشد.

---

# Phase 11 — Internal Activity

## Goal

اثبات اینکه Brain بدون input خارجی هم می‌تواند فعالیت داخلی داشته باشد.

## Tasks

* [ ] Internal tick
* [ ] `step(None)`
* [ ] Idle processing
* [ ] Internal state transitions
* [ ] Memory replay during idle
* [ ] Goal activation during idle
* [ ] Reflection
* [ ] Delayed action
* [ ] Spontaneous output
* [ ] Silence as valid action

## Required Behaviors

### Input → Output

```text
Input
  ↓
Brain
  ↓
Output
```

### Input → Nothing

```text
Input
  ↓
Brain
  ↓
Nothing
```

### No Input → Output

```text
No Input
   ↓
Internal Activity
   ↓
Brain
   ↓
Output
```

## Success Criteria

```text
No Input
   ≠
No Activity
```

---

# Phase 12 — Body

## Goal

Brain بتواند با یک environment تعامل کند.

## Tasks

* [ ] Body interface
* [ ] Observation interface
* [ ] Action interface
* [ ] Action result
* [ ] Environment interface
* [ ] Permission boundary
* [ ] Simulated environment
* [ ] Brain / Body separation

## Rule

در این Phase هنوز ابزارهای واقعی مثل Web Search وارد نمی‌شوند.

---

# Phase 13 — Autonomous Exploration

## Goal

Brain بتواند بر اساس Goal و Curiosity خودش exploration انجام دهد.

## Tasks

* [ ] Action selection
* [ ] Goal → Action
* [ ] Action → Observation
* [ ] Observation → Learning
* [ ] Exploration loop
* [ ] Curiosity-driven exploration
* [ ] Exploration memory

## Core Loop

```text
Goal
  ↓
Action
  ↓
Observation
  ↓
Learning
  ↓
Memory
  ↓
New Goal
```

---

# Phase 14 — Tools

## Goal

Tool را به عنوان یک Action واقعی وارد Brain کنیم.

## Tasks

* [ ] Tool interface
* [ ] Tool registry
* [ ] Tool selection
* [ ] Tool permissions
* [ ] Tool invocation
* [ ] Tool result observation
* [ ] Tool failure handling
* [ ] Tool result memory
* [ ] Tool-result learning

## Example

```text
Knowledge Gap
      ↓
Goal
      ↓
Action Selection
      ↓
Search
      ↓
Observation
      ↓
Learning
      ↓
Memory
```

Tool هدف نیست.

Tool فقط یک Action در اختیار Brain است.

---

# Phase 15 — Self-Directed Learning

## Goal

Brain بتواند خودش تشخیص دهد که چه چیزی ارزش یادگیری دارد.

## Tasks

* [ ] Knowledge-gap driven learning
* [ ] Curiosity-driven research
* [ ] Autonomous learning goals
* [ ] Learning prioritization
* [ ] Research action
* [ ] Knowledge integration
* [ ] Memory integration
* [ ] Knowledge retention
* [ ] Self-directed experiments

## Example

```text
Day 1

User:
"چطوری می‌دونی عشق چیه؟"

        ↓

Knowledge Gap
        ↓
Curiosity
        ↓
Internal Goal
        ↓
Research
        ↓
Learning
        ↓
Memory
```

چند روز بعد:

```text
Person Representation
        ↓
Memory Activation
        ↓
Previous Goal
        ↓
Previous Learning
        ↓
Potential Spontaneous Interaction
```

هدف، hard-code کردن جمله‌ای مثل:

```text
"راستی امیر..."
```

نیست.

هدف ایجاد معماری‌ای است که بتواند چنین رفتاری را به صورت emergent تولید کند.

---

# Phase 16 — Autonomous Cognitive Loop

## Goal

تمام subsystemها در یک continuous cognitive loop قرار بگیرند.

```text
              WORLD
                ↓
           EXPERIENCE
                ↓
             BRAIN
                │
        ┌───────┼────────┐
        ↓       ↓        ↓
      STATE   MEMORY   TIME
        │       │        │
        └───────┼────────┘
                ↓
          UNCERTAINTY
                ↓
            CURIOSITY
                ↓
              GOAL
                ↓
             POLICY
                ↓
        THINK / SPEAK /
        ACT / SILENCE
                ↓
              BODY
                ↓
              WORLD
                ↓
           EXPERIENCE
```

## Tasks

* [ ] Continuous loop
* [ ] Long-running execution
* [ ] Persistent memory
* [ ] Persistent state
* [ ] Internal activity
* [ ] Autonomous goals
* [ ] Autonomous learning
* [ ] Action selection
* [ ] Silence decision
* [ ] Spontaneous interaction
* [ ] Long-horizon evaluation

## Controls

* [ ] Memory ablation
* [ ] Curiosity ablation
* [ ] Goal ablation
* [ ] Internal-activity ablation
* [ ] Temporal-state ablation

---

# Phase 17 — Long-Term Brain

## Goal

آزمایش Brain در بازه‌های طولانی.

## Tasks

* [ ] Days-long continuous experiment
* [ ] Weeks-long continuous experiment
* [ ] Persistent identity representation
* [ ] Long-term memory
* [ ] Controlled forgetting
* [ ] Long-term goals
* [ ] Autonomous learning
* [ ] Spontaneous interaction
* [ ] Stability evaluation
* [ ] Memory quality evaluation
* [ ] Language degradation evaluation
* [ ] Behavioral consistency evaluation

---

# Final Research Experiment

در نهایت Brain باید بتواند چنین lifecycleای داشته باشد:

```text
Start Brain
     ↓
Continuous Experience
     ↓
Observe
     ↓
Remember
     ↓
Learn
     ↓
Detect Uncertainty
     ↓
Curiosity
     ↓
Generate Goal
     ↓
Internal Activity
     ↓
Wait / Think / Stay Silent
     ↓
Take Action
     ↓
Observe Result
     ↓
Learn
     ↓
Update Memory
     ↓
Continue
```

و مهم‌تر از همه:

```text
Input ≠ Output
```

```text
No Input ≠ No Activity
```

```text
Silence = Valid Behavior
```

```text
Idle ≠ Inactive
```

```text
Session ≠ Life
```

```text
Goal ≠ User Request
```

---

# Experimental Rules

هر قابلیت جدید باید با این چرخه توسعه داده شود:

```text
Hypothesis
    ↓
Minimal Implementation
    ↓
Test
    ↓
Experiment
    ↓
Control
    ↓
Ablation
    ↓
Metrics
    ↓
Analysis
    ↓
Iteration
```

برای هر قابلیت مهم:

* [ ] Baseline تعریف شود.
* [ ] Control تعریف شود.
* [ ] Ablation تعریف شود.
* [ ] Metrics تعریف شود.
* [ ] Failure cases ثبت شوند.
* [ ] Experiment reproducible باشد.

---

# Dataset Strategy

## Initial Training Data

```text
TinyStories-Farsi       ~40%
Persian General Corpus ~40%
Conversation Data       ~20%
```

این نسبت‌ها hypothesis اولیه هستند.

## Initial Training Target

```text
Model:
~10M parameters

Tokens:
~10M – 30M

Context:
256 – 512

Tokenizer:
8K – 16K vocabulary

Hardware:
CPU
```

## Important Constraint

Dataset نباید رفتارهایی را که قرار است بعداً به عنوان قابلیت معماری آزمایش کنیم، مستقیماً به مدل آموزش دهد.

به‌خصوص:

* Memory
* Curiosity
* Goal generation
* Autonomous activity
* Autonomous search
* Spontaneous interaction

این‌ها باید در architecture و experiments بررسی شوند.

---

# Final Success Criterion

معیار اصلی موفقیت پروژه این نیست که:

```text
Model is a good chatbot.
```

بلکه این است:

```text
Can a small neural system evolve from

Input → Output

into

Experience
   ↓
State
   ↓
Memory
   ↓
Time
   ↓
Uncertainty
   ↓
Curiosity
   ↓
Goal
   ↓
Internal Activity
   ↓
Action / Silence
   ↓
New Experience
```

به شکلی که این رفتارها قابل مشاهده، اندازه‌گیری، تکرار و مقایسه باشند.

هدف نهایی:

> ساخت یک continuous neural system که بتواند در طول زمان تجربه کند، state خود را حفظ کند، یاد بگیرد، فراموش کند، هدف ایجاد کند، در نبود input فعالیت داخلی داشته باشد و رفتارهای جدید را از تعامل میان state، memory، temporal context، uncertainty، curiosity و learning ایجاد کند.
