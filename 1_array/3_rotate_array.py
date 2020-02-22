def rotate_arr_d(arr, d, length):
    for i in range(d):
        left_rotate(arr, length)

def left_rotate(arr, length):
    temp = arr[0]
    for i in range(length - 1):
        arr[i] = arr[i+1]
    arr[length-1] = temp

def print_arr(arr, n):
    for i in range(n):
        print(arr[i], sep=" ")

if __name__ == "__main__":
    arr = [int(i) for i in input("Enter space sepreated integers: ").split()]
    arr_len = len(arr)
    d = int(input("Enter the no time array needs to be rotated: "))
    rotate_arr_d(arr, d, arr_len)
    print_arr(arr, arr_len)