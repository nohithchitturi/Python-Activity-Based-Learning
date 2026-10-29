
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
required = int(input("Enter required attendance %: "))

percentage = attended / total * 100
print("Attendance:", percentage, "%")

if percentage >= required:
    print("Eligible")
else:
    needed = 0
    while (attended + needed) / (total + needed) * 100 < required:
        needed += 1
    print("Extra classes needed:", needed)
#12 question