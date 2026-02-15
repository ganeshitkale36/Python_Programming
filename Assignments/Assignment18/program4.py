def main():

    size = int(input("Enter the number of elements:"))
    Data = list()
    print("Enter the elements:")

    for i in range(size):
        value = int(input())
        Data.append(value)

    print(Data)

    print("Element to be search:")
    key = 5
    freq = Data.count(key)
    print("frequency of key is:",freq)


if __name__=="__main__":
    main()