class Employee_EIV:
    def work_EIV(self_EIV):
        print("Employee performs tasks")

class Programmer_EIV(Employee_EIV):
    def work_EIV(self_EIV):
        print("Programmer writes code")

class Designer_EIV(Employee_EIV):
    def work_EIV(self_EIV):
        print("Designer creates UI designs")

employees_EIV = [Programmer_EIV(), Designer_EIV()]
for emp_EIV in employees_EIV:
    emp_EIV.work_EIV()
