student_name = input("Enter student name: ")

grades_RBH = []
for i in range(1, 4):
    grade_RBH = float(input(f"Enter grade for subject {i}: "))
    grades_RBH.append(grade_RBH)

average = sum(grades_RBH) / len(grades_RBH)

if average >= 90:
    remark = "Excellent"
elif average >= 85:
    remark = "Very Good"
elif average >= 80:
    remark = "Good"
elif average >= 75:
    remark = "Fair"
else:
    remark = "Failed"

print(f"\nStudent Name: {student_name}")
print(f"Average Grade: {average:.2f}")
print(f"Remark: {remark}")

