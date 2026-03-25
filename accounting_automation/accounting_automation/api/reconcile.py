from __future__ import annotations

import csv
from io import StringIO

import frappe


@frappe.whitelist(methods=["POST"])
def suggest_matches(statement_csv: str):
    rows = csv.DictReader(StringIO(statement_csv))
    suggestions = []

    for row in rows:
        amount = float(row["amount"])
        invoice_name = frappe.db.get_value(
            "Sales Invoice",
            {
                "docstatus": 1,
                "outstanding_amount": amount,
                "status": ["in", ["Unpaid", "Overdue"]],
            },
            "name",
        )

        suggestions.append(
            {
                "bank_ref": row.get("reference"),
                "amount": amount,
                "suggested_invoice": invoice_name,
            }
        )

    return {"matches": suggestions}
