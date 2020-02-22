def ditsinct_elements(arr, n):
    s = dict()

    for i in range(n):
        if arr[i] not in s.keys():
            s[arr[i]] = arr[i]
            print(arr[i]),

if __name__ == "__main__":
    arr = [int(i) for i in input("Enter array").split()]
    n = len(arr)
    ditsinct_elements(arr, n)