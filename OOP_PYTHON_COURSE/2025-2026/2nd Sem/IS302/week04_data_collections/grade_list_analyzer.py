grades_EIV = []
for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    grades_EIV.append(grade)

average = sum(grades_EIV) / len(grades_EIV)
highest = max(grades_EIV)
lowest = min(grades_EIV)

print(f"Average Grade: {average:.1f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")

