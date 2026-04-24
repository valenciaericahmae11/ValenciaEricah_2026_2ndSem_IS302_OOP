class Person_EIV:
    def __init__(self_EIV, name_EIV, age_EIV):
        self_EIV.name_EIV = name_EIV
        self_EIV.age_EIV = age_EIV

    def display_info_EIV(self_EIV):
        print("Name:", self_EIV.name_EIV)
        print("Age:", self_EIV.age_EIV)

class Student_EIV(Person_EIV):
    def __init__(self_EIV, name_EIV, age_EIV, course_EIV):
        super().__init__(name_EIV, age_EIV)
        self_EIV.course_EIV = course_EIV

    def display_info_EIV(self_EIV):
        super().display_info_EIV()
        print("Course:", self_EIV.course_EIV)

class Teacher_EIV(Person_EIV):
    def __init__(self_EIV, name_EIV, age_EIV, subject_EIV):
        super().__init__(name_EIV, age_EIV)
        self_EIV.subject_EIV = subject_EIV

    def display_info_EIV(self_EIV):
        super().display_info_EIV()
        print("Subject:", self_EIV.subject_EIV)

# Example usage
student_EIV = Student_EIV("Maria", 20, "BSIS")
teacher_EIV = Teacher_EIV("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_EIV.display_info_EIV()
print("\nTeacher Info:")
teacher_EIV.display_info_EIV()
