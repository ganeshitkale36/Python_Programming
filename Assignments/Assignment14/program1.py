Square = lambda No : (No ** 2)


def main():

    Value = int(input("Enter the value:"))
    Ret = Square(Value)
    print("Square of No",Ret)

if __name__=="__main__":
    main()