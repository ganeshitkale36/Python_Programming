import threading
import time
def even(No):
    for i in range(2,No,2):
        print(i)

def odd(No):
    for i in range(1,No,2):
        print(i)



def main():
    print("Inside main")
    start_time = time.time()
    t1  = threading.Thread(target=even,args=(21,))
    t1.start()
    t1.join()

    t2  = threading.Thread(target=odd,args=(21,))
    t2.start()
    t2.join()
    end_time = time.time()

    

    print("Time required:",end_time - start_time)

if __name__=="__main__":
    main()