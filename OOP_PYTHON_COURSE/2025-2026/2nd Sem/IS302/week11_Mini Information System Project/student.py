class Student:
    def __init__(self, student_id, name, course):
        self.student_id_EMIV = student_id
        self.name_EMIV = name
        self.course_EMIV = course

    def display_info(self):
        print(f"ID: {self.student_id_EMIV}")
        print(f"Name: {self.name_EMIV}")
        print(f"Course: {self.course_EMIV}")