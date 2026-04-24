name_EIV = input("Enter student name: ")
course_EIV = input("Enter course: ")
with open("students.txt", "a") as file_EIV:
    file_EIV.write(name_EIV + "," + course_EIV + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_EIV:
    for line_EIV in file_EIV:
        print(line_EIV.strip())

