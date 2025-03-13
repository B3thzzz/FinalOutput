def get_file_paths():
    return {
        "users": {
            "Teacher": "teacher.txt",
            "Staff": "staff.txt",
            "Student": "student_list.txt"
        },
        "courses": "courses.txt",
        "schedules": "schedule.txt",
        "grades": "grades.txt",
        "attendance": "attendance.txt",
        "financial": "financial_records.txt"
    }


# Helper function to check if a phone number is valid (digits only)
def validate_phone_number(phonenum):
    return phonenum.isdigit()


# Helper function to load data from a file
def load_data(file_name):
    data = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                data.append(parts)
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return data


# Helper function to save data to a file
def save_data(file_name, data):
    with open(file_name, "w") as file:
        for item in data:
            file.write(",".join(item) + "\n")  # Write each item as a line in the file


# Function to manage users (students only for now)
def manage_users(file_paths):
    students = []
    for entry in load_data(file_paths["users"]["Student"]):
        if len(entry) == 5:
            students.append(
                {"TP ID": entry[0], "Name": entry[1], "Phone": entry[2], "Age": entry[3], "Parent Name": entry[4]})
        else:
            print(f"Invalid student entry: {entry}")  # Debugging information

    while True:
        print("\nSTUDENT MANAGEMENT")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":  # Add a new student
            tp_id = input("Enter TP ID: ")
            if any(s["TP ID"] == tp_id for s in students):
                print("Error: TP ID already exists!")
                continue

            name = input("Enter student name: ")
            if any(s["Name"] == name for s in students):
                print("Error: Username already exists!")
                continue

            phone = input("Enter phone number: ")
            age = input("Enter age: ")
            parent_name = input("Enter parent's name: ")
            students.append({"TP ID": tp_id, "Name": name, "Phone": phone, "Age": age, "Parent Name": parent_name})
            save_data(file_paths["users"]["Student"],
                      [[s["TP ID"], s["Name"], s["Phone"], s["Age"], s["Parent Name"]] for s in students])
            print("Student added!")

        elif choice == "2":  # View students
            tp_id = input("Enter TP ID to view a specific student (or press Enter to view all): ")
            if tp_id:
                student = next((s for s in students if s["TP ID"] == tp_id), None)
                if student:
                    print(student)
                else:
                    print("Student not found.")
            else:
                if not students:
                    print("No students available.")
                else:
                    for student in students:
                        print(student)

        elif choice == "3":  # Delete a student
            tp_id = input("Enter TP ID to delete: ")
            students = [s for s in students if s["TP ID"] != tp_id]
            save_data(file_paths["users"]["Student"],
                      [[s["TP ID"], s["Name"], s["Phone"], s["Age"], s["Parent Name"]] for s in students])
            print("Student deleted!")

        elif choice == "4":  # Exit
            break
        else:
            print("Invalid choice!")


# Function to manage courses
def manage_courses(file_paths):
    courses = []
    for entry in load_data(file_paths["courses"]):
        if len(entry) >= 3:
            courses.append({"ID": entry[0], "Name": entry[1], "Instructor": entry[2]})
        else:
            print(f"Invalid course entry: {entry}")  # Debugging information

    while True:
        print("\nCOURSE MANAGEMENT")
        print("1. Create Course")
        print("2. Update Course")
        print("3. Delete Course")
        print("4. Assign Instructor")
        print("5. View Courses")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":  # Create a new course
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            instructor = input("Enter instructor (optional): ") or "None"
            courses.append({"ID": course_id, "Name": course_name, "Instructor": instructor})
            save_data(file_paths["courses"],
                      [[course["ID"], course["Name"], course["Instructor"]] for course in courses])
            print("Course created!")

        elif choice == "3":  # Delete a course
            course_id = input("Enter course ID to delete: ")
            courses = [course for course in courses if course["ID"] != course_id]
            save_data(file_paths["courses"],
                      [[course["ID"], course["Name"], course["Instructor"]] for course in courses])
            print("Course deleted!")

        elif choice == "5":  # View all courses
            if not courses:
                print("No courses available.")
            else:
                for course in courses:
                    print(course)

        elif choice == "6":  # Exit
            break
        else:
            print("Invalid choice!")


# Main program
def admin():
    file_paths = get_file_paths()
    while True:
        print("\nMAIN MENU")
        print("1. Account Management")
        print("2. Course Management")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_users(file_paths)  # Now it won't cause an error
        elif choice == "2":
            manage_courses(file_paths)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# Run the program
if __name__ == "__main__":
    admin()
