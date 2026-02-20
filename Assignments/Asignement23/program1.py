
class Bookstore():
    NoOfBooks = 0

   

    def __init__(self,Name,Author,quantity):
        self.BookName = Name 
        self.AuthorName = Author
        self.NoOfBooks = quantity

    NoOfBooks = 1



    def display(self):
        print(self.BookName,self.AuthorName, self.NoOfBooks)
        
    
obj1 = Bookstore("Linux System Programing"," by Robert Love", 1)

obj1.display()


obj2 = Bookstore("C Programing"," by Denis Ritchie",2)

obj2.display()




