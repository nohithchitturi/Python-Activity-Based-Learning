# 1. Input Room Capacities
capacity = {}
num_rooms = int(input("Enter the number of rooms: "))

for i in range(num_rooms):
    room_name = input(f"Enter name for Room {i+1} (e.g., Room1): ").strip()
    cap = int(input(f"Enter capacity for {room_name}: "))
    capacity[room_name] = cap

print("\n--- Enter Course Details ---")

# 2. Input Course Information
courses = []
num_courses = int(input("Enter the total number of courses: "))

for i in range(num_courses):
    print(f"\nCourse #{i+1}:")
    course_name = input("  Course Name: ").strip()
    room_name = input("  Room Assigned: ").strip()
    period = int(input("  Period Number: "))
    students = int(input("  Number of Students: "))
    
    courses.append((course_name, room_name, period, students))

print("\n" + "="*30)
print("       CHECK RESULTS       ")
print("="*30 + "\n")

# 3. Check for Room Capacities and Schedule Clashes
for course, room, period, students in courses:
    print(f"{course} | {room} | Period: {period}")

    # Check if the room exists in capacities and if students exceed capacity
    if room in capacity:
        if students > capacity[room]:
            print("   Capacity exceeded")
    else:
        print("   Room capacity unknown (Room not found)")

    # Check for room schedule clashes
    clash = False
    for other in courses:
        if other != (course, room, period, students):
            if other[1] == room and other[2] == period:
                clash = True
                break

    if clash:
        print("   Room clash detected")
    else:
        print("   No room clash")
    print("-" * 25)
