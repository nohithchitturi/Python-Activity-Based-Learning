
products = [
    ("Pen", 10, 20),
    ("Book", 50, 5),
    ("Bag", 500, 0)
]

for name, price, stock in products:
    print("Product:", name)
    print("Price:", price)
    print("Stock:", stock)

    if stock == 0:
        print("Reorder required")
    else:
        print("Stock available")
