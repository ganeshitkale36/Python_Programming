findmax = lambda No1,No2,No3:max(No1,No2,No3)

def main():
    value1 = int(input("Enter a  first number:"))
    value2 = int(input("Enter a second number:"))
    value3 = int(input("Enter a Third number:"))
   
    Ret = findmax(value1,value2,value3)
    print("Largset Number is :",Ret)
    

if __name__=="__main__":
    main()