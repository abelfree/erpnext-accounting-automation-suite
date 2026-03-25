from __future__ import annotations

import frappe


def generate_monthly_invoices():
    contracts = frappe.get_all(
        "Subscription",
        filters={"status": "Active"},
        fields=["name", "party", "plans", "next_invoice_date"],
    )

    today = frappe.utils.today()
    for contract in contracts:
        if str(contract.next_invoice_date) != str(today):
            continue

        invoice = frappe.get_doc(
            {
                "doctype": "Sales Invoice",
                "customer": contract.party,
                "posting_date": today,
                "due_date": frappe.utils.add_days(today, 30),
                "items": [
                    {
                        "item_code": "SUBSCRIPTION-FEE",
                        "qty": 1,
                        "rate": 100,
                    }
                ],
            }
        )
        invoice.insert(ignore_permissions=True)

    frappe.db.commit()
