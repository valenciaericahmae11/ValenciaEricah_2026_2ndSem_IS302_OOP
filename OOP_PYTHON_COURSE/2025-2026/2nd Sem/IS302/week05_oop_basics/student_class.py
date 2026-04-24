class Student:
    def __init__(self, name, student_id, course):
        self.name_EIV = name
        self.student_id_EIV = student_id
        self.course_EIV = course

    def display_student(self):
        print("Name:", self.name_EIV)
        print("Student ID:", self.student_EIV)
        print("Course:", self.course_EIV)


student1 = Student("Maria", "2023-001", "BSIS")
student1.display_student()

