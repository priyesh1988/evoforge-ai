# 🚀 EvoForge AI

**AI-powered product enhancement orchestration** that learns from real user behavior, recommends the next best product improvements, simulates future versions, and shows likely user impact **before engineering commits to build**.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-blue">
  <img alt="FastAPI" src="https://img.shields.io/badge/api-FastAPI-009688">
  <img alt="License" src="https://img.shields.io/badge/license-All%20Rights%20Reserved-black">
  <img alt="Status" src="https://img.shields.io/badge/status-MVP%20with%20enterprise%20blueprint-success">
</p>

**behavior ingestion → learning → enhancement proposals → future impact simulation → before/after decision support**.

---

## ✨ What it does

Most teams decide enhancements using fragmented signals: tickets, analytics dashboards, support complaints, PM intuition, and roadmap politics.

**EvoForge AI** turns that into one AI-driven loop:

1. **Collects behavior data** from product usage, support signals, feedback, and release telemetry.
2. **Learns patterns** in friction, adoption, abandonment, and repeat workflows.
3. **Generates enhancement proposals** with reasoning and expected impact.
4. **Simulates future versions** to estimate how UX, adoption, latency, conversion, support load, and churn may change.
5. **Shows before vs after** so teams can see the business and user outcome of each enhancement.
6. **Captures failure risk** so unsafe or low-confidence ideas do not get promoted blindly.

---

## 🎯 Why this is different

### Traditional flow
- Product team reads dashboards
- Support team raises pain points
- Engineering interprets requests manually
- Future impact is mostly guessed
- Releases happen first, learning happens later

### EvoForge AI flow
- Product behavior is continuously ingested
- AI clusters friction and opportunity patterns
- AI drafts enhancement candidates automatically
- AI simulates **future-version impact before release**
- Teams compare **before / after** with expected user effect
- Confidence, risk, and failure modes are shown up front

---

## 🧠 Core capabilities

### 1) Behavior learning
EvoForge AI ingests:
- product analytics
- clickstream/session summaries
- feature usage rates
- drop-off events
- support tickets
- NPS/feedback themes
- release metrics

It then detects:
- repeated user pain
- underused features
- workflow bottlenecks
- opportunities for simplification
- likely enhancement priority

### 2) AI-generated enhancement proposals
For each opportunity, the system creates:
- problem summary
- likely root cause
- proposed enhancement
- affected user segments
- expected uplift
- confidence score
- rollout recommendation

### 3) Future-version simulation
Before building a change, EvoForge AI can estimate how a future version may affect:
- activation
- retention
- completion time
- support burden
- user satisfaction
- performance sensitivity
- regression risk

### 4) Before vs After comparison
Every proposal includes a clear comparison of:
- current user experience
- proposed future experience
- projected user/business impact

### 5) Failure-aware decisioning
The system explicitly surfaces:
- low-confidence enhancements
- noisy or biased data
- impact uncertainty
- risky assumptions
- segments likely to regress

---

## 🏗️ Reference architecture

```text
User Events / Product Analytics / Feedback / Tickets / Release Metrics
                                │
                                ▼
                      Ingestion + Normalization Layer
                                │
                                ▼
                     Behavior Learning / Pattern Mining
                                │
                 ┌──────────────┼──────────────┐
                 ▼              ▼              ▼
         Friction Detection  Opportunity Map  Segment Insights
                 │              │              │
                 └──────────────┴──────────────┘
                                │
                                ▼
                    AI Enhancement Proposal Engine
                                │
                                ▼
                    Future Version Impact Simulator
                                │
                                ▼
                    Before / After Decision Dashboard
                                │
                                ▼
                  Product / Engineering / UX Prioritization
```

---

## 📸 Before vs After example

### Before
A SaaS settings page has:
- 11 controls
- 3 advanced toggles shown to everyone
- 28% user abandonment on configuration
- high support volume: “too confusing”

### AI enhancement proposed
- progressive disclosure
- role-based simplification
- guided setup for first-time users
- contextual help near risky controls

### After (simulated)
- abandonment projected from **28% → 14%**
- setup completion time projected from **8.4 min → 4.9 min**
- support tickets on setup projected from **100/week → 58/week**
- new-user completion confidence: **0.81**

