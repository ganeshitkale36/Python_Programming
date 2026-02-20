
def main():
     
    filename = input("Enter the name of file and srting:")

    obj = open("Demo.txt","r")

    print("The content of file is:", obj.read())

  



if __name__=="__main__":
    main()
