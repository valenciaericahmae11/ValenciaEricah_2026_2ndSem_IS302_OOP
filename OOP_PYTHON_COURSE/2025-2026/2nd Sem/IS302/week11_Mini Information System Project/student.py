class Student:
    def __init__(self, student_id, name, course):
        self.student_id_JFGA = student_id
        self.name_JHFGA = name
        self.course_JHFGA = course

    def display_info(self):
        print(f"ID: {self.student_id_JFGA}")
        print(f"Name: {self.name_JHFGA}")
        print(f"Course: {self.course_JHFGA}")