class Shape:
    pi = 3.14
    def area(self):
        print('Calculate the area here')

class Rectangle(Shape):
    def area(self,length,width):
        Area=length*width
        print(f"The area of Rectangle: {Area}")

class Circle(Shape):
    def area(self,radius):
        Area= Shape.pi * radius
        print(f"The area of Rectangle: {Area}")

class Triangle(Shape):
    def area(self,base,height):
        Area= base * height
        print(f"The area of Rectangle: {Area}")


def get_area(Shape):
    Shape.area(5,2)

get_area(Rectangle())



