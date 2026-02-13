import threading

def Even(No):
    
    for i in range(2,No,2):
        print(i)
        
    
        
def odd(No):
    for i in range(1,No,2):
        print(i)



def main():
    print("Inside main")
    

    List1 = int(input("Enter a number"))
    t1 = threading.Thread(target=Even,args=(List1,))
    t1.start()

    List2 = int(input("Enter a number"))
    t2 = threading.Thread(target=odd,args=(List2,))
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()