# Import all modules
import admin
import teacher
import student
import staff

# Hardcoded users (username: password)
users = {
    "admin": "admin123",
    "staff": "staff123",
    "teacher": "teacher123",
    "student": "student123"
}

# Print welcome message
def print_welcome():
    print("-" * 50)
    print("\n W E L C O M E   T O   E D   G L O B A L\n")
    print("-" * 50)

# Handle user login
def login():
    print("\nPlease log in to continue.")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if users.get(username) == password:
        print(f"Welcome, {username}!")
        return username  # Return the role
    else:
        print("Invalid username or password. Try again.")
        return None

# Main function to route users to their respective modules
def main():
    print_welcome()
    user_role = None

    while not user_role:  # Keep asking until login is successful
        user_role = login()

    # Route to the appropriate module
    if user_role == "admin":
        admin.admin()  # Call admin module
    elif user_role == "teacher":
        teacher.teacher_menu()  # Call teacher module
    elif user_role == "student":
        student.main()  # Call student module
    elif user_role == "staff":
        staff.staff_menu()  # Call staff module
    else:
        print("Unknown role. Exiting...")

# Run the program
if __name__ == "__main__":
    main()
