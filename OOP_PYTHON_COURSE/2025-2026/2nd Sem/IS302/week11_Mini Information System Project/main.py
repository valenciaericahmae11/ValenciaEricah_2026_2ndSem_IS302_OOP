from student import Student
from file_handler import save_student, view_students


def add_student():
    try:
        student_id_EMIV = input("Enter Student ID: ").strip()
        name_EMIV = input("Enter Name: ").strip()
        course_EMIV = input("Enter Course: ").strip()

        if student_id_EMIV == "" or name_EMIV == "" or course_EMIV == "":
            raise ValueError("All fields are required.")

        student = Student(student_id_EMIV, name_EMIV, course_EMIV)

        save_student(student)

        print("Student added successfully.")

    except ValueError as error:
        print("Error:", error)


def search_student():
    search_id = input("Enter Student ID to search: ")

    try:
        with open("students.txt", "r") as file:
            found = False

            for line in file:
                student_id_EMIV, name_EMIV, course_EMIV = line.strip().split(",")

                if student_id_EMIV == search_id:
                    print("\nStudent Found")
                    print("-" * 30)
                    print(f"ID: {student_id_EMIV}")
                    print(f"Name: {name_EMIV}")
                    print(f"Course: {course_EMIV}")
                    found = True
                    break

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("No records available.")


while True:
    print("\nSTUDENT INFORMATION SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")