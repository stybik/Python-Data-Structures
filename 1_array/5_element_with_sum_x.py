def print_pairs(arr, n, sum):
    s = set()
    for i in range(0, n):
        temp = sum-arr[i]
        print(temp)
        if (temp in s):
            print("Pair with sum {} are {} and {}".format(sum, arr[i], temp))
        s.add(arr[i])

    for i in s:
        print(i)


if __name__ == "__main__":
    arr = [int(i) for i in input("Enter array").split()]
    n = int(input("Enter sum: "))
    print_pairs(arr, len(arr), n)