def push_zeroes(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


if __name__ == "__main__":
    arr = [int(i) for i in input("Enter array").split()]
    n = len(arr)
    push_zeroes(arr, n)
    print(arr)