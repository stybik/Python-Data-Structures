r = 3
c = 4

def changeMatrix(mat):
    row = [0] * r
    col = [0] * c

    for i in range(0, r):
        for j in range(0, c):
            if (mat[i][j] == 0):
                row[i] = 0
                col[j] = 0

    for i in range(0, r):
        for j in range(0, c):
            if(row[i] == 0 or col[j] == 0):
                mat[i][j] = 0
    

def printMatrix(mat):
    for i in range(0, r):
        for j in range(0, c):
            print(mat[i][j], end=" ")
        print()


if __name__ == "__main__":
    mat = [ [1, 0, 0, 1], 
            [0, 0, 1, 0], 
            [0, 0, 0, 0] ]
    print(f"Input Matrix: {mat}")
    changeMatrix(mat)
    print(f"Modified Matrix: ")
    printMatrix(mat)
