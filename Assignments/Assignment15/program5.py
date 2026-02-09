from functools import reduce
max_number = lambda No : max_number

def main():
     Data = [1,2,3,4,5,10]
     print("Actual data is:",Data)

     RData = reduce(max,Data)
     print("Data After Reduce:",RData)

if __name__=="__main__":
     main()