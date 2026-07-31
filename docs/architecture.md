# AIS Architecture

## Vision

AIS (Adaptive Intelligence System) is a multi-agent AI Business Consultant designed to help businesses identify problems, reason through them, recommend strategies, learn from outcomes, and continuously improve business performance.

---

## Core Components

### 1. Orchestrator
Responsible for coordinating the entire workflow.

Responsibilities:
- Starts the workflow
- Routes tasks to the appropriate agent
- Updates Business Context
- Decides the workflow
- Returns results to the user

---

### 2. Discovery Agent
Responsible for collecting information from the business.

Responsibilities:
- Ask business questions
- Build the initial Business Context
- Return collected information

---

### 3. Analysis Agent
Responsible for understanding the business problem.

Responsibilities:
- Analyse the Business Context
- Identify root problems
- Assign confidence scores
- Detect missing information
- Recommend specialist agents
- Store analysis in Business Intelligence Memory

---

### 4. Business Intelligence Memory (BIM)

Responsible for long-term business memory.

Stores:
- Business Profile
- Products
- Customers
- Cases
- Marketing
- Finance
- Goals
- Strategies
- Performance
- Decision Journal
- External Environment

---

## Current Workflow

User
↓
Discovery Agent
↓
Orchestrator
↓
Analysis Agent
↓
Business Intelligence Memory
↓
Specialist Agent (Future)
↓
Orchestrator
↓
User

---

## Current Version

AIS v0.1