from __future__ import annotations

import frappe


def send_overdue_reminders():
    overdue = frappe.get_all(
        "Sales Invoice",
        filters={"docstatus": 1, "status": "Overdue"},
        fields=["name", "customer", "contact_email", "outstanding_amount", "due_date"],
    )

    for inv in overdue:
        if not inv.contact_email:
            continue
        frappe.sendmail(
            recipients=[inv.contact_email],
            subject=f"Payment Reminder: {inv.name}",
            message=(
                f"Dear {inv.customer},<br>"
                f"Invoice {inv.name} overdue since {inv.due_date}. "
                f"Outstanding amount: {inv.outstanding_amount}."
            ),
        )
