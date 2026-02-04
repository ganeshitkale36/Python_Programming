
class Circle():

    PI = 3.14

    def __init__(self,A):
        self.Radius = A
        self.Area = A
        self.Circumference = A

    def Accept(self):
        self.Radius = int(input("enter a Radius:"))
        print(self.Radius)
       

    def CalculateArea(self):
        self.Area = 3.14 * 4 * 4
        print("Inside instance method of CalculateArea:",self.Area)

    def CalculateCircumference(self):
        self.Circumference = 2 * 3.14 * 4
        print("Inside instance method of CalculateCircumference:",self.Circumference)

    def display(self):
        print("Display the values of:",self.Radius,self.Area,self.Circumference)

obj1 = Circle(4)
obj2 = Circle(8)
obj3 = Circle(2)    

obj1.Accept()
obj2.CalculateArea()
obj3.CalculateCircumference()