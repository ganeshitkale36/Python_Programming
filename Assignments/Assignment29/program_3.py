import shutil
def main():
    filename = input("Enter the name of file:")

    fobj = open("Demo.txt")
    
    #shutil.copyfile("Demo.txt","Hello.txt")

    print("The Demo.txt is copies into Hello.txt file:",shutil.copyfile("Demo.txt","Hello.txt"))
   
  

if __name__=="__main__":
    main()



  