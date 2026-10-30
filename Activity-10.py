
courses = [
    ("Python", "Room1", 1, 40),
    ("Maths", "Room1", 1, 30),
    ("English", "Room2", 2, 25)
]

capacity = {"Room1": 50, "Room2": 30}

for course, room, period, students in courses:
    print(course, room, "Period:", period)

    if students > capacity[room]:
        print("Capacity exceeded")

    clash = False

    for other in courses:
        if other != (course, room, period, students):
            if other[1] == room and other[2] == period:
                clash = True

    if clash:
        print("Room clash detected")
    else:
        print("No room clash")