---

## 🧪 Use cases

### 1) UX simplification
Detects screens with high abandonment and recommends fewer steps, smarter defaults, or progressive disclosure.

### 2) Feature adoption growth
Finds underused features and suggests onboarding changes, contextual nudges, or repositioning.

### 3) Workflow optimization
Identifies repetitive multi-click journeys and proposes streamlining or automation.

### 4) Release planning
Shows how an enhancement may affect different user segments before committing roadmap capacity.

### 5) Support reduction
Learns from ticket patterns and converts them into product enhancement candidates.

### 6) Enterprise change review
Lets product, UX, and engineering compare likely benefits vs regression risk.

---

## ⚠️ Failure cases the README explicitly supports

### Failure case 1: weak signal quality
**Problem:** sparse or inconsistent product telemetry.

**System behavior:** lowers confidence, flags data gaps, avoids overclaiming impact.

### Failure case 2: biased behavior data
**Problem:** only one user segment is overrepresented.

**System behavior:** segment imbalance warning; recommendation is marked as non-generalizable.

### Failure case 3: enhancement improves one metric but hurts another
**Problem:** faster flow may reduce discoverability.

**System behavior:** simulator surfaces positive and negative tradeoffs together.

### Failure case 4: future-version assumption drift
**Problem:** behavior changes after seasonality, pricing, or a new user mix.

**System behavior:** confidence decays and prompts re-simulation with fresher data.

### Failure case 5: unsafe recommendation auto-trust
**Problem:** team blindly follows AI output.

**System behavior:** human approval required for recommendation promotion in enterprise mode.

---

## 📦 Repo contents

```text
evoforge-ai/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── api/routes.py
│   └── services/
│       ├── ingest.py
│       ├── learner.py
│       ├── proposals.py
│       └── simulator.py
├── data/
│   └── sample_events.json
├── tests/
│   └── test_api.py
├── docs/
│   └── examples.md
├── .github/workflows/
│   └── ci.yml
├── pyproject.toml
├── Makefile
├── Dockerfile
└── README.md
```

---

## ⚙️ How to run

### Local
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

API docs:
```text
http://127.0.0.1:8000/docs
```

### Docker
```bash
docker build -t evoforge-ai .
docker run -p 8000:8000 evoforge-ai
```

---

## ▶️ How to use

### 1. Ingest user behavior data
```bash
curl -X POST http://127.0.0.1:8000/v1/ingest/events \
  -H "Content-Type: application/json" \
  -d @data/sample_events.json
```

### 2. Generate enhancement opportunities
```bash
curl http://127.0.0.1:8000/v1/opportunities
```

### 3. Create AI enhancement proposals
```bash
curl -X POST http://127.0.0.1:8000/v1/proposals/generate
```

### 4. Simulate a future version
```bash
curl -X POST http://127.0.0.1:8000/v1/simulate \
  -H "Content-Type: application/json" \
  -d '{
    "proposal_id": "prop-001",
    "version_name": "settings-v2",
    "changes": ["guided_setup", "progressive_disclosure", "contextual_help"]
  }'
```

### 5. Compare before vs after
```bash
curl http://127.0.0.1:8000/v1/compare/prop-001
```

---

## 📈 Impact

EvoForge AI helps teams:
- prioritize enhancements using real behavior instead of guesswork
- reduce product friction earlier
- simulate outcome before roadmap commitment
- make tradeoffs visible across product, UX, and engineering
- accelerate enhancement discovery while keeping risk visible

---

## 🧭 Example successful flow

1. Events show high abandonment on onboarding.
2. AI learns repeated friction around role selection.
3. Proposal suggests a 2-step guided setup.
4. Simulator predicts better completion and fewer support tickets.
5. Team reviews before/after and schedules rollout.

## 🧨 Example unsuccessful flow

1. Data only comes from power users.
2. AI suggests hiding advanced controls.
3. Simulator warns beginner uplift but admin regression risk.
4. Confidence falls due to segment imbalance.
5. Team rejects proposal pending broader sample data.

---

## 📄 License

**All Rights Reserved**
