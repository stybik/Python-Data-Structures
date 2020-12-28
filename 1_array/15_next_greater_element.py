def printNGE(arr):
    for i in range(0, len(arr), 1):
        n = -1
        for j in range(i+1, len(arr), 1):
            if arr[i] < arr[j]:
                n = arr[j]
                break
        print(f"{arr[i]} ---> {str(n)}")

if __name__ == "__main__":
    arr = [11,13,21,3]
    printNGE(arr)