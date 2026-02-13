import threading
import time

def Evenfactor(No):
    fact = 1
    
    for i in range(2,No,2):
        fact = fact * i
        
        print(fact)

def Oddfactor(No):
    fact = 1
    
    for i in range(1,No,2):
        fact = fact * i
        
        print(fact)

def main():
    print("Inisde main")
    
    t1 = threading.Thread(target=Evenfactor,args=(10,))
    t1.start()
    t1.join()
    
    t2 = threading.Thread(target=Oddfactor,args=(10,))
    t2.start()
    t2.join()


if __name__=="__main__":
    main()

