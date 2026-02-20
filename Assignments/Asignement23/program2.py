
class BankAccount():
    ROI = 10.5

    def __init__(self,Name,Balance):
        self.AccountName = Name
        self.CurrentBalance = Balance

    def display(self):
        print("The Account holder name is:",self.AccountName)

        print("The Account Balance is:",self.CurrentBalance)

    def deposite(self):
        self.user1= int(input("Enter a balance:"))
        print("The Account Balance is:",self.CurrentBalance + self.user1)

    def Withdraw(self):
        self.user2 = int(input("Enter a balance:"))
        print("The Withdraw Balance is:",self.CurrentBalance - self.user2)

    def CalculateInterest(self):
        Interest = (2500 * 10.5)/100
        print("The Interest  is:",Interest)





obj1 = BankAccount("Ganesh","2000")
obj2 = BankAccount("display",2000)
obj3 = BankAccount("deposite",3000)
obj4 = BankAccount("deposite",3000)
 


obj1.display()
obj2.deposite()
obj3.Withdraw()
obj4.CalculateInterest()




