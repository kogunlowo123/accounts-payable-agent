# Accounts Payable Agent

[![CI](https://github.com/kogunlowo123/accounts-payable-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/accounts-payable-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Finance | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Accounts payable agent that manages vendor payments, optimizes payment timing for cash flow, processes payment batches, handles early payment discounts, and reconciles AP ledger.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `process_payment_batch` | Process a batch of vendor payments |
| `optimize_payment_timing` | Optimize payment timing for cash flow and early payment discounts |
| `apply_early_payment_discount` | Calculate and apply early payment discount terms |
| `reconcile_ap` | Reconcile accounts payable ledger with bank statements |
| `generate_aging_report` | Generate accounts payable aging report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/accounts-payable/process` | Process transaction |
| `POST` | `/api/v1/accounts-payable/analyze` | Analyze data |
| `POST` | `/api/v1/accounts-payable/validate` | Validate |
| `POST` | `/api/v1/accounts-payable/report` | Generate report |
| `GET` | `/api/v1/accounts-payable/audit` | Get audit trail |

## Features

- Accounts
- Payable
- Compliance
- Reporting

## Integrations

- Netsuite
- Quickbooks
- Xero
- Sap
- Oracle Financials

## Architecture

```
accounts-payable-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── accounts_payable_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ERP + Accounting Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
