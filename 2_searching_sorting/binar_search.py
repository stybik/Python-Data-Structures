def binarySearch(arr, ele):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == ele:
            return True
        elif ele < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False

if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    sorted_arr = sorted(arr)
    ele = int(input())
    search = binarySearch(sorted_arr, ele)
    print(search)