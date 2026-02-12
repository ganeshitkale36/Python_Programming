
def Display(rows,cols):

    i = 1
    j = 1

    for i in range(1,rows):

        for j in range(1,cols):

            if(i < j):

                print("*")

def main():

    row = int(input("Enter the number of rows:"))
    col = int(input("Enter the number of columns:"))

    Display(row,col)


if __name__ == "__main__":
    main()