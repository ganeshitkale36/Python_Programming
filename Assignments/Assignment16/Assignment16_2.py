def chknum(Number):
    if Number % 2 == 0:
        print("Even NUmber")
    else:
        print("odd Number")
    
def main():
    No = int(input("Enter a number:"))
    Ret = chknum(No)

if __name__=="__main__":
    main()