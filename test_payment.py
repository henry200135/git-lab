import pytest
from payment import PaymentProcessor

def test_charge_success():
    processor = PaymentProcessor("key_123")
    result = processor.charge(100.0)
    assert result["status"] == "success"
    assert result["amount"] == 100.0

def test_charge_negative_amount():
    processor = PaymentProcessor("key_123")
    with pytest.raises(ValueError, match="positive"):
        processor.charge(-50.0)

def test_refund():
    processor = PaymentProcessor("key_123")
    result = processor.refund("txn_12345")
    assert result["status"] == "refunded"
