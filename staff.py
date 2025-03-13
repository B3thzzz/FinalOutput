import os

# File paths
STUDENT_FILE = "student_list.txt"
SCHEDULE_FILE = "schedule.txt"
RESOURCE_FILE = "resources.txt"
EVENT_FILE = "events.txt"
COMMUNICATION_FILE = "communications.txt"

# Utility function to read a file
def read_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

# Utility function to write data to a file
def write_file(file_path, data):
    with open(file_path, "w") as file:
        for item in data:
            file.write(f"{item}\n")

# Function to manage student records
def manage_student_records():
    students = read_file(STUDENT_FILE)
    print("\n1. View Student Records\n2. Transfer Student")
    choice = input("Select an option: ").strip()

    if choice == "1":
        print("Student Records:")
        for student in students:
            print(student)
    elif choice == "2":
        student_id = input("Enter Student ID to transfer: ").strip()
        students = [s for s in students if not s.startswith(student_id)]
        write_file(STUDENT_FILE, students)
        print("Student transferred successfully.")

# Function to manage timetable
def manage_timetable():
    schedule = read_file(SCHEDULE_FILE)
    print("\n1. Schedule Class\n2. Reschedule Class")
    choice = input("Select an option: ").strip()

    if choice == "1":
        class_id = input("Enter Class ID: ").strip()
        time_slot = input("Enter Time Slot: ").strip()
        schedule.append(f"{class_id},{time_slot}")
        write_file(SCHEDULE_FILE, schedule)
        print("Class scheduled successfully.")
    elif choice == "2":
        class_id = input("Enter Class ID to reschedule: ").strip()
        new_time = input("Enter New Time Slot: ").strip()
        schedule = [s for s in schedule if not s.startswith(class_id)]
        schedule.append(f"{class_id},{new_time}")
        write_file(SCHEDULE_FILE, schedule)
        print("Class rescheduled successfully.")

# Function to allocate resources
def allocate_resources():
    resources = read_file(RESOURCE_FILE)
    print("\n1. Allocate Resource\n2. View Resources")
    choice = input("Select an option: ").strip()

    if choice == "1":
        resource_name = input("Enter Resource Name: ").strip()
        resources.append(resource_name)
        write_file(RESOURCE_FILE, resources)
        print("Resource allocated successfully.")
    elif choice == "2":
        print("Allocated Resources:")
        for resource in resources:
            print(resource)

# Function to manage events
def manage_events():
    events = read_file(EVENT_FILE)
    print("\n1. Create Event\n2. View Events")
    choice = input("Select an option: ").strip()

    if choice == "1":
        event_name = input("Enter Event Name: ").strip()
        events.append(event_name)
        write_file(EVENT_FILE, events)
        print("Event created successfully.")
    elif choice == "2":
        print("Scheduled Events:")
        for event in events:
            print(event)

# Function to manage communications
def manage_communications():
    messages = read_file(COMMUNICATION_FILE)
    print("\n1. Send Message\n2. View Messages")
    choice = input("Select an option: ").strip()

    if choice == "1":
        recipient = input("Enter Recipient (Student/Parent/Faculty): ").strip()
        message = input("Enter Message: ").strip()
        messages.append(f"To: {recipient} - {message}")
        write_file(COMMUNICATION_FILE, messages)
        print("Message sent successfully.")
    elif choice == "2":
        print("Messages:")
        for msg in messages:
            print(msg)

# Function to display menu
def staff_menu():
    while True:
        print("\nStaff Management System")
        print("1. Manage Student Records")
        print("2. Manage Timetable")
        print("3. Allocate Resources")
        print("4. Manage Events")
        print("5. Manage Communications")
        print("6. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            manage_student_records()
        elif choice == "2":
            manage_timetable()
        elif choice == "3":
            allocate_resources()
        elif choice == "4":
            manage_events()
        elif choice == "5":
            manage_communications()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the staff menu
if __name__ == "__main__":
    staff_menu()
