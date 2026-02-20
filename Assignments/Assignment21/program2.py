
import threading

def max(list):
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num 
    print(max_num) 



def min(list):
    min_num = list[0]
    for num in list:
        if num <= min_num:
            min_num = num 
    print(min_num) 
    

def main():
      
    size = int (input("Enter the Number of elements :"))
    Data = list()
    print("Enter the elements")

    for i in range(size):
        value = int(input())
        Data.append(value)
    print(Data)
 
   
    

    t1 = threading.Thread(target=max,args=(Data,))
    
    t2 = threading.Thread(target=min,args=(Data,))
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__=="__main__":
    main()





