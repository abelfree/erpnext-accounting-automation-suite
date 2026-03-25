app_name = "accounting_automation"
app_title = "Accounting Automation"
app_publisher = "Portfolio"
app_description = "Invoice and reconciliation automation"
app_email = "dev@example.com"
app_license = "MIT"

scheduler_events = {
    "daily": [
        "accounting_automation.services.recurring.generate_monthly_invoices",
        "accounting_automation.services.reminders.send_overdue_reminders",
    ]
}
