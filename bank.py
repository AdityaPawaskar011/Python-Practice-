class Bank:
    bankbal = 0 
    def __init__(self,name,accouuntno):
        self.name=name
        self.accoountno=accouuntno
        self.balance=0
    
    def deposite(self,accountno,amount):
        
        if accountno != self.accoountno:
            return f"Wrong accountno"
        
        self.balance += amount
        Bank.bankbal += amount
        print(self.balance)
    
    def withdraw(self,amount,accountno):

        if self.accoountno != accountno or self.balance < amount or Bank.bankbal < amount:
            return f"Wrong account no or insufficiant balance"
        self.balance -= amount
        Bank.bankbal -= amount

    def chechkBal(self,accountno):
        if self.accoountno != accountno :
            return f"Wrong account no"
        return self.balance
    
b= Bank('A',1234)
   
b.deposite(1234,100)  
# print(b.chechkBal(1234))   
print(b.chechkBal(1234))  
