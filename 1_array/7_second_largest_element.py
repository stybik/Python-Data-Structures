def second_largest(arr, n):
    if n < 2:
        print("Invalid input")
        return
    
    first = second = -99

    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]

        elif (arr[i] > second and arr[i] != first):
            second = arr[i]


if __name__ == "__main__":
    arr = [int(i) for i in input("Enter array").split()]
    n = len(arr)
    second_largest(arr, n)