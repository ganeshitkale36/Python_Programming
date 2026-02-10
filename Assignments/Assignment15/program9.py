from functools import reduce

Mul = lambda A,B: A * B 

def main():
    Data = [1,2,3,4,5]
    print("Actual data is:",Data)

    RData= reduce(Mul,Data)
    print("Data After reduce:",RData)

if __name__=="__main__":
    main()