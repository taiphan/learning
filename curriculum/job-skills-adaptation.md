# Job Skills & Adaptation Playbook

For each target role: **(1) skills extracted from the JD**, **(2) a skill-relationship map** (how skills cluster and reinforce each other), and **(3) an adaptation plan** — the gaps to close and how to position yourself to get the job.

Roles analyzed:
- **A. OCB — AI Engineer** (forward-deployed AI squad) · `tuyendung.ocb.com.vn/vi/jobs/qGG4vq`
- **B. OCB — Senior BA (Lending/BPM)** · `.../P836py`
- **C. OCB — Senior Backend Engineer** · `.../qoAEgP`
- **E. OCB — other IT roles** (Digital Banking BA, Scrum Master, T24 Dev, Digital PM) · `tuyendung.ocb.com.vn/vi/jobs`
- **F. VPBank — IT & Data** · `hr.vpbank.com.vn/ta/Tuyendung_IT/index.html`
- **G. Techcombank — Technology & Data** · `techcombankjobs.com/go/Cong-nghe/553844/`
- **H. NAB Innovation Centre Vietnam — IT & Data** · `nab.wd3.myworkdayjobs.com` · `itviec.com/nha-tuyen-dung/nab-innovation-centre-vietnam`
- **I. Anthropic — Applied AI / Claude Code** (stretch; post-VN portfolio) · [anthropic-career-adaptation.md](anthropic-career-adaptation.md) · `job-boards.greenhouse.io/anthropic`

> How to read the maps: a skill **cluster** is a group you should be able to demonstrate together; the **"feeds"** arrows show which skill unlocks or proves another. Recruiters hire on *clusters with evidence*, not isolated keywords.

---

## A. OCB — AI Engineer (Forward-Deployed AI Squad)

### A.1 Skills extracted

| Category | Must-have | Nice-to-have / "Bonus" |
|---|---|---|
| Core AI | Production LangChain/**LangGraph** (multi-agent, function calling, stateful graphs), advanced **RAG**, agent orchestration | — |
| Vision | **CV/VLM** for OCR, document intelligence, image analysis | — |
| Ops | **LLMOps/MLOps**: FastAPI, vLLM, Triton, Docker, Kubernetes, CI/CD, eval + guardrails, observability | — |
| Data | **Databricks** (Delta Lake, MLflow) | — |
| Domain | Banking / regulated industry | Forward-deployed / embedded / solutions-engineer experience |
| Behaviors | Outcome-obsessed (CIR bps, revenue lift), embedded with operators, bias to ship, exec communication | Bilingual VI/EN |
| Experience | **4+ yrs** AI/ML engineering with *production* systems (not prototypes) | — |

### A.2 Skill-relationship map

```
                         ┌──────────────────────────────┐
   BUSINESS OUTCOME  ◄───┤ Forward-deployed mindset      │
   (CIR bps / revenue)   │ embed · map workflow · own KPI│
                         └───────────────┬──────────────┘
                                         │ frames what to build
              ┌──────────────────────────┼───────────────────────────┐
              ▼                          ▼                            ▼
     ┌─────────────────┐       ┌───────────────────┐       ┌──────────────────┐
     │ AGENT/RAG CORE  │       │ DOC INTELLIGENCE  │       │ DATA PLATFORM    │
     │ LangGraph       │◄──────┤ CV/VLM · OCR      │       │ Databricks       │
     │ RAG · tools     │ feeds │ extraction        │ feeds │ Delta · MLflow   │
     └────────┬────────┘       └─────────┬─────────┘       └────────┬─────────┘
              │ all three must be productionized by ▼                │
              └───────────────►┌───────────────────────┐◄───────────┘
                               │ LLMOps / PRODUCTION   │
                               │ FastAPI·vLLM·Triton   │
                               │ Docker·K8s·CI/CD      │
                               │ eval·guardrails·obs.  │
                               └───────────┬───────────┘
                                           │ proves
                                           ▼
                               "running in production with users"
```

**Reading it:** The *forward-deployed mindset* decides **what** to build; the three technical clusters are **how**; **LLMOps** is the multiplier that converts any of them into the one thing the JD rewards — *production systems with measured business impact*. A LangGraph demo without serving/eval/guardrails reads as a "PoC factory" — exactly what they say they are **not**.

### A.3 Adaptation plan (how to get it)

1. **Build one end-to-end, production-shaped artifact** that hits a banking CIR/revenue metric. Example: an **AML-alert-triage agent** (LangGraph) + **RAG over credit policy** + **document-extraction (VLM/OCR)**, served via **FastAPI**, containerized (**Docker/K8s**), with an **eval harness + guardrails + tracing**. Even a personal/synthetic-data version demonstrates the full cluster.
2. **Quantify like an operator.** Frame every story as *"removed X minutes/headcount → ~Y bps CIR"* or *"+Z% conversion / products-per-customer."* This directly mirrors their success definition.
3. **Show "embedded," not "ivory tower."** One STAR story where you sat with business users, learned the workflow, and shipped — the Palantir-FDE / "production over PowerPoint" signal.
4. **Close likely gaps:** if weak on **vLLM/Triton serving** or **Databricks MLflow**, do a focused mini-project each; if weak on **guardrails/eval**, adopt a framework (e.g. ragas-style eval + a guardrail layer) and document it.
5. **Reframe your BRD/AI-Factory assets** (this repo) as proof of *governance + responsible-AI-by-design* and *value-led prioritization* — a differentiator most pure-coders lack.

---

## B. OCB — Senior Business Application Analyst (Lending / BPM)

### B.1 Skills extracted

| Category | Must-have | Nice-to-have |
|---|---|---|
| BA craft | **BRD authoring** + SRS quality control, **As-is/To-be** process analysis, requirements governance (feasibility, value-based prioritization) | — |
| Domain | Deep **credit-granting** process & **SBV (NHNN)** regulations *or* card operations | — |
| Systems | **LOS**, **Core Banking (T24)**, card systems (**Way4/SmartVista**) | BPM digitization, **AI/OCR** in banking |
| Architecture | Microservices, **API integration**, Agile/Scrum | — |
| Solution | E2E data flow across Core Banking, LOS, Omni-channel, CRM, **BPM** | — |
| Testing | **UAT** — end-to-end test scenarios, end-user support | — |
| Tools | **Visio / Lucidchart / Bizagi** process modeling | — |
| Soft | Stakeholder management, negotiation, professional English; mentoring junior BAs | — |
| Experience | **5+ yrs** BA in Banking/Fintech | — |

### B.2 Skill-relationship map

```
        DOMAIN KNOWLEDGE (credit/cards + SBV rules)
                        │ grounds every artifact
                        ▼
   ┌─────────────────────────────────────────────────┐
   │ PROCESS ANALYSIS  As-is → To-be  (Visio/Bizagi)  │
   └───────────────┬─────────────────────────────────┘
                   │ produces
                   ▼
   ┌──────────────────────┐   reviewed/QC'd   ┌─────────────────┐
   │ BRD (you own)        │──────────────────►│ SRS (system BA) │
   └──────────┬───────────┘                   └─────────────────┘
              │ traces into
              ▼
   ┌──────────────────────┐    enabled by     ┌──────────────────────────┐
   │ E2E SOLUTION DESIGN  │◄──────────────────│ SYSTEMS+ARCH literacy     │
   │ across LOS/T24/CRM/  │                   │ LOS·T24·Way4·API·µservices│
   │ Omni/BPM             │                   │ ·Agile/Scrum              │
   └──────────┬───────────┘                   └──────────────────────────┘
              │ validated by
              ▼
   ┌──────────────────────┐   amplified by   ┌──────────────────────┐
   │ UAT (E2E scenarios)  │◄─────────────────│ STAKEHOLDER MGMT +    │
   └──────────────────────┘                  │ English + mentoring   │
                                             └──────────────────────┘
```

**Reading it:** This is the **strongest direct match to this repo.** Your BRD template, quality gate, As-is/To-be framing, IT-delivery framework, UAT E2E scenarios, and BA-coaching content *are* the JD. Domain knowledge grounds everything; systems literacy (T24/LOS/Way4/API) is the credibility gate; stakeholder skill + English is the multiplier that turns a good analyst into a *senior* one.

### B.3 Adaptation plan (how to get it)

1. **Lead with the artifact you already own.** Your Finance BRD package (template + quality rubric ≥80% + delivery framework + UAT scenarios) is a portfolio piece — bring a redacted sample BRD and the quality-gate scorecard to interview.
2. **Prove the lending stack.** Map your experience explicitly onto **LOS → T24 → disbursement** and (if cards) **Way4/SmartVista**. If you lack hands-on T24/Way4, narrate adjacent integration work and study the data models.
3. **Show As-is/To-be in a tool.** Produce 1–2 **Bizagi/Lucidchart/Visio** process diagrams (loan origination current vs automated) — the JD names these tools specifically.
4. **Differentiate with BPM + AI/OCR.** The "ưu tiên" (preferred) line rewards anyone who has done **process digitization** and **AI-OCR** in banking — tie in your AI-Factory document-intelligence framing.
5. **Senior signals:** quantify SBV-compliant designs you've shepherded, show a junior-BA mentoring example, and demonstrate stakeholder/expectation management under regulatory deadlines.

---

## C. OCB — Senior Backend Engineer (Golang, Java, Backbase)

### C.1 Skills extracted

| Category | Must-have | Bonus |
|---|---|---|
| Languages | Expert **Java (Spring Boot / Spring Cloud)**; secondary **Golang** or Node.js | — |
| Architecture | Distributed systems, microservices, scalability/HA, capacity planning; transaction orchestration; data consistency | Platforms serving **10M+ users** |
| API | REST / **gRPC** / GraphQL lifecycles | (Backbase platform) |
| Data | **PostgreSQL/MySQL** (query optimization, partitioning), **Redis** (caching, locks) | — |
| Messaging | **Kafka**, event-driven (event sourcing, exactly-once) | — |
| Quality | Unit/integration/contract/perf + **chaos testing**; SOLID, DDD, CQRS, DRY; profiling/JVM tuning/APM | — |
| Security | OAuth2, JWT, SSO, **Zero-Trust**, API Gateway security | — |
| DevOps/Obs | Git/GitLab, Jira, GitFlow/trunk, CI/CD; **Prometheus, Grafana, ELK, OpenTelemetry/Jaeger** | Terraform + **Kubernetes**, multi-zone cloud (AWS/GCP/Azure) |
| Strategic | Mentoring, architectural reviews, **AI-SDLC** (Copilots, AI code analysis) | — |
| Experience | **5+ yrs** backend on high-traffic systems | — |

### C.2 Skill-relationship map

```
        LANGUAGE CORE: Java/Spring (+ Go)
                  │ implements
                  ▼
   ┌──────────────────────────────┐      proven safe by     ┌────────────────────┐
   │ DISTRIBUTED SYSTEM DESIGN    │────────────────────────►│ ENGINEERING RIGOR  │
   │ µservices·orchestration·HA   │                         │ SOLID/DDD/CQRS     │
   └───────┬───────────┬──────────┘                         │ chaos·perf·profiling│
           │           │                                    └────────────────────┘
   built on│           │ communicates via
           ▼           ▼
   ┌───────────────┐  ┌────────────────────┐    secured by   ┌────────────────────┐
   │ DATA LAYER    │  │ MESSAGING / EDA    │───────────────► │ BANKING SECURITY   │
   │ Postgres·Redis│  │ Kafka·event-source │                 │ OAuth2·JWT·ZeroTrust│
   └───────────────┘  └────────────────────┘                 └────────────────────┘
                  │ all observed by ▼
        ┌──────────────────────────────────────┐
        │ OBSERVABILITY + DEVOPS               │
        │ Prometheus·Grafana·ELK·OTel · CI/CD  │
        │ K8s·Terraform                        │
        └──────────────────────────────────────┘
```

**Reading it:** Language is table-stakes; the hire decision is **distributed-systems design proven by engineering rigor and made safe by banking security**, all wrapped in **observability**. Bonus items (10M+ users, K8s, Terraform) are seniority tie-breakers.

### C.3 Adaptation plan (how to get it)

1. **This is the most divergent from your current materials** — only pursue if you have real backend depth. If yes:
2. **Show a high-traffic distributed system** you built: throughput numbers, latency targets, how you handled consistency/timeouts/retries across services — exactly the JD's "partial failures" language.
3. **Demonstrate rigor, not just features:** a chaos-testing story, a JVM/profiling bottleneck you fixed, and clean SOLID/DDD/CQRS examples.
4. **Banking security fluency:** OAuth2/JWT/SSO + Zero-Trust + API-gateway — speak to a concrete secure-integration with core banking.
5. **Cover the observability + IaC bonus** (Prometheus/Grafana/ELK/OTel, K8s, Terraform) and mention **AI-SDLC** (you already use AI dev tools) — a cheap, on-trend signal they explicitly ask for.

---

## E. OCB — Other IT roles (current openings)

| Role | Code / URL | Fit | Key skills |
|---|---|---|---|
| **Senior BA (Digital Banking)** | `PgAjbq` | **High** | Same as **B**, domain = digital channels / omni |
| **Senior BA (Lending/BPM)** | `P836py` | **Highest** | See **B** |
| **Scrum Master (Junior/Middle)** | `PxngNq` | Medium | Agile/Scrum ceremonies, delivery gates, stakeholder facilitation |
| **T24 Technical Developer** | `qbbVNq` | Low–Medium | Temenos T24, core-banking customization |
| **Giám đốc Phát triển giải pháp số (PM)** | `ypAXaP` | Medium–High | Digital product strategy, roadmap, cross-functional delivery |

**Adaptation:** For Digital Banking BA, reuse **B** portfolio + add omni/mobile journey examples. For Scrum Master, lead with your IT-delivery framework (sprint gates, dual-track). For Digital PM, combine BA artifacts + AI/value roadmap from `strategy-and-roadmap.md`.

---

## F. VPBank — IT & Data (key targets)

Source: [VPBank IT recruitment](https://hr.vpbank.com.vn/ta/Tuyendung_IT/index.html) (~73 titles; details in page modals).

### F.1 Roles that match BA + AI profile

| Role | Type | Must-have skills (typical) | Adaptation |
|---|---|---|---|
| **AI Engineer (DS1)** | Data/AI | Python, ML/DL, LLM/RAG/agents, MLOps, banking use cases | Same cluster as **A** — production agents + eval |
| **Data Scientist (DS1)** | Data | Python/R/Spark/SQL, ML/DL, statistical modeling, Agile, **10+ yrs** for senior | Classical ML + one GenAI project; quantify financial impact |
| **Data Engineer** | Data | Pipelines, ETL, Spark/Kafka, data architecture, ML feature stores | SQL + Spark + one end-to-end pipeline artifact |
| **Senior Business Analyst** | IT/BA | BRD, process, UAT, banking systems, stakeholder mgmt | Your repo = direct portfolio (**B**) |
| **Senior Business Architect** | IT/BA | E2E process, capability map, solution alignment | BRD + operating model + As-is/To-be |
| **Senior Solution Architect** | IT | Enterprise/solution design, integration, microservices | TOGAF-lite + API/integration stories |
| **Product Owner — Digital Factory** | IT/PM | Backlog, Agile, business value, acceptance criteria | BRD AC → user stories traceability |

### F.2 Skill-relationship map (VPBank AI/Data track)

```
  BANKING DOMAIN (credit, ops, CX, compliance)
              │
              ▼
  ┌───────────────────────┐     ┌─────────────────────┐
  │ DATA FOUNDATIONS      │────►│ CLASSICAL ML        │
  │ SQL · Python · Spark  │     │ scoring · forecast  │
  └───────────┬───────────┘     └──────────┬──────────┘
              │                            │
              └────────────┬───────────────┘
                           ▼
              ┌────────────────────────────┐
              │ GENAI LAYER                │
              │ RAG · LangGraph · agents     │
              └────────────┬───────────────┘
                           │ productionized by
                           ▼
              ┌────────────────────────────┐
              │ MLOps / LLMOps + GOVERNANCE│
              │ deploy · monitor · guardrails│
              └────────────┬───────────────┘
                           ▼
              "AI Engineer / Data Scientist hire signal"
```

### F.3 Adaptation plan (VPBank)

1. **Primary target:** **Senior BA** or **AI Engineer** — pick one narrative (BA-first with AI/OCR differentiator, or AI-first with governance/BRD differentiator).
2. **Portfolio:** BRD sample + one AI demo (RAG policy copilot or doc-intelligence) + metrics slide from `Head-of-AI-Factory-Slides.pptx`.
3. **Gap close:** VPBank senior data roles often ask **10+ yrs** — emphasize depth of production impact and leadership if years are short; for AI Engineer, **4–5 yrs production AI** may suffice if artifact is strong.

---

## G. Techcombank — Technology & Data

### G.1 Technology category (`/go/Cong-nghe/553844/`)

| Role | Code | Level | Key skills |
|---|---|---|---|
| **Senior Expert, Solution Architecture** | 40001547 | Chuyên gia | E2E solution design, enterprise arch, RFP/scorecards, SDLC, fintech high-volume systems, **~12 yrs** |
| **DevSecOps Expert / Senior Specialist** | 40001146 / 47 | Chuyên gia / CV | CI/CD, security in pipeline, cloud/containers |
| **Senior Director, Technology** | 40001149 | Quản lý cấp cao | Tech leadership, strategy |
| **Cloud Engineer / Network Ops** | — | CV | Cloud platform, network operations |

### G.2 Data & Analytics (separate category on portal)

| Role | Code | Key skills |
|---|---|---|
| **Senior Data Scientist** | 40000030 | ML/DL, Python/R/Spark/SQL, financial markets AI, Agile, mentoring, **10+ yrs**, Master's+ |
| **Senior Data Engineer** | 40000063 | Data architecture, pipelines/ETL, integration, reusable assets for ML, regulatory compliance |
| **Senior Data Architect** | 40000054 | Big-data platform (Hadoop/Spark/Kafka), cloud analytics, **10+ yrs**, 3+ yrs architect |

### G.3 Adaptation plan (Techcombank)

- **Senior Data Scientist:** strongest AI target — build credit-scoring or NBO/recommendation case study with production narrative.
- **Solution Architecture:** bridge from Senior BA — add TOGAF vocabulary, RFP evaluation story, and high-volume integration design.
- **Data Engineer:** only if you want platform track — prioritize Spark/SQL pipelines over modeling.

---

## H. NAB Innovation Centre Vietnam — IT & Data

**Entity:** NAB Innovation Centre Vietnam (NICV) — technology hub of National Australia Bank (NAB), part of NAB Technology & Enterprise Operations. **~2,000+** colleagues in **Hà Nội** and **TP.HCM** (est. 2019).

| Channel | URL |
|---|---|
| **Official careers hub** | https://www.nab.com.au/about-us/careers/nabvietnam |
| **Apply (Workday)** | https://nab.wd3.myworkdayjobs.com/en-US/nab_careers → Location: **Vietnam** |
| **ITviec listings** | https://itviec.com/nha-tuyen-dung/nab-innovation-centre-vietnam |
| **Early career — StarCamp** | Workday search `?q=StarCamp` (Software + **Data Engineering** 12-week bootcamp) |

**Tech stack (from NICV profile):** Java, Spring Boot, React, Node.js, TypeScript, AWS, Kubernetes, Terraform, microservices, DevOps, **LLM**.

---

### H.1 Current openings — IT & Data (17 roles, ITviec scan)

#### Data / BA / product (best fit for your profile)

| Role | Location | Type | Key skills | ITviec |
|---|---|---|---|---|
| **Senior/Lead Business Analyst (data focus)** | HCMC / Hà Nội | **Data + BA** | Business analysis, data-driven, Agile, data analysis, English | [1219](https://itviec.com/viec-lam-it/senior-lead-business-analyst-data-focus-nab-innovation-centre-vietnam-1219) |
| **Senior Business Analyst (Biz focus)** | HCMC | BA / IT | Business analysis, Agile, English, banking domain | [3846](https://itviec.com/viec-lam-it/senior-business-analyst-biz-focus-nab-innovation-centre-vietnam-3846) |
| **Senior Database Administrator (Oracle/PostgreSQL)** | HCMC | **Data platform** | DBA, PostgreSQL, Oracle, cloud | [3634](https://itviec.com/viec-lam-it/senior-database-administrator-oracle-postgresql-nab-innovation-centre-vietnam-3634) |
| **Product Owner** | HCMC | IT / PM | Agile, backlog, banking/fintech, **10+ yrs** (5+ as PO) | [1132](https://itviec.com/viec-lam-it/product-owner-nab-innovation-centre-vietnam-1132) |

#### Software engineering & architecture

| Role | Location | Key skills | ITviec |
|---|---|---|---|
| **Solution Designer** | Hà Nội | Software architecture, microservices, Java, React, DevOps | [2848](https://itviec.com/viec-lam-it/solution-designer-nab-innovation-centre-vietnam-2848) |
| **Solution Designer** | HCMC | Architecture, React, Java, .NET, Node, microservices | [5434](https://itviec.com/viec-lam-it/solution-designer-nab-innovation-centre-vietnam-5434) |
| **Java Engineer (All levels)** | Hà Nội | Java, Spring Boot, React, cloud, AI | [0402](https://itviec.com/viec-lam-it/java-engineer-all-levels-nab-innovation-centre-vietnam-0402) |
| **Consultant, Fullstack Engineer (Python/ReactJS)** | HCMC / Hà Nội | Python, React, DevOps, security | [0039](https://itviec.com/viec-lam-it/consultant-fullstack-engineer-python-reactjs-nab-innovation-centre-vietnam-0039) |
| **Lead Fullstack Engineer** | HCMC | Java, JavaScript, API, microservices, AWS, leadership | [5042](https://itviec.com/viec-lam-it/lead-fullstack-engineer-nab-innovation-centre-vietnam-5042) |
| **Senior React Native Engineer** | HCMC | React Native, Node, AWS, Jenkins | [3719](https://itviec.com/viec-lam-it/senior-react-native-engineer-nab-innovation-centre-vietnam-3719) |

#### DevOps / SRE / security / production

| Role | Location | Key skills | ITviec |
|---|---|---|---|
| **Senior DevOps Engineer** | HCMC / Hà Nội | DevOps, CI/CD, Terraform, Kubernetes, AWS, DevSecOps | [5444](https://itviec.com/viec-lam-it/senior-devops-engineer-nab-innovation-centre-vietnam-5444) |
| **Senior Production Support Engineer** | HCMC | Production support, API, user journey, AI | [1621](https://itviec.com/viec-lam-it/senior-production-support-engineer-nab-innovation-centre-vietnam-1621) |
| **Security Architect — Group Security** | HCMC / Hà Nội | Security architecture, software architecture | [4442](https://itviec.com/viec-lam-it/security-architect-group-security-nab-innovation-centre-vietnam-4442) |

#### QA & leadership

| Role | Location | Key skills | ITviec |
|---|---|---|---|
| **Senior Performance Test Engineer** | HCMC | Gatling, JMeter | [2231](https://itviec.com/viec-lam-it/senior-performance-test-engineer-nab-innovation-centre-vietnam-2231) |
| **Senior/Middle Automation Quality Engineer** | HCMC | Automation, Selenium, Java, microservices | [2145](https://itviec.com/viec-lam-it/senior-middle-automation-quality-engineer-nab-innovation-centre-vietnam-2145) |
| **Engineering Manager** | HCMC / Hà Nội | Team mgmt, Java, architecture, stakeholder mgmt | [5412](https://itviec.com/viec-lam-it/engineering-manager-nab-innovation-centre-vietnam-5412) |
| **Engineering Manager (Frontend/Mobile)** | HCMC | React Native, React, leadership, Agile | [2757](https://itviec.com/viec-lam-it/engineering-manager-frontend-mobile-nab-innovation-centre-vietnam-2757) |

#### Rotating / check Workday (recently listed, may not appear on ITviec)

| Role | Type | Key skills |
|---|---|---|
| **Senior AIOps/MLOps Engineer — Nexus** | **Data/AI** | LangGraph, LangChain, LLMs, Databricks, ServiceNow, K8s/EKS, Terraform, OpenTelemetry, agentic workflows |
| **Senior Data Integration** | **Data** | Data pipelines, integration, enterprise data platforms |
| **Senior Site Reliability Engineer** | IT/Ops | SRE, observability, production reliability |
| **Lead / Middle-Senior Java Engineer** | IT | Java backend, microservices |
| **Delivery Lead (Technical PM)** | IT/PM | Technical delivery, stakeholder mgmt |

Search Workday: `?q=MLOps` OR `Data Integration` OR `Data Engineer`.

---

### H.2 Key roles — skills extracted

#### H.2a Senior/Lead Business Analyst (data focus)

| Category | Must-have | Nice-to-have |
|---|---|---|
| BA craft | Business analysis, **data-driven** requirements, Agile ceremonies | Lead/mentor junior BAs |
| Data | Data analysis, translating data needs for engineering teams | SQL, data modelling literacy |
| Domain | Banking / financial services (AU/NZ context via NAB) | Regulated-industry experience |
| Soft | English (working/professional), stakeholder management | HCMC + Hanoi hybrid |

**Adaptation:** Same as **B** (OCB Senior BA) — lead with BRD package, quality gate, UAT E2E scenarios; **differentiate with data-analysis examples** (KPI definition, data requirements in BRD Section I, analytics use-case intake).

#### H.2b Senior AIOps/MLOps Engineer — Nexus (when open)

| Category | Must-have |
|---|---|
| GenAI / agents | **LangGraph / LangChain** (or CrewAI, AutoGen), LLMs (GPT-4, Claude, LLaMA), agentic workflows, tool-use, multi-step planning |
| Integration | Connectors/APIs to enterprise systems (**ServiceNow**, **Databricks**) |
| Cloud & ops | **AWS** (EKS a plus), **Kubernetes**, **Terraform**, Docker, CI/CD, secrets management |
| Observability | **OpenTelemetry**, SLOs, error budgets, runbooks, auto-remediation, blue/green/canary |
| Languages | Production **Python** and/or **TypeScript** |
| Platform | Java (Spring Boot), Node.js, React — for app/platform context |

**Adaptation:** Nearly identical cluster to **A** (OCB AI Engineer) — your Phase 3–4 flagship (LangGraph copilot + FastAPI/Docker/eval) is the proof artifact. Add **Terraform + K8s on AWS** story and **ServiceNow/Databricks** familiarity if applying here.

#### H.2c Solution Designer

| Category | Must-have |
|---|---|
| Architecture | Software/solution architecture, **microservices**, API design |
| Stack | Java, React, .NET, Node — at least two fluently |
| Process | Agile, E2E solution design, integration with AU engineering teams |
| Domain | Banking products for **10M+ customers** |

**Adaptation:** Bridge from Senior BA — bring As-is/To-be diagrams + one architecture decision record (ADR) showing trade-offs (microservices vs monolith, sync vs async).

#### H.2d Product Owner

| Category | Must-have |
|---|---|
| Experience | **10+ yrs** industry, **5+ yrs** as Product Owner; banking/fintech preferred |
| Craft | Agile/Scrum, backlog management, acceptance criteria, product journeys |
| Technical literacy | Cloud platforms (EKS/AKS/GKE), observability, reliability across apps + infra |
| Soft | English, regulated-industry stakeholder management |

**Adaptation:** Map BRD Section M acceptance criteria → user stories → sprint backlog; show traceability from business need to shipped feature (your IT-delivery framework).

---

### H.3 Skill-relationship map (NAB IT & Data)

```
  NAB BANKING DOMAIN (AU/NZ · 10M customers · regulated)
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
   ┌───────────┐  ┌────────────┐  ┌─────────────────┐
   │ BA / DATA │  │ GENAI/ML   │  │ ENGINEERING     │
   │ BA data   │  │ AIOps/MLOps│  │ Java·React·Cloud│
   │ focus · PO│  │ LangGraph  │  │ microservices   │
   └─────┬─────┘  └─────┬──────┘  └────────┬────────┘
         │              │                   │
         │    all productionized on         │
         └──────────────┼───────────────────┘
                        ▼
         ┌──────────────────────────────────────┐
         │ NAB PLATFORM SPINE                   │
         │ AWS · Kubernetes · Terraform · Agile │
         │ CI/CD · observability · English      │
         └──────────────────────────────────────┘
```

**Reading it:** NAB hires **platform-native** engineers and BAs who can work in a **global, English-first, AWS/K8s** environment. The **AIOps/MLOps — Nexus** role is the closest pure-AI match; **BA (data focus)** is the closest match to your current repo.

---

### H.4 Adaptation plan (NAB)

1. **Primary targets:** **Senior/Lead BA (data focus)** → **Product Owner** (if 5+ yrs PO) → **AIOps/MLOps Nexus** (when listed on Workday).
2. **Portfolio bundle:**
   - BRD sample + quality rubric (≥80%) from this repo
   - One **data-focused** BRD section (objectives with baseline/target/measurement, data classification)
   - Optional: LangGraph policy copilot demo (for AIOps/MLOps or to differentiate BA applications)
3. **Language:** NAB Vietnam is **English-heavy** — prepare CV, cover letter, and interview stories in English (`cv-cover-letter.md` template).
4. **Stack signals:** Mention **AWS, microservices, Agile/Scrum** even in BA applications — NICV engineers work closely with AU teams on cloud-native delivery.
5. **Apply path:** Workday first (official) → ITviec as mirror; set Workday job alert for Vietnam + keywords `Business Analyst`, `MLOps`, `Data`.

### H.5 Early career (StarCamp — not full-time hire)

| Program | Track | Duration | For |
|---|---|---|---|
| **StarCamp Software Engineering** | Java or Full-stack JS | 12 weeks, paid | Final-year / fresh grad |
| **StarCamp Data Engineering** | Data pipelines & platforms | 12 weeks, paid | CS/Data grads → path to Data Integration / DE roles |

Apply: https://nab.wd3.myworkdayjobs.com/en-US/nab_careers?q=StarCamp

---

## I. Anthropic — Applied AI & Claude Code (stretch target)

**Full 52-week map + CV:** [anthropic-career-adaptation.md](anthropic-career-adaptation.md)  
**Apply:** [job-boards.greenhouse.io/anthropic](https://job-boards.greenhouse.io/anthropic)

> **Sequencing:** Finish **§A/§H portfolio** + land **VN bank role** first (months 12–18). Anthropic Tier 1–2 are realistic at **18–24 months** with relocation (SF/NYC hybrid, visa sponsorship available).

### I.1 Three tiered roles

| Tier | Role | Bar | Horizon | Job ID |
|---|---|---|---|---|
| **1 — Primary** | Applied AI Architect, Commercial | 3+ yrs SWE + customer-facing | 18–24 mo | [5192805008](https://job-boards.greenhouse.io/anthropic/jobs/5192805008) |
| **2 — Bridge** | Technical Specialist, Claude Code | 3–7 yrs SA/devrel + builder | 12–18 mo | [5197597008](https://job-boards.greenhouse.io/anthropic/jobs/5197597008) |
| **3 — Stretch** | Staff SWE, Dev Productivity (CI/CD) — Claude Code | 7+ yrs dev-infra | 3–5 yrs | [5271428008](https://job-boards.greenhouse.io/anthropic/jobs/5271428008) |

### I.2 Skills extracted — Tier 1 (Applied AI Architect, Commercial)

| Category | Must-have | Maps from your path |
|---|---|---|
| Pre-sales advisory | Discovery → eval → deployment; business ↔ technical translation | §B Senior BA stakeholder work |
| Builder | Python prototypes, eval frameworks, near-production examples | Syllabus weeks 31–46 → `policy-copilot-api` |
| Claude stack | Claude API, Claude Code, Claude for Enterprise | Week 31+: rebuild flagship on Claude API |
| Architecture | Scalable cloud + enterprise integration | Add AWS/Azure module post-month 12 |
| Safety | Reliable, beneficial deployments | `governance-mlops.md` + quality gates in repo |
| Experience | 3+ yrs SWE **or** 3+ yrs SA/TAM with hands-on build | Portfolio year + VN AI role = narrative |

### I.3 Skill-relationship map

```
  CUSTOMER ADOPTION (measured Claude value)
              ▲
   ┌──────────┴──────────┐
   │ EVAL + GOVERNANCE    │◄─── §A/H LLMOps cluster + governance-mlops.md
   └──────────┬──────────┘
              │
   ┌──────────▼──────────┐
   │ RAG + AGENTS         │◄─── Syllabus Phase 4 (LangGraph)
   │ Claude API           │
   └──────────┬──────────┘
              │
   ┌──────────▼──────────┐
   │ DISCOVERY + TRUST    │◄─── §B BA / banking domain
   └─────────────────────┘
```

### I.4 Adaptation plan (how to get Tier 1)

1. **Same flagship as §A:** LangGraph policy copilot + FastAPI + Docker + eval harness — **one repo, three employers** (OCB, NAB, Anthropic).
2. **Anthropic-specific adds (months 10–12):** Claude API migration · FS case study · 5-min English demo · reusable blueprint README.
3. **Experience gap:** Count intensive portfolio + VN production role toward "3+ yrs SWE"; lead CV with **shipped artifacts**, not job titles alone.
4. **Cover letter angle:** Banking governance + responsible AI + eval discipline = Anthropic mission fit ([cv-cover-letter.md §5](cv-cover-letter.md#5-applied-ai-architect-anthropic--cv-outline)).
5. **Tier 2 earlier option:** If Claude Code enablement repo is strong (`hooks`, MCP, eval CI), apply Technical Specialist before Tier 1.

### I.5 Syllabus week map (summary)

| Syllabus block | Weeks | Anthropic skill |
|---|---|---|
| Python + SQL | 1–8 | Read customer integration code |
| ML + SHAP | 17–24 | Credible ML generalist |
| RAG + LangGraph | 31–38 | **Core interview topics** |
| FastAPI + Docker + CI eval | 39–46 | Near-production + regression detection |
| 2nd banking use case | 47–50 | Financial services vertical demo |

Full 52-week table: [anthropic-career-adaptation.md §52-week map](anthropic-career-adaptation.md#52-week-syllabus--anthropic-skills-map).

---

## Cross-role skill graph (where the roles overlap)

```
                 ┌────────────────────────────────────────────┐
                 │ SHARED BANKING SPINE (all banks)            │
                 │ regulated industry · stakeholder comms ·    │
                 │ VI/EN · Agile · microservices · cloud       │
                 └───────────────┬────────────────────────────┘
        ┌───────────┬───────────┼───────────┬───────────┬───────────┐
        ▼           ▼           ▼           ▼           ▼           ▼
   OCB AI ENG   OCB SEN BA   VPBank AI/BA  TCB DS/Arch  NAB BA/AIOps  ANTHROPIC Applied AI
   LangGraph    BRD·UAT      DS·AI Eng     ML·Spark     data-BA·LangGraph  Claude·evals·pre-sales
        │  shared: API integration + production discipline + outcome metrics │
        └─────────────────────────────────────────────────────────────────┘
```

- **A ↔ B bridge:** *document-intelligence / AI-OCR in banking* — credible for OCB AI Engineer and OCB Senior BA (preferred).
- **B ↔ H bridge:** *data-focused BA* — NAB **Senior/Lead BA (data focus)** is the same spine as **B** plus explicit data-analysis emphasis.
- **A ↔ H bridge:** NAB **AIOps/MLOps — Nexus** mirrors OCB AI Engineer (LangGraph, Databricks, K8s, production agents).
- **A/H ↔ I bridge:** OCB/NAB flagship (LangGraph + eval + FastAPI/Docker) is the **same artifact** Anthropic Applied AI asks for — add **Claude API** + enablement demo for [§I](anthropic-career-adaptation.md).
- **Common multiplier:** **production discipline + business-outcome quantification** — every bank penalizes PoC-only work; Anthropic adds **eval frameworks + safety-by-design**.

---

## Recommended targeting (best fit → stretch)

| Rank | Role | Bank | Why | Biggest gap to close |
|---|---|---|---|---|
| 1 | **Senior BA (Lending/BPM or Digital)** | OCB | Your BRD/UAT repo *is* the JD | T24/LOS/Way4 + Bizagi/Visio As-is/To-be |
| 2 | **Senior/Lead BA (data focus)** | **NAB** | BA + data-driven — English-first global hub | Data-analysis examples + English CV/interview |
| 3 | **Senior BA / Business Architect** | VPBank | Same BA spine + larger org | Same as #1 + VPBank systems narrative |
| 4 | **AIOps/MLOps Engineer — Nexus** | **NAB** / OCB AI Engineer | LangGraph + K8s + Databricks — closest AI IC match | End-to-end LangGraph/RAG + Terraform/K8s artifact |
| 5 | **AI Engineer** | OCB / VPBank | GenAI + production + banking outcomes | Same as #4 |
| 6 | **Senior Data Scientist** | Techcombank / VPBank | ML/AI leadership track | 10+ yrs narrative or deep production portfolio |
| 7 | **Solution Designer** | **NAB** / Techcombank | BA → solution architecture bridge | Microservices ADR + architecture portfolio |
| 8 | **Product Owner** | **NAB** | BRD → backlog → AC traceability | 5+ yrs PO experience if required |
| 9 | **Backend Engineer** | OCB | Only with Java/distributed depth | Kafka/K8s/chaos-testing portfolio |
| 10 | **Applied AI Architect, Commercial** | **Anthropic** | Same forward-deployed + eval story as §A; global scale | 3+ yrs SWE narrative + Claude API + relocation SF/NYC |
| 11 | **Technical Specialist, Claude Code** | **Anthropic** | Enablement + demos; BA teaching skill transfers | Daily Claude Code + hooks/MCP reference repo |
| 12 | **Staff SWE, CI/CD — Claude Code** | **Anthropic** | Harness/loop engineering destiny | 7+ yrs dev-infra — year 3+ stretch |

**Anthropic detail:** full 52-week map + CV → [anthropic-career-adaptation.md](anthropic-career-adaptation.md)

### Universal positioning moves (apply to whichever you target)
1. **Mirror the JD's language** in your CV summary (LangGraph/RAG/LLMOps · BRD/As-is/To-be/UAT · Claude API/evals · Spring/Kafka/distributed).
2. **One quantified flagship per role** (CIR bps / revenue lift · BRD quality-gate pass-rate & delivery speed · throughput/latency at scale).
3. **Bring an artifact**, not just claims — your repo (BRD package, AI-Factory docs, the visual decks) is a ready-made portfolio.
4. **Production > prototype** narrative everywhere — it's the single most repeated signal across banking AI JDs.

---

## AI skills roadmap — what to learn (and in what order)

This roadmap gets you from **BA / banking domain + this repo** to **hire-ready for AI Engineer / Data Scientist / AI-augmented Senior BA** at OCB, VPBank, Techcombank, or **NAB Vietnam** — and builds toward **Anthropic Applied AI** (§I) on the same portfolio.

### Target outcome (what "done" looks like)

You can demo **one banking AI system** that is:
- grounded (RAG or structured data, not hallucination-prone),
- served (API + container),
- evaluated (quality + safety metrics),
- governed (risk tier, guardrails, audit trail),
- tied to a **business metric** (CIR, conversion, TAT, fraud rate).

That single artifact satisfies OCB AI Engineer, VPBank AI Engineer, **NAB AIOps/MLOps — Nexus**, and strengthens Senior BA (data focus) at **NAB/OCB** and Techcombank Data Scientist interviews.

### Learning paths (pick one primary track)

| Track | Target roles | Duration (focused) | You already have |
|---|---|---|---|
| **Track 1 — AI Engineer (GenAI)** | OCB / VPBank AI Engineer, **NAB AIOps/MLOps**, **Anthropic Applied AI (§I)** | **4–6 months** | Governance, BRD, operating model (`curriculum/`) |
| **Track 2 — Data Scientist (ML + GenAI)** | VPBank/Techcombank Data Scientist | **6–9 months** | Domain + requirements; need deeper ML math/code |
| **Track 3 — AI-augmented BA** | OCB / VPBank / **NAB** Senior BA | **2–3 months** AI add-on | **Strongest base** — full BRD/UAT repo |

Most people with your materials should run **Track 3 first** (fastest job) while building **Track 1** in parallel for AI roles.

---

### Phase 0 — Foundations (Weeks 1–2) · skip if comfortable

| Learn | Why | How |
|---|---|---|
| **Python 3.11+** (functions, classes, async basics) | All AI roles | 30 min/day: automate a BRD checklist script in this repo |
| **Git** (branch, PR, CI) | Production signal | Push a small feature to a personal GitHub repo |
| **SQL** (joins, window functions, aggregates) | Data Scientist / Engineer gate | Query a public lending dataset (Kaggle credit default) |
| **CLI + Docker basics** | LLMOps prerequisite | `docker run` a Postgres + run SQL against it |

**Exit check:** Write a Python script that reads a CSV, computes KPIs, and outputs a one-page summary.

---

### Phase 1 — Data & classical ML (Weeks 3–8)

| Learn | Why | Resources / project |
|---|---|---|
| **pandas, numpy** | Data wrangling | Clean a loan application dataset |
| **scikit-learn** | Scoring, classification, regression | Build a **credit default / PD proxy model** |
| **Train/validation/test, metrics** (AUC, precision/recall, calibration) | Banking models are judged on this | Document baseline vs tuned model |
| **Feature engineering** | JD asks explicitly (OCB, Techcombank) | Income, DTI, bureau flags, behavior features |
| **Explainability basics** (SHAP or feature importance) | Responsible AI / regulator questions | One slide: "why this decision" |

**Portfolio project 1:** *POS pre-approval scoring prototype* — ties to your BRD examples (`examples/04a-brd-pos-lending.md`).

**Exit check:** Notebook or repo with reproducible train → evaluate → explain pipeline; state business metric (e.g. reduce false declines 5%).

---

### Phase 2 — Deep learning & NLP essentials (Weeks 9–12)

| Learn | Why | Resources / project |
|---|---|---|
| **PyTorch or TensorFlow basics** | Data Scientist JDs | MNIST → simple tabular NN |
| **Transformers concept** (attention, embeddings) | Prerequisite for LLMs | Hugging Face course (free) |
| **Embeddings + vector search** | RAG core | Index 50 credit-policy PDF chunks in **Chroma or pgvector** |
| **Text classification / NER** | Doc intelligence | Classify document types (contract, ID, collateral) |

**Portfolio project 2:** *Document classifier* for loan files — bridges to OCB VLM/OCR and Senior BA AI/OCR preference.

**Exit check:** Given a PDF, return doc type + extracted key fields (even if rule-assisted at first).

---

### Phase 3 — Generative AI & agents (Weeks 13–18) · **core for AI Engineer**

| Learn | Why | Resources / project |
|---|---|---|
| **LLM APIs** (OpenAI / Azure OpenAI / local via Ollama) | Production GenAI | Start with structured prompts + JSON output |
| **RAG pipeline** (chunk, embed, retrieve, generate) | Every banking GenAI JD | LangChain or LlamaIndex tutorial |
| **LangGraph** (stateful graphs, tools, multi-agent) | **OCB hard requirement** | Official LangGraph docs + 1 agent with 3 tools |
| **Function calling / tool use** | Agents that *act* | Tools: policy lookup, calculator, ticket API mock |
| **Prompt engineering + eval** | Quality gate | Define 20 test questions with expected grounded answers |

**Portfolio project 3 (flagship):** *Credit policy copilot*
- RAG over synthetic policy docs
- LangGraph agent: intake → retrieve → answer → escalate if low confidence
- Guardrail: refuse out-of-scope / PII leakage
- Metric: **grounded-response rate ≥ 90%** on test set

**Exit check:** Live demo + README with architecture diagram (reuse style from `Head-of-AI-Factory-Slides.pptx`).

---

### Phase 4 — Production & LLMOps (Weeks 19–22)

| Learn | Why | Resources / project |
|---|---|---|
| **FastAPI** | OCB JD: model serving | Wrap copilot as REST API |
| **Docker + docker-compose** | Container standard | One-command local deploy |
| **CI/CD** (GitHub Actions) | Production discipline | Lint + test + build on push |
| **Observability** (logging, tracing, latency) | Banking-grade | Log prompts/responses (redacted), trace IDs |
| **Eval harness** (ragas or custom) | LLMOps gate | Automated nightly eval on golden set |
| **Guardrails** (input/output filters, PII redaction) | Responsible AI | Block jailbreaks + mask national ID patterns |
| **Optional:** vLLM, MLflow, Databricks | JD bonus | Pick one; MLflow for experiment tracking is highest ROI |

**Portfolio project 4:** Harden project 3 — add FastAPI, Docker, eval dashboard, rollback story.

**Exit check:** `docker compose up` → API answers policy questions → eval report generated.

---

### Phase 5 — Banking domain AI (Weeks 23–26)

Map skills to **real bank metrics** (what hiring managers measure):

| Use case | Skills used | Metric to cite |
|---|---|---|
| **AML alert triage agent** | LangGraph + classification | Analyst minutes saved / alert |
| **Doc intelligence (OCR/VLM)** | CV/VLM + extraction | Straight-through processing % |
| **Next-best-offer / propensity** | Classical ML + feature store | Conversion / products-per-customer |
| **Ops copilot (collections, RM)** | RAG + workflow tools | Handle time, first-contact resolution |
| **Credit policy Q&A** | RAG + guardrails | Grounded-response rate, escalation rate |

Pick **two** use cases: one **GenAI** (Phase 3–4 artifact) + one **Predictive ML** (Phase 1 artifact).

**Exit check:** One-page "value case" per use case with baseline, target, measurement — same format as BRD Section C.

---

### Phase 6 — Governance & interview readiness (Weeks 27–28)

| Learn | Why | Use from repo |
|---|---|---|
| **Three governance gates** (intake, pre-deploy, in-life) | Differentiator vs pure coders | `governance-mlops.md` |
| **Model cards, risk tiers** | Regulator / CISO questions | `governance-mlops.md` |
| **BRD → AI use-case intake** | BA + AI hybrid story | `docs/01-brd-template-en.md`, quality gate |
| **STAR stories** (embed, ship, metric) | OCB "forward-deployed" signal | `interview-kit.md` dimensions |

**Exit check:** 5-minute exec pitch: problem → solution → metric → governance → 90-day plan.

---

### Weekly rhythm (sustainable)

| Day | Activity | Time |
|---|---|---|
| Mon–Thu | Learn + code (one module above) | 1–2 hrs/day |
| Fri | Document (README, diagram, metric) | 1 hr |
| Sat | Portfolio polish / mock interview | 2 hrs |
| Sun | Rest or optional reading | — |

**Minimum viable pace:** 5 hrs/week → ~6 months to Phase 4 flagship. **10 hrs/week → ~3 months.**

---

### Skill stack summary (hire checklist)

Check off before applying to **AI Engineer / Data Scientist**:

- [ ] Python + SQL fluent
- [ ] One **classical ML** project with metrics (scoring/forecast)
- [ ] One **RAG** system with eval scores
- [ ] One **LangGraph agent** with tools
- [ ] **FastAPI + Docker** deploy
- [ ] **Guardrails + logging** (no PII in logs)
- [ ] **Business metric** documented (CIR, conversion, TAT, etc.)
- [ ] **Governance narrative** (gates, risk tier, human oversight)
- [ ] **BRD or process diagram** (for BA-hybrid roles)
- [ ] GitHub repo + 3-slide exec summary (use your deck generator pattern)

---

### What NOT to learn first (common traps)

| Trap | Why skip early |
|---|---|
| Training LLMs from scratch | JDs want applied AI, not research |
| 10 frameworks at once | Master LangGraph + one vector DB |
| Kaggle-only notebooks | No serving/eval = "PoC factory" |
| Ignoring domain | Banking hires outcome + compliance, not demos |
| Only Copilot usage | "AI-SDLC" helps; it doesn't replace RAG/LLMOps |

---

### Recommended free/low-cost resources

| Topic | Resource |
|---|---|
| Python for data | Kaggle Learn, Real Python |
| ML | scikit-learn docs, *Hands-On ML* (select chapters) |
| LLMs & RAG | DeepLearning.AI short courses, LangChain/LangGraph docs |
| MLOps | Made With ML, MLflow tutorials |
| Banking context | Your repo `docs/`, SBV circulars summaries, Finacle/LOS overviews |
| Interview | `curriculum/interview-kit.md`, `cv-cover-letter.md` |

---

### 90-day sprint (if you need a job soon)

| Month | Focus | Deliverable |
|---|---|---|
| **Month 1** | Python/SQL + scikit-learn PD model | Project 1 repo |
| **Month 2** | RAG + LangGraph policy copilot | Project 3 demo |
| **Month 3** | FastAPI/Docker/eval + apply OCB/VPBank/**NAB** BA+AI | Project 4 + updated CV |

Apply to **Senior BA** in month 2–3 while finishing AI artifact — dual pipeline maximizes offers.

---

### Next actions in this repo

1. Fill placeholders in `cv-cover-letter.md` with your real metrics.
2. Add a `curriculum/portfolio/` folder with links to GitHub projects as you build them.
3. Extend `interview-kit.md` with banking AI STAR prompts (AML triage, policy RAG, doc OCR).
4. Tell me your **years of experience + current stack** and I'll tailor the roadmap to a 12-week or 24-week calendar.
