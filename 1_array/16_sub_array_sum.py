def sub_arr_sum(arr, n, l, r):
    """
    Given an array of length n, and q queries which has indices left and right from the array,
    find the sum of the sub array with left index being l and right index being r
    """
    for i in range(1,n):
        arr[i] += arr[i-1]

    if l == 0:
        return arr[r]
    else:
        return arr[r] - arr[l-1]

if __name__ == "__main__":
    arr = [int(i) for i in input("Enter space sepreated integers: ").split()]
    arr_len = len(arr)
    query_left = int(input("Enter left index: "))
    query_right = int(input("Enter right index: "))
    result = sub_arr_sum(arr, arr_len, query_left, query_right)
    print(result)
