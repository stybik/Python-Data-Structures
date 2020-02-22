def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        value = arr[i]
        pos = i
        while pos > 0 and value < arr[pos-1]:
            arr[pos] = arr[pos-1]
            pos -=1

        arr[pos] = value
    return arr

if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)