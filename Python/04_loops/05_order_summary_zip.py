orders = ["Hitest", "Aman", "Becky", "Carlos"]
bills = [50, 70, 100, 55]

for name, amount in zip(orders, bills):
    print(f"{name} paid $${amount}.")