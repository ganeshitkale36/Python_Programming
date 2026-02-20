def divisible(Num):

    if Num % 5 == 0:
        print ("True")
    else:
        print("False") 
    
def main():
    No = int(input("Enter a Number:"))
    Ret = divisible(No)
    

if __name__=="__main__":
    main()

