
def main():
    filename = input("Enter the name of file:")

    fobj = open("Demo.txt")

   
    print("The content of file is :",fobj.read())

if __name__=="__main__":
    main()



  