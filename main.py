# User database to store user credentials
user_database = {}


def register_user(username, password):
    if username in user_database:
        return "Username already exists. Please choose a different username."
    else:
        user_database[username] = password
        return "Registration successful. You can now log in."


def login_user(username, password):
    if username in user_database and user_database[username] == password:
        return "Login successful. Welcome, {}!".format(username)
    else:
        return "Login failed. Invalid username or password."


class AttendanceSystem:
    def __init__(self):
        self.students = {}
        self.attendance_data = {}

    def add_student(self, id, name):
        self.students[id] = name

    def display_students(self):
        for id, name in self.students.items():
            print(f"ID: {id}, Name: {name}")

    def mark_attendance(self, id, date, status):
        if id not in self.students:
            return "Student not found."

        if date not in self.attendance_data:
            self.attendance_data[date] = {}

        if id in self.attendance_data[date]:
            return "Attendance already marked for this student on this date."

        self.attendance_data[date][id] = status
        return f"Attendance marked as {status} successfully."

    def view_attendance(self, date):
        if date in self.attendance_data:
            attendance_records = self.attendance_data[date]
            return f"Date: {date}\n{attendance_records}"
        else:
            return "No attendance data available for this date."

    def view_individual_attendance(self, id):
        if id not in self.students:
            return "Student not found."

        individual_attendance = {}
        for date, attendance_records in self.attendance_data.items():
            if id in attendance_records:
                individual_attendance[date] = attendance_records[id]

        if individual_attendance:
            return f"Attendance records for {self.students[id]}: {individual_attendance}"
        else:
            return f"No attendance records found for {self.students[id]}."


def main():
    user_authenticated = False
    attendance_system = AttendanceSystem()

    while True:
        if not user_authenticated:
            print("1. Register\n2. Login\n3. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                message = register_user(username, password)
                print(message)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                message = login_user(username, password)
                print(message)
                if "Welcome" in message:
                    user_authenticated = True

            elif choice == '3':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please choose again.")
        else:
            print(
                "\n1. Add Student\n2. Display Students\n3. Mark Attendance\n4. View Attendance\n5. View Individual Attendance\n6. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                id = input("Enter ID: ")
                name = input("Enter Name: ")
                attendance_system.add_student(id, name)
                print("Student added successfully.")

            elif choice == '2':
                attendance_system.display_students()

            elif choice == '3':
                id = input("Enter Student ID: ")
                date = input("Enter Date (YYYY-MM-DD): ")
                status = input("Enter Attendance Status (Present/Absent): ").lower()
                if status == "present" or status == "absent":
                    message = attendance_system.mark_attendance(id, date, status)
                    print(message)
                else:
                    print("Invalid status. Please enter 'Present' or 'Absent'.")

            elif choice == '4':
                date = input("Enter Date (YYYY-MM-DD): ")
                attendance = attendance_system.view_attendance(date)
                print(attendance)

            elif choice == '5':
                id = input("Enter Student ID: ")
                individual_attendance = attendance_system.view_individual_attendance(id)
                print(individual_attendance)

            elif choice == '6':
                user_authenticated = False
                print("Logged out.")

            else:
                print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()