def save_student(student):
    with open("students.txt", "a") as file:
        file.write(
            student.student_id_JFGA + "," +
            student.name_JHFGA + "," +
            student.course_JHFGA + "\n"
        )


def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found.")
                return

            print("\nLIST OF STUDENTS")
            print("-" * 30)

            for line in records:
                student_id_JFGA, name_JHFGA, course_JHFGA = line.strip().split(",")

                print(f"ID: {student_id_JFGA}")
                print(f"Name: {name_JHFGA}")
                print(f"Course: {course_JHFGA}")
                print("-" * 30)

    except FileNotFoundError:
        print("No records found.")