import time
import math

# decorator to calculate duration taken by any function
def calculate_time(func):

	# added arguments inside the inner1, if function takes any arguments can be added like this
	def inner1(*args, **kwargs):
		begin = time.time()
		func(*args, **args)
		end = time.time()
		print("Total time taken: ", func.__name__, end - begin)

	return inner1


# This can be added to any function
@calculate_time
def factorial(num):
	time.sleep(2)
	print(math.factorial(num))

factorial(10)
