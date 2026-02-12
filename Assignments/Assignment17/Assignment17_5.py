def main():
    No = int(input("Enter a Number:"))

    if No % 1 == 0:
        print("Number is prime:",No)
    else:
        print("Number is not prime:",No)

if __name__=="__main__":
    main()