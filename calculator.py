class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        c=self.a+self.b
        print(c)
    
    def sub(self):
        c=self.a-self.b
        print(c)

    def mul(self):
        c=self.a*self.b
        print(c)

    def div(self):
        c=self.a/self.b
        print(c)

    

math=Calculator(5,1)
math.add()