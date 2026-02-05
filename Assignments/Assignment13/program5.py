def main():
    marks = 0
    marks = int(input("Enter a marks:"))
    if (marks >= 75):
        print("Distinction:",marks)


    elif(marks >= 60):
        print("First class",marks)


    elif(marks >= 50): 
        print("Second class",marks)


    elif(marks < 50): 
        print("fail",marks)



if __name__=="__main__":
    main()