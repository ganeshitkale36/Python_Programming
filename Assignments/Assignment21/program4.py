import threading

def Sum_no(list):
    sum = 0
    for i in list:
        sum = sum + i
    print(sum)
    
         

def mul_no(list):
    mul = 1
    for i in list:
        mul = mul * i
    print(mul)

def main():
    size = int (input("Enter the Number of elements :"))
    Data = list()
    print("Enter the elements")

    for i in range(size):
        value = int(input())
        Data.append(value)
    print(Data)

    t1 = threading.Thread(target=Sum_no,args=(Data,))

    t2 = threading.Thread(target=mul_no,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__=="__main__":
    main()




