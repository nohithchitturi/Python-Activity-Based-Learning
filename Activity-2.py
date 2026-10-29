
balance = 1000
n = int(input("Enter number of transactions: "))

for i in range(n):
    action = input("Enter deposit or withdraw: ").lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif action == "deposit":
        balance += amount
    elif action == "withdraw":
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")
    else:
        print("Invalid transaction")

print("Final balance:", balance)
#13 question