"""Payment processing module."""

class PaymentProcessor:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def charge(self, amount: float, currency: str = "USD") -> dict:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return {
            "amount": amount,
            "currency": currency,
            "status": "success",
            "transaction_id": "txn_12345",
        }

    def refund(self, transaction_id: str) -> dict:
        return {
            "transaction_id": transaction_id,
            "status": "refunded",
        }
