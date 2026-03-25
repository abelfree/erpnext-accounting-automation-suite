def match_by_amount(amount, open_invoices):
    for inv in open_invoices:
        if inv["outstanding_amount"] == amount:
            return inv["name"]
    return None


def test_match_by_amount():
    invoices = [
        {"name": "ACC-SINV-0001", "outstanding_amount": 100},
        {"name": "ACC-SINV-0002", "outstanding_amount": 250},
    ]
    assert match_by_amount(250, invoices) == "ACC-SINV-0002"
