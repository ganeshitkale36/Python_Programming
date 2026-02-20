
import  os 
def checkdir(filename):

    Ret = False

    Ret = os.path.exists(filename)

    if(Ret == True):
        print("File exists")

    else:
        print("file is not exists")

    
    
       
    
def main():
    filename = input("Enter the name of file")

    checkdir(filename)

if __name__=="__main__":
    main()
