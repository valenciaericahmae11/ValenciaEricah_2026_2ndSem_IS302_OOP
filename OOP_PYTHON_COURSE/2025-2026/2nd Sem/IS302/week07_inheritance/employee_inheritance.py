class Employee_EIV:
    def __init__(self_EIV, name_EIV, salary_EIV):
        self_EIV.name_EIV = name_EIV
        self_EIV.salary_EIV = salary_EIV

class Manager_EIV(Employee_EIV):
    def __init__(self_EIV, name_EIV, salary_EIV, department_EIV):
        super().__init__(name_EIV, salary_EIV)
        self_EIV.department_EIV = department_EIV

    def display_manager_EIV(self_EIV):
        print("Name:", self_EIV.name_EIV)
        print("Salary:", self_EIV.salary_EIV)
        print("Department:", self_EIV.department_EIV)

manager1_EIV = Manager_EIV("John", 50000, "IT")
manager1_EIV.display_manager_EIV()
