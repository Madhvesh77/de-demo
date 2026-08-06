# Data Engineering Workshop – Project Guide (v1.0)

> **Status:** 🚧 Under Development
> **Architecture Status:** Frozen (v1.0)

---

# 1. Vision

This project is **not** an e-commerce application.

It is a **miniature data platform** built to teach Data Engineering from first principles.

The application database exists only to generate realistic business events.

The focus of the workshop is to answer one question:

> **"What happens to application data after it is created?"**

The audience should gradually discover why Data Engineering exists rather than being told upfront.

---

# 2. Learning Journey

The workshop follows a story instead of individual technologies.

```
A startup launches
        ↓
Application database grows
        ↓
Analytics become slow
        ↓
Need a warehouse
        ↓
Need ETL
        ↓
Need incremental synchronization
        ↓
Need CDC
        ↓
Need semantic layer
        ↓
AI can finally answer business questions correctly
```

Every new technology is introduced only after the previous architecture becomes insufficient.

---

# 3. Guiding Principles

1. Every technology must solve a problem introduced just before it.
2. No unnecessary abstractions.
3. Every lesson ends with runnable software.
4. Every lesson ends with a Git commit.
5. Architecture changes require strong justification.
6. The generator is **supporting code**, not the main project.
7. The data platform is the main project.

---

# 4. Current Architecture

```
Project Root

│
├── postgres/
│
├── generator/
│
├── warehouse/
│
├── etl/
│
├── semantic/
│
├── ai/
│
├── docs/
│
└── tests/
```

This architecture is frozen unless a genuine design issue is discovered.

---

# 5. Current Progress

| Module              | Status         |
| ------------------- | -------------- |
| Environment         | ✅ Complete     |
| Docker + PostgreSQL | ✅ Complete     |
| OLTP Schema         | ✅ Complete     |
| Project Structure   | ✅ Complete     |
| Customer Generator  | ✅ Complete     |
| Product Generator   | 🟡 In Progress |
| Inventory           | ⬜ Pending      |
| Orders              | ⬜ Pending      |
| Payments            | ⬜ Pending      |
| Warehouse           | ⬜ Pending      |
| ETL                 | ⬜ Pending      |
| CDC                 | ⬜ Pending      |
| Semantic Layer      | ⬜ Pending      |
| AI Analyst          | ⬜ Pending      |
| Workshop UI         | ⬜ Pending      |

Overall Progress: **~35%**

---

# 6. Workshop Roadmap

## Phase 1 – Build the Business

Goal:

Create a realistic OLTP database.

Deliverables:

* Customers
* Products
* Categories
* Inventory
* Orders
* Payments

Once complete:

**Freeze the generator.**

No new features.

---

## Phase 2 – Build the Warehouse

Audience discovers:

Production queries are becoming slow.

Need:

Separate analytics database.

Technology:

DuckDB.

---

## Phase 3 – ETL

Teach:

* Full Refresh
* Incremental Load
* Metadata table
* Scheduling

---

## Phase 4 – CDC

Show why polling isn't enough.

Introduce:

Change Data Capture.

---

## Phase 5 – Analytics

Run real business questions.

Examples:

* Revenue
* Top Products
* Customer Lifetime Value
* Return Rate
* Inventory Health

---

## Phase 6 – Semantic Layer

Introduce:

Business metadata.

Examples:

* Revenue
* Active Customer
* Gross Sales
* Net Sales

Demonstrate why column names alone are insufficient.

---

## Phase 7 – Local AI Analyst

Using:

* Ollama
* Local LLM
* Semantic Layer

The AI generates SQL over the warehouse.

Without metadata it struggles.

With metadata it succeeds.

---

# 7. Definition of Done

A lesson is complete only if it contains:

* Objective
* Code
* Commands
* Verification
* Git Commit
* Guide Update

If any of these are missing, the lesson is incomplete.

---

# 8. Technical Decisions

## Why PostgreSQL?

Represents a production OLTP database.

---

## Why DuckDB?

Runs locally.

Zero setup.

Excellent analytics engine.

Perfect for workshops.

---

## Why Ollama?

No API keys.

Offline.

Open source.

---

## Why Python?

Simple.

Readable.

Industry standard.

---

# 9. Current Risks

* Keep the OLTP generator intentionally simple.
* Avoid spending too much time building an application.
* Prioritize Data Engineering concepts over software engineering patterns.

---

# 10. Next Milestone

## First Complete Purchase

A single business event will:

* Create an order
* Create order items
* Reduce inventory
* Create payment

This marks the completion of the OLTP application and the beginning of the actual Data Engineering journey.
