def load_students(filename):
    """Load student data from a text file."""
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:  # Ensure there are exactly 5 parts
                    tp, name, contact, age, parents = parts
                    students.append({
                        'TP': tp.strip(),
                        'name': name.strip(),
                        'contact': contact.strip(),
                        'age': age.strip(),
                        'parents': parents.strip()
                    })
    except FileNotFoundError:
        print("Students file not found.")
    return students

def save_students(filename, students):
    """Save updated student data back to the text file."""
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student['TP']},{student['name']},{student['contact']},{student['age']},{student['parents']}\n")

def authenticate_user(students):
    """Handle user login and return the user if successful."""
    print("Welcome to the Student Management System")

    while True:
        has_account = input("Do you have a student account? (yes/no): ").strip().lower()
        if has_account in ['yes', 'no']:
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    if has_account == 'yes':
        username = input("Enter your name: ").strip()
        for student in students:
            if student['name'].lower() == username.lower():
                print("Login successful! Welcome, {}.".format(username))
                return student
        print("Login failed! Please check your name.")
        return None
    else:
        return create_account(students)

def create_account(students):
    """Create a new student account."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    contact = input("Enter your contact number: ")
    parents = input("Enter your parents' name: ")
    tp = input("Enter your TP number: ")

    new_student = {
        'TP': tp.strip(),
        'name': name.strip(),
        'contact': contact.strip(),
        'age': age.strip(),
        'parents': parents.strip()
    }

    students.append(new_student)
    save_students('Student_list.txt', students)
    print("Account created successfully! Welcome, {}.".format(name))
    return new_student

def get_feedback():
    """Collect feedback from the student."""
    print("Feedback Submission")

    student_name = input("Enter your name: ")
    course = input("Feedback on course: ")
    lecturer = input("Feedback on lecturer: ")
    academic_performance = input("Feedback on academic performance: ")

    feedback_entry = f"Student: {student_name}\nCourse: {course}\nLecturer: {lecturer}\nAcademic Performance: {academic_performance}\n{'-' * 40}\n"
    return feedback_entry

def save_feedback(feedback_entry):
    """Save feedback to a text file."""
    with open("Student_feedback.txt", "a") as file:
        file.write(feedback_entry)
    print("Thank you for your feedback!")

def view_grades(student_name):
    """Display the grades for the specified student."""
    if not student_name:
        print("Student name cannot be empty.")
        return
    try:
        with open('grades.txt', 'r') as file:
            grades_found = False
            print(f"Grades for {student_name}:")

            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3 and parts[0].strip().lower() == student_name.lower():
                    grades_found = True
                    print(f"Course: {parts[1].strip()}, Grade: {parts[2].strip()}")

            if not grades_found:
                print("No grades found for this student.")
    except FileNotFoundError:
        print("Grades file not found.")

def access_options(user_found, students):
    """Provide options for the logged-in user."""
    while True:
        print("\nChoose an option:")
        print("1. View Profile")
        print("2. Update Contact Number")
        print("3. Student List")
        print("4. Courses")
        print("5. Course Material")
        print("6. Student Grades")
        print("7. Feedback Submission")
        print("8. Logout")
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            print(f"TP: {user_found['TP']}")
            print(f"Name: {user_found['name']}")
            print(f"Contact: {user_found['contact']}")
            print(f"Age: {user_found['age']}")
            print(f"Parents: {user_found['parents']}")
              # Display TP ID

        elif choice == '2':
            new_contact = input("Enter new contact number: ")
            user_found['contact'] = new_contact
            save_students('Student_list.txt', students)
            print("Profile updated successfully!")

        elif choice == '3':
            print("List of all students:")
            for student in students:
                print(f"Name: {student['name']}, Contact: {student['contact']}, Age: {student['age']}, Parents: {student['parents']}, TP: {student['TP']}")

        elif choice == '4':
            def view_courses():
                try:
                    with open('Courses.txt', 'r') as file:
                        courses = file.readlines()

                    print("Available Courses:")
                    for index, course in enumerate(courses, start=1):
                        print(f"{index}. {course.strip()}")
                except FileNotFoundError:
                    print("Courses file not found.")

            def enroll_in_course(student_name):
                view_courses()
                try:
                    course_choice = int(input("Enter the course code: "))
                    with open('Courses.txt', 'r') as file:
                        courses = file.readlines()

                    if 1 <= course_choice <= len(courses):
                        selected_course = courses[course_choice - 1].strip()
                        print(f"You have successfully enrolled in: {selected_course}")

                        with open('Course_student.txt', 'a') as list_file:
                            list_file.write(f"{student_name}: {selected_course}\n")
                        print("Your enrollment has been saved.")
                    else:
                        print("Invalid course number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            enroll_in_course(user_found['name'])

        elif choice == '5':
            def course_file(filename):
                """Open a text file with name and link format and print its contents."""
                try:
                    with open(filename, 'r') as file:
                        for line in file:
                            parts = line.strip().split(',')
                            if len(parts) == 2:
                                course = parts[0].strip()
                                link = parts[1].strip()
                                print(f"Course: {course}, Link: {link}")
                            else:
                                print(f"Warning: Invalid line format: {line.strip()}")
                except FileNotFoundError:
                    print(f"The file '{filename}' was not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")

            course_file('course_materials.txt')

        elif choice == '6':
            view_grades(user_found['name'])

        elif choice == '7':
            feedback_entry = get_feedback()
            save_feedback(feedback_entry)

        elif choice == '8':
            print("Thank You. Have a nice day!!!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    filename = 'Student_list.txt'
    students = load_students(filename)

    user_found = authenticate_user(students)
    if user_found:
        access_options(user_found, students)

    save_students(filename, students)

if __name__ == "__main__":
    main()