

def max(list):
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num 
    print(max_num) 


def main():
    Ret = 0
    

    size = int (input("Enter the Number of elements :"))
    Data = list()
    print("Enter the elements")

    for i in range(size):
        value = int(input())
        Data.append(value)
    print(Data)
    print("maximum no is :",Ret)

    Ret = max(Data)
    
   
    
  


if __name__=="__main__":
    main()

    