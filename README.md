# ERPNext Accounting Automation Suite

Automation toolkit for repetitive accounting tasks in ERPNext.

## Features
- Monthly recurring invoice generation
- Dunning reminders for overdue invoices
- Bank statement CSV parser and matching suggestions

## Scheduler Setup
- Daily: generate recurring invoices
- Daily: send overdue reminders

## Endpoints
- `POST /api/method/accounting_automation.api.reconcile.suggest_matches`
