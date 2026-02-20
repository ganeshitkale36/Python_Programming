from functools import reduce

def chk(num):
    if (num >= 70):
        return num
    
    
def Add(num):
    return num + 10

def mul(A,B):
    return A * B


def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Input List",Data)

    Fchk = list(filter(chk,Data))
    print("List after Filter:",Fchk)

    MAdd = list(map(Add,Fchk))
    print("List after Map:",MAdd)

    Rmul  = reduce(mul,MAdd)
    print("List after reduce:",Rmul)


if __name__=="__main__":
     main()




