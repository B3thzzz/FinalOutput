# Constants
COURSES_FILE = 'courses.txt'
ATTENDANCE_FILE = 'attendance.txt'
GRADES_FILE = 'grades.txt'
ASSIGNMENTS_FILE = 'assignments.txt'
ENROLL_FILE = 'enroll.txt'
COURSE_MATERIALS_FILE = 'course_materials.txt'  # New file for course materials
SCHEDULE_FILE = 'schedules.txt'  # New file for course schedules
REPORT_FILE = 'reports.txt'  # New file for saving reports


# Function to create a new course
def create_course(course_name, course_description, course_schedule, course_materials):
    if not course_name:
        print("Course name cannot be empty.")
        return

    # Validate course schedule (simple validation for example)
    if not validate_schedule(course_schedule):
        print("Invalid course schedule.")
        return

    try:
        with open(COURSES_FILE, 'a') as file:
            file.write(f"{course_name},{course_description}\n")  # Save only name and description

        # Save the course schedule in a separate file
        with open(SCHEDULE_FILE, 'a') as file:
            file.write(f"{course_name},{course_schedule}\n")  # Save course name and schedule

        # Save course materials directly from user input
        if course_materials:
            # Assuming course_materials is a comma-separated string of links
            materials_links = course_materials.split(',')
            materials_links_str = ','.join([link.strip() for link in materials_links])

            with open(COURSE_MATERIALS_FILE, 'a') as file:
                file.write(f"{course_name},{materials_links_str}\n")

        print("Course created successfully.")
    except Exception as e:
        print(f"Error while creating course: {e}")

        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        from google.oauth2 import service_account

        def upload_to_drive(file_path):
            SCOPES = ['https://www.googleapis.com/auth/drive.file']
            SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

            credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

            service = build('drive', 'v3', credent11ials=credentials)

            file_metadata = {'name': file_path.split('/')[-1]}
            media = MediaFileUpload(file_path, mimetype='text/plain')
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            # Get the file ID and create a shareable link
            file_id = file.get('id')
            shareable_link = f"https://drive.google.com/file/d/{file_id}/view"

            return shareable_link

# Function to validate course schedule
def validate_schedule(schedule):
    # Placeholder for schedule validation logic
    return True  # Assume all schedules are valid for this example


# Function to enroll a student in a course
def enroll_student(course_name, student_id, student_name):
    try:
        with open(COURSES_FILE, 'r') as file:
            courses = file.readlines()

        # Print the courses for debugging
        print("Available courses:")
        for course in courses:
            print(course.strip())

        # Check for exact course match
        course_found = any(course_name.strip() == course.split(',')[0].strip() for course in courses)

        if course_found:
            with open(ENROLL_FILE, 'a') as file:
                file.write(f"{course_name},{student_id},{student_name}\n")  # Corrected formatting
            print(f"Student {student_name} (ID: {student_id}) enrolled in {course_name}.")
        else:
            print("Course not found.")
    except Exception as e:
        print(f"Error while enrolling student: {e}")

# Function to remove a student from a course
def remove_student(course_name, student_id):
    try:
        with open(ENROLL_FILE, 'r') as file:
            enrollments = file.readlines()

        # Print current enrollments for debugging
        print("Current enrollments:")
        for enrollment in enrollments:
            print(f"'{enrollment.strip()}'")  # Show each enrollment clearly

        # Create the string to match for removal
        # Note: We need to include student_name in the comparison
        enrollment_to_remove = f"{course_name.strip()},{student_id.strip()}"
        print(f"Attempting to remove: '{enrollment_to_remove}'")

        with open(ENROLL_FILE, 'w') as file:
            found = False  # Flag to check if we found the enrollment
            for enrollment in enrollments:
                if enrollment.startswith(enrollment_to_remove):
                    found = True
                    print(f"Removed: '{enrollment.strip()}'")  # Confirm removal
                else:
                    file.write(enrollment)

        if found:
            print(f"Student {student_id} removed from {course_name}.")
        else:
            print(f"No enrollment found for student {student_id} in {course_name}.")
    except FileNotFoundError:
        print(f"Error: The file '{ENROLL_FILE}' does not exist.")
    except IOError as e:
        print(f"Error while accessing the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to grade an assignment
def grade_assignment(student_id, course_name, grade):
    try:
        with open(GRADES_FILE, 'a') as file:
            file.write(f"{student_id},{course_name},{grade}\n")
        print(f"Grade {grade} recorded for student {student_id} in {course_name}.")
    except Exception as e:
        print(f"Error while grading assignment: {e}")


# Function to add an assignment
def add_assignment(course_name, assignment_name):
    try:
        with open(ASSIGNMENTS_FILE, 'a') as file:
            file.write(f"{course_name},{assignment_name}\n")
        print(f"Assignment '{assignment_name}' added to course '{course_name}'.")
    except Exception as e:
        print(f"Error while adding assignment: {e}")


# Function to track attendance
def track_attendance(course_name, student_id, status):
    try:
        with open(ATTENDANCE_FILE, 'a') as file:
            file.write(f"{course_name},{student_id},{status}\n")
        print(f"Attendance recorded for student {student_id} in {course_name}.")
    except Exception as e:
        print(f"Error while tracking attendance: {e}")


# Function to generate a report
def generate_report(course_name):
    try:
        with open(GRADES_FILE, 'r') as file:
            grades = file.readlines()

        report_lines = []  # List to hold report lines
        report_lines.append(f"Report for {course_name}:\n")

        for grade in grades:
            if course_name in grade:
                report_lines.append(grade.strip() + "\n")

        # Print the report to the console
        print("".join(report_lines))

        # Save the report to a text file
        with open(REPORT_FILE, 'a') as report_file:
            report_file.writelines(report_lines)

        print(f"Report saved to {REPORT_FILE}.")
    except Exception as e:
        print(f"Error while generating report: {e}")

# Menu-driven system for teacher functionalities
def teacher_menu():
    while True:
        print("\nTeacher Menu:")
        print("1. Create Course")
        print("2. Enroll Student")
        print("3. Remove Student")
        print("4. Grade Assignment")
        print("5. Add Assignment")
        print("6. Track Attendance")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            course_name = input("Enter course name: ")
            course_description = input("Enter course description: ")
            course_schedule = input("Enter course schedule: ")
            course_materials = input("Enter course materials (comma-separated): ")  # New input for materials
            create_course(course_name, course_description, course_schedule, course_materials)
        elif choice == '2':
            course_name = input("Enter course name: ")
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            enroll_student(course_name, student_id, student_name)  # Now this matches the updated function
        elif choice == '3':
            course_name = input("Enter course name: ")
            student_id = input("Enter student ID: ")
            remove_student(course_name, student_id)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = input("Enter grade: ")
            grade_assignment(student_id, course_name, grade)
        elif choice == '5':
            course_name = input("Enter course name: ")
            assignment_name = input("Enter assignment name: ")
            add_assignment(course_name, assignment_name)
        elif choice == '6':
            course_name = input("Enter course name: ")
            student_id = input("Enter student ID: ")
            status = input("Enter attendance status (Present/Absent): ")
            track_attendance(course_name, student_id, status)
        elif choice == '7':
            course_name = input("Enter course name: ")
            generate_report(course_name)
        elif choice == '8':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")


# Start the teacher menu
if __name__ == "__main__":
    teacher_menu()