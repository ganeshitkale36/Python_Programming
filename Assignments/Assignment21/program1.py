import threading

def is_prime(list):
    if list <= 1:
        print(False)

    for i in range(2,int(list **0.5) + 1 ):
        if list % i == 0:
            print(False)
    print(True)


def Notprime(list):
    num = 0
    
    for i in list(1,int(num ** 0.5) +1 ):
        if(num % i != 0):
            print(num)

def main():
    print("Inside main")

    value = [1,2,3,4,5]
    Ret = is_prime(value)
    
  
    
if __name__=="__main__":
    main()
