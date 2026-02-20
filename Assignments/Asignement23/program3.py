class Numbers():

    def __init__(self,value):
        self.No = value

    def ChkPrime(self):
        
        if self.No <= 1 :
            return False
        for i in range(2,int(self.No ** 0.5) + 1):
            if self.No % i == 0:
                return False
        print("Prime no is:",self.No)
    

    def Factors(self):
        Fact = 1
        for i in range(1,self.No+1, 1):
            Fact = Fact * i
            print("Factors of the  number is:",Fact)

    
    def SumFactors(self):
        total = 0
        for i in range(1,self.No+ 1):
            if self.No % i == 0:
                total = total + 1
        print("Sumfactor is",total)


    def perfect(self):
        total = 0
        for i in range(1,self.No):
            if self.No % i == 0:
                total += i
        print("perfecat number is:",total == self.No)
      
obj1 = Numbers(3)
obj2 = Numbers(4)
obj3 = Numbers(5)
obj4 = Numbers(6)


obj1.Factors()
obj2.SumFactors()
obj3.ChkPrime()
obj4.perfect()
