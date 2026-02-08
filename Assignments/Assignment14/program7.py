Chkdivisible = lambda No:(No % 5 == 0 )

def main():
    value = int(input("Enter a Number:"))

    Ret = Chkdivisible(value)
    print("Number is divisible:",Ret)


    if(value % 5 == 0):
        return True
    else:
        return False
    

if __name__=="__main__":
    main() 