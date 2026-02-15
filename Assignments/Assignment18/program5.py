import MarvellousNum
def main():
    Ret = 0
    size = int(input("Enter the number of elemmts:"))
    Data = list()
    print("Enter the elemnets:")

    for i in range(size):
        value = int(input())
        Data.append(value)
    print(Data)

    Ret = MarvellousNum.chkprime(Data)
    print(Ret)


if __name__=="__main__":
    main()