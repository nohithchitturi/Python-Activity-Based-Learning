
rows = int(input("Enter number of rows: "))
cols = int(input("Enter seats per row: "))

for i in range(rows):
    for j in range(cols):
        print("R", i + 1, "S", j + 1, end="  ")
    print()
#26 question