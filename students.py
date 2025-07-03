class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age= age
        self.rollno = rollno

    def display_info(self,rollno):
        if self.rollno != rollno:
            return f"invalid details"
        
        print( f"student roll no {self.rollno} name is {self.name} and he is {self.age} old")
    
Stu = Student('Aditya',22,10)

Stu.display_info(10)

