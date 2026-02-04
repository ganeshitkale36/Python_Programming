
class Arithematic():
    
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B


    def Addition(self,A,B):
        self.Addition = A + B
        print("Addition is:",self.Addition)
       
    
    def Substraction(self,A,B):
        self.Substraction = A - B
        print("Substraction is:",self.Substraction)
       
    
    def Multiplication(self,A,B):
        self.Multiplication = A * B
        print("Multilication is:",self.Multiplication)
        

    def Division(self,A,B):
        self.Division = A / B
        print("Division  is:",self.Division)
        
    

 

obj1 = Arithematic(10,20)
obj2 = Arithematic(10,20)
obj3 = Arithematic(10,20)
obj4 = Arithematic(10,20)

obj1.Addition(10,20)
obj2.Substraction(10,20)
obj3.Multiplication(10,20)
obj4.Division(10,20)