

def main():
    
    size = int (input("Enter the Number of elements :"))
    Data = list()
    print("Enter the elements")

    for i in range(size):
        Value = int(input())
        Data.append(Value)

    sum = 0
    for i in range(size):
        sum = sum + Data[i]
    print("Summattion is",sum) 

    


if __name__=="__main__":
    main()