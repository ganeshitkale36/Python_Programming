class Demo():
    No = 10
    
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
    
    def fun(self):
        print("Inside instance method of fun:",self.No1,self.No2)

    def gun(self):
        print("Inside instance method of gun:",self.No1,self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()


