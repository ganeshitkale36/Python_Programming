
cube = lambda No : (No ** 3)


def main():

    Value = int(input("Enter the value:"))
    Ret = cube(Value)
    print("cube of No",Ret)

if __name__=="__main__":
    main()