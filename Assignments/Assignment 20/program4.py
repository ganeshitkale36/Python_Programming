import threading

def Small(str):
    print("Small is :",threading.get_ident())

    count = 0
    for char in str:
        if char.islower():
            count =+ 1
    print(count)

def Capital(str):
    print("Capital is :",threading.get_ident())
    count = 0
    for char in str:
        if char.isupper():
            count =+ 1
    print(count)


def Digits(str):
    print("Digits is :",threading.get_ident())
    count = 0
    for char in str:
        if char.isupper():
            count =+ 1
    print(count)

def main():
    print("Inside main")

    t1 = threading.Thread(target=Small,args=("fhhjfhgjgkkkkkkkkk",))

    t2= threading.Thread(target=Capital,args=("GJHKJHGKHH",))

    t3= threading.Thread(target=Digits,args=("1284658908",))
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

if __name__=="__main__":
    main()

    


