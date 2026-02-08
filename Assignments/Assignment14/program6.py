Chkodd = lambda No:(No % 2 != 0 )

def main():
    value = int(input("Enter a Number:"))

    Ret = Chkodd(value)
    print("Number is odd:",Ret)


    if(value % 2 != 0):
        return True
    else:
        return False
    

if __name__=="__main__":
    main() 