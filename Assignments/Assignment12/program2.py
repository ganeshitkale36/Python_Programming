
def main():
    num = int(input("Enter a number:"))
    for i in range(1,num+1):
        if num % i == 0:
            print(i)
            print("Factors are:",num)

if __name__=="__main__":
    main()