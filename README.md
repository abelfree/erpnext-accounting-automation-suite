# ERPNext Accounting Automation Suite

[![ERPNext](https://img.shields.io/badge/ERPNext-v15-blue)](https://erpnext.com/)
[![Accounting](https://img.shields.io/badge/Domain-Accounting-2ea44f)](https://docs.erpnext.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Automation toolkit for finance teams: recurring invoicing, overdue reminders, and reconciliation suggestions.

## Author
Abel Takele

## What This Project Demonstrates
- Scheduled automation jobs in ERPNext
- Automated invoice generation workflows
- Reminder delivery for overdue accounts receivable
- CSV-based bank reconciliation helper API

## Key Features
- Daily creation of recurring invoices for active subscriptions
- Daily reminder emails for overdue invoices
- Statement CSV parser that suggests invoice matches by amount

## Architecture
- `accounting_automation/hooks.py`: scheduler registration
- `accounting_automation/accounting_automation/services/recurring.py`: recurring billing engine
- `accounting_automation/accounting_automation/services/reminders.py`: dunning reminder service
- `accounting_automation/accounting_automation/api/reconcile.py`: reconciliation suggestion API

## API Endpoint
- `POST /api/method/accounting_automation.api.reconcile.suggest_matches`

## Quick Start
```bash
bench get-app accounting_automation https://github.com/abelfree/erpnext-accounting-automation-suite
bench --site yoursite install-app accounting_automation
```

## Demo Flow
1. Ensure active `Subscription` records exist.
2. Run daily scheduler and verify generated `Sales Invoice` records.
3. Mark invoices overdue and run reminders task.
4. Submit `scripts/sample_statement.csv` to reconciliation endpoint.

## Recruiter Notes
This project highlights practical ERP accounting automation and backend business process implementation in Frappe.
