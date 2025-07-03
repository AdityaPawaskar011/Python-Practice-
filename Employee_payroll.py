class Employee:
    sal=0
    bonus_salary=0
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
        Employee.bonus_salary=Employee.sal+bonus
        print(f"The salary with bonus is {Employee.bonus_salary}")

class Developer(Employee):
    def getsalary(self,projectbonus=0,overtime=0,skill_based_incentives=0):
        final_salary=projectbonus+overtime+skill_based_incentives+Employee.bonus_salary
        print(f"The Final salary with bonus + projectbonus + overtime + skill_based_incentives is {final_salary}")


E=Employee('A',20000)
E.getsalary()

M=Manager('A',20000)
M.getsalary()

D= Developer('A',2000)
D.getsalary(overtime=100)