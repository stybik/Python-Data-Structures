def subarray_sum(arr, n, sum):
    curr_sum = arr[0]
    start = 0
    i = 1
    while(i <= n):
        while curr_sum > sum and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            print("{} and {}".format(start, i-1))
            return 1
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

if __name__ == "__main__":
    arr = [int(i) for i in input("Enter array").split()]
    n = len(arr)
    sum = int(input())
    subarray_sum(arr, n, sum)