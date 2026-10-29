
password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short")
elif not any(c.isdigit() for c in password):
    print("Add at least one number")
else:
    print("Valid password")
#29 question