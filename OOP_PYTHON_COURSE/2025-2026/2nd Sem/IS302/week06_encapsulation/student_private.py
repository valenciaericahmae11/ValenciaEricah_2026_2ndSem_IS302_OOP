class Student_EIV:
    def __init__(self_EIV, name_EIV, student_id_EIV, gpa_EIV):
        self_EIV.__name_EIV = name_EIV
        self_EIV.__student_id_EIV = student_id_EIV
        self_EIV.__gpa_EIV = gpa_EIV

    def get_student_info_EIV(self_EIV):
        print("Name:", self_EIV.__name_EIV)
        print("Student ID:", self_EIV.__student_id_EIV)
        print("GPA:", self_EIV.__gpa_EIV)

student1_EIV = Student_EIV("Juan", "2023-001", 1.75)
student1_EIV.get_student_info_EIV()
