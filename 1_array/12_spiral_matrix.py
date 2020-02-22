def spiral(a, row, col):
    k = 0
    l = 0
    while(k < row and l < col):
        for i in range(l, col):
            print(a[k][i], end=" ")
        
        k += 1

        for i in range(k, col):
            print(a[i][col-1], end=" ")
        
        row -= 1

        if(k < row):
            for i in range(row-1, (l-1), -1):
                print(a[col-1][i], end=" ")

            col -= 1
        if(l<row):
            for i in range(col-1, k-1, -1):
                print(a[i][l], end=" ")

            l+=1



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

    spiral(matrix, row, col)