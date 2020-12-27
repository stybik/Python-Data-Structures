import time
import math

# decorator to calculate duration taken by any function
def calculate_time(original_function):
	def wrapper(*args, **kwargs):
		begin = time.time()
		result = original_function(*args, **kwargs)
		end = time.time()
		print("Total time taken: ", original_function.__name__, end - begin)
		return result
	return wrapper


@calculate_time
def factorial(num, ):
	time.sleep(2)
	print(math.factorial(num))

factorial(10)
