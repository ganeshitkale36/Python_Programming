import threading
import time
def Thread1(No):
    for i in range(1,No,1):
        print(i)
        


def Thread2(No):
    for i in range(No,0,-1):
        print(i)

def main():
    print("Inside main")
 
    t1 = threading.Thread(target=Thread1,args=(51,))
    t2 = threading.Thread(target=Thread2,args=(50,))

    t2.start()
    t2.join()

    t1.start()
    t1.join()
    

   
if __name__=="__main__":
    main()