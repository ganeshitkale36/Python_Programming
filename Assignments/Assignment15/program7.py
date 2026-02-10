name = lambda str : name 

def main():
    Data = ["Ganesh","kartik","Omkar","vedant","Atharva"]
    print("Actual data is:",Data)

    FData =len(list(filter(name,Data)))
    print("Data After  filter:",FData)

if __name__=="__main__":
    main()