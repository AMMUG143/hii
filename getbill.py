def get_bill(items):
    total = 0
    for item in items:
        name, quantity, price = item
        total += quantity * price
        print(f"{name}: {quantity} x {price} = {quantity * price}")
    print(f"Total Bill: {total}")
    return total

# Example usage
if __name__ == "__main__":
    items = [
        ("Apple", 2, 0.5),
        ("Banana", 3, 0.3),
        ("Milk", 1, 1.2)
    ]
    get_bill(items)