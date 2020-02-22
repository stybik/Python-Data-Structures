def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        if small != i:
            arr[i], arr[small] = arr[small], arr[i]

    return arr


if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    sorted_arr = selection_sort(arr)
    print(sorted_arr)