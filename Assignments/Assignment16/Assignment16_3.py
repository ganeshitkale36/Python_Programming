def Add(No1,No2):
    return No1 + No2


def main():
    value1 = int(input("Enter first Number:"))
    value2 = int(input("Enter Second Number:"))

    Ans = value1 + value2

    Ans = Add(value1,value2)

    print("Addition is :",Ans)

if __name__=="__main__":
    main()