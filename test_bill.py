
from getbill import get_bill

def get_bill_test():
    items = [
        ("Apple", 2, 0.5),
        ("Banana", 3, 0.3),
        ("Milk", 1, 1.2)
    ]
    expected_total = 2 * 0.5 + 3 * 0.3 + 1 * 1.2
    assert get_bill(items) == expected_total, "Test failed!"
    print("Test passed!")