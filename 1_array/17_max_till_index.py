def sub_arr_sum(arr, len, index):
    """
    Given an array of length n, and q queries which has indices left and right from the array,
    find the sum of the sub array with left index being l and right index being r
    """
    max_arr = len * [0]
    max_arr[0] = arr[0]
    for i in range(0,len-1):
        max_arr[i+1] = max(max_arr[i], arr[i+1])

    if index == 0:
        return arr[0]
    else:
        return max_arr[index]

if __name__ == "__main__":
    arr = [int(i) for i in input("Enter space sepreated integers: ").split()]
    arr_len = len(arr)
    index = int(input("Enter index till which maximum is needed: "))
    result = sub_arr_sum(arr, arr_len, index)
    print(result)
