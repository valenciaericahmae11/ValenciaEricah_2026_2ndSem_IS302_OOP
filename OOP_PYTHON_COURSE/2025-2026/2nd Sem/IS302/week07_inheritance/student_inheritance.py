class Person_EIV:
    def __init__(self_EIV, name_EIV, age_EIV):
        self_EIV.name_EIV = name_EIV
        self_EIV.age_EIV = age_EIV

class Student_EIV(Person_EIV):
    def __init__(self_EIV, name_EIV, age_EIV, course_EIV):
        super().__init__(name_EIV, age_EIV)
        self_EIV.course_EIV = course_EIV

    def display_student_EIV(self_EIV):
        print("Name:", self_EIV.name_EIV)
        print("Age:", self_EIV.age_EIV)
        print("Course:", self_EIV.course_EIV)

student1_EIV = Student_EIV("Maria", 20, "BSIS")
student1_EIV.display_student_EIV()
