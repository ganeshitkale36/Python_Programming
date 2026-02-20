def main():
    filename1 = input("Enter the firts name of file:")

    filename2 = input("Enter the second name of file:")

    obj1 = open("Demo.txt","r")
    obj2 = open("Hello.txt","r")

    obj1.read()
    obj2.read()


    if(obj1 == obj2):

        print("Sucess files")
    else:
        print("Failure file")


if __name__=="__main__":
    main()


