from functools import reduce

def even(No):
    if No % 2 == 0:
        return No
    
def square(No):
    return No ** 2

def Add(A,B):
    return A + B

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]
    print("Input list:",Data)

    Feven = list(filter(even,Data))
    print("List after filter:",Feven)

    Msquare = list(map(square,Feven))
    print("List after map:",Msquare)

    RAdd = reduce(Add,Msquare)
    print("List after reduce:",RAdd)

if __name__=="__main__":
    main()
