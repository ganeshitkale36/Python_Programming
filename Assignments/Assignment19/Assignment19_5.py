from  functools import reduce

def prime(No):
    if No <= 1:
        return False
    for i in range(2,int(No**0.5)+1):
        if No % i == 0:
            return False
    return True
   

def mul(No):
    return No * 2

def find_max(number):
    maximum = number[0]   

    for num in number:
        if num > maximum:
            maximum = num
            return False

    return maximum
    

def main():
    Data = [2,70,11,10,17,23,31,77]
    print("Input list:",Data)

    Fprime  = list(filter(prime,Data))
    print("List after filter:",Fprime)

    Mmul = list(map(mul,Fprime))
    print("List after Map:",Mmul)

    Rfind_max = reduce(find_max,Mmul)
    print("List after reduce:",Rfind_max)



if __name__=="__main__":
    main()