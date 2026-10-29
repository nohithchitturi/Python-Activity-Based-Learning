
n = int(input("Enter number of exams: "))
marks = []

for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

print("Marks:", marks)

for i in range(1, n):
    if marks[i] > marks[i - 1]:
        print("Improved")
    elif marks[i] < marks[i - 1]:
        print("Declined")
    else:
        print("No change")
#17 question