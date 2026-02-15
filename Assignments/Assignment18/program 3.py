
def min(list):
    min_num = list[0]
    for num in list:
        if num < min_num:
            min_num = num 
    print(min_num) 

def main():
    Ret = 0
    
    size = int (input("Enter the Number of elements :"))
    Data = list()
    print("Enter the elements")

    for i in range(size):
        value = int(input())
        Data.append(value)
    print(Data)

    print("minimum no is :",Ret)

    Ret = min(Data)
    
if __name__=="__main__":
    main()