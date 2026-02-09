
Square = lambda No: No ** 2

def main():
    Data = [1,2,3,4,5]
    print("Actual data is",Data)
    
    MData = list (map(Square,Data))
    print("Data After map:",MData)
 
if __name__=="__main__":
    main()

