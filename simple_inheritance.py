class Animal:
    def makesoound(self):
        print('Animal make different sounds')

class Dog(Animal):
    def makesoound(self):
        print('Dog make Bhow Bhow sounds')

D= Dog()
D.makesoound()