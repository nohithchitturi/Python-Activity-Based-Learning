
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    row = []
    for j in range(subjects):
        m = int(input("Enter marks: "))
        row.append(m)
    marks.append(row)

for i in range(students):
    total = sum(marks[i])
    average = total / subjects
    print("Student", i + 1)
    print("Total:", total)
    print("Average:", average)
