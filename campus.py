# Melsoft Campus Manager
# Python Essentials 1 Capstone Group Project
# Team 2

# Team Members
# Xayan Lovell
# Tetlanyo Leshogo
# Remofilwe Molehabangwe

# Workstream A
# Reads and validates a whole number within a given range.
def read_valid_number(prompt, low, high):

    while True:
        try:
            number = int(input(prompt))
            if number < low or number > high:
                print("Please enter a number between", low, "and", high)
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Workstream A
# Adds a new course with validated input and an empty roster.
def add_course(courses):
    global next_course_number
    name = input("Enter course name: ").strip()
    if name == "":
        print("Course name cannot be blank.")
        return
    capacity = read_valid_number("Enter course capacity: ", 1, 100)
    pass_mark = read_valid_number("Enter pass mark: ", 0, 100)

    course_id = "C" + str(next_course_number)
    courses[course_id] = {
        "name": name,
        "capacity": capacity,
        "pass_mark": pass_mark,
        "roster": []
    }
    next_course_number = next_course_number + 1
    print(f"Added {course_id}: {name} (capacity {capacity}, pass mark {pass_mark})")



# Workstream B
# Registers a new student.
def register_student(students):
    pass


# Workstream A
# Enrols a student into a course, after validating ALL rules.
def enrol_student(courses, students):
    student_id = input("Student ID: ")
    if student_id not in students:
        print("No such student.")
        return

    course_id = input("Course ID: ")
    if course_id not in courses:
        print("No such course.")
        return

    if len(courses[course_id]["roster"]) >= courses[course_id]["capacity"]:
        print(course_id, "is full (" + str(len(courses[course_id]["roster"])) + " of " + str(courses[course_id]["capacity"]) + " enrolled).")
        return

    if course_id in students[student_id]["enrolments"]:
        print("Student is already enrolled in this course.")
        return

    courses[course_id]["roster"].append(student_id)
    students[student_id]["enrolments"][course_id] = []
    print(student_id, "enrolled in", course_id + ":", courses[course_id]["name"])

    
# Workstream B
# Records a mark for a student.
def record_mark(courses, students):
    pass


# Workstream B
# Returns the average for one student in one course.
def course_average_for(students, student_id, course_id):
    pass


# Workstream B
# Displays one student's transcript.
def student_transcript(courses, students):
    pass


# Workstream C
# Displays one course report.
def course_report(courses, students):
    pass


# Workstream C
# Searches students and courses.
def search_everything(courses, students):
    pass


# Workstream A
# Withdraws a student from a course.
def withdraw_student(courses, students):

    student_id = input("Student ID: ")
    if student_id not in students:
        print("No such student.")
        return

    student_id = input("Course ID: ")
    if course_id not in courses:
        print("No such course.")
        return

    if course_id not in students[student_id]["enrolments"]:
        print("Student is not enrolled in course. ")
        return
    
    marks = students[student_id]["enrolments"][course_id]

    confirmation = input(
        "Withdraw " + student_id + " from " + course_id + ": "
        + courses[course_id]["name"] + "? Their "
        + str(len(marks)) + " marks will be deleted. (y/n)"
    ).lower()
    if confirmation !="y":
        print("Withdrawal cancelled.")
        return

    courses[course_id]["roster"].remove(student_id)
    del students[student_id]["enrolments"][course_id]
    print(student_id, "withdrawn from", course_id + ":",
          courses[course_id]["name"])
    


# Workstream C
# Returns academy totals as a tuple.
def academy_totals(students):
    pass


# Workstream C
# Returns the best performing course.
def best_course(courses, students):
    pass


# Workstream C
# Displays the academy report.
def academy_report(courses, students):
    pass

# ---- Main Program ----

courses = {}
students = {}

next_course_number = 1
next_student_number = 1

while True:
    print("\n===== MELSOFT CAMPUS MANAGER =====")
    print("1. Add a course")
    print("2. Register a student")
    print("3. Enrol a student for a course")
    print("4. Record a mark")
    print("5. Student transcript")
    print("6. Course report")
    print("7. Search")
    print("8. Withdraw a student from a course")
    print("9. Academy report")
    print("10. Exit")

    choice = input("Choose an option (1-10): ")

    if choice == "1":
        add_course(courses)

    elif choice == "2":
        register_student(students)

    elif choice == "3":
        enrol_student(courses, students)

    elif choice == "4":
        record_mark(courses, students)

    elif choice == "5":
        student_transcript(courses, students)

    elif choice == "6":
        course_report(courses, students)

    elif choice == "7":
        search_everything(courses, students)

    elif choice == "8":
        withdraw_student(courses, students)

    elif choice == "9":
        academy_report(courses, students)

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1-10.")