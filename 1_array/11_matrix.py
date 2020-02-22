def lower(matrix, row, col):
    for i in range(0, row):
        for j in range(0, col):
            if (i<j):
                print("0", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print(" ")


if __name__ == "__main__":
    matrix = []
    row = int(input("Enter rows: "))
    col = int(input("Enter Col: "))
    for i in range(row):
        a = []
        for j in range(col):
            a.append(int(input()))
        matrix.append(a)

    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()

    lower(matrix, row, col)