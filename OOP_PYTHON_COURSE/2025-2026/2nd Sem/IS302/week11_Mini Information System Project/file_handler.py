def save_student(student):
    with open("students.txt", "a") as file:
        file.write(
            student.student_id_EMIV + "," +
            student.name_EMIV + "," +
            student.course_EMIV + "\n"
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
                student_id_EMIV, name_EMIV, course_EMIV = line.strip().split(",")

                print(f"ID: {student_id_EMIV}")
                print(f"Name: {name_EMIV}")
                print(f"Course: {course_EMIV}")
                print("-" * 30)

    except FileNotFoundError:
        print("No records found.")