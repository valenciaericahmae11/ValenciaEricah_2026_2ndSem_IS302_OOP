class Employee_EIV:
    def __init__(self_EIV, name_EIV):
        self_EIV.__name_EIV = name_EIV
        self_EIV.__salary_EIV = 0

    def set_salary_EIV(self_EIV, salary_EIV):
        if salary_EIV > 0:
            self_EIV.__salary_EIV = salary_EIV

    def get_salary_EIV(self_EIV):
        return self_EIV.__salary_EIV

emp_EIV = Employee_EIV("Ana")
emp_EIV.set_salary_EIV(30000)
print("Salary:", emp_EIV.get_salary_EIV())
