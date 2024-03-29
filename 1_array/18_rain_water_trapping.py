
def calculate_water(arr, n):
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
    Eg:  
    Input: arr[]   = {2, 0, 2}
    Output: 2
    """    

    left = [0] * n
    right = [0] * n
    water = 0

    # Pre compute left array
    left[0] = arr[0]
    for i in range(1,n):
        left[i] = max(left[i-1], arr[i])

    # Pre compute right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)
    water = calculate_water(arr, n)
    print(f"Maximum water that can be accumulated is: {water}")