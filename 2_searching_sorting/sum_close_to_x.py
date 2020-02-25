MAX_VAL =100000

def printClosest(arr, n, x):
    res_l , res_r = 0,0
    l, r, diff = 0, n-1, MAX_VAL

    while(r>l):
        if abs(arr[l] + arr[r]) - x < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)
        
        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1


    print("Closes pair numbers {} and {}".format(arr[res_l], arr[res_r]))



if __name__ == "__main__": 
    arr = [10, 22, 28, 29, 30, 40] 
    n = len(arr) 
    x=54
    printClosest(arr, n, x) 