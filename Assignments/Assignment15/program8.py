chkDivisible = lambda No : No % 3 == 0 & No % 5 == 0

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Actual data is:",Data)

    FData = list(filter(chkDivisible,Data))
    print("Data after filter:",FData)

if __name__=="__main__":
    main()
