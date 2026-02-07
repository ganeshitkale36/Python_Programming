
chk = lambda Value1,Value2:(Value1<Value2)
       
       
def main():
    value1 = int(input("Enter a first  Number:"))      
    value2 = int(input("Enter a  second Number:"))
  
    Ret = 0
    Ret = chk(value1,value2)

    if(Ret == True):
        print("Min no is:",value1)

    else:
        print("Min no is:",value2)
 

if __name__=="__main__":
    main()