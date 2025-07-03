class Employee:
    sal=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.sal=self.salary

    
    def getsalary(self):
        # sal += sal
        print(f"The basic salary of Employee is {Employee.sal}")
    

class Manager(Employee):
    def getsalary(self):
        bonus=int(input("how much Bonus you want to give:"))
        print(Employee.sal)
        Bonus_salary=Employee.sal+bonus
        print(f"The total salary is {Bonus_salary}")

E=Employee('A',20000)
E.getsalary()

M=Manager('A',20000)
M.getsalary()