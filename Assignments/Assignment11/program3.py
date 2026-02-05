def main():
    num = (input("Enter a number:"))
    sum = 0
    for digit in str(num):
        
        sum = sum + int(digit)
        print("Sum of digit is :",sum)
if __name__=="__main__":
    main()