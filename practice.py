
def reverse_array(arr, start, end):
	while(start < end):
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

def left_rotate(arr, d):
	if d == 0:
		return
	n = len(arr)
	reverse_array(arr, 0, d-1)
	reverse_array(arr, d, n-1)
	reverse_array(arr, 0, n-1)

def print_array(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")

if __name__ == "__main__":
	arr = [int(i) for i in input("Enter array:").split()]
	d = int(input("Enter d:"))
	left_rotate(arr, d)
	print_array(arr)