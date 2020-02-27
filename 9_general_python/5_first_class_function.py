def square(x):
	return x*x

def cube(x):
	return x*x*x

def my_map(func, arr):
	result = []
	for i in arr:
		result.append(func(i))
	return result

squares = my_map(cube, [1,2,3,4,5])
# print(squares)


# Returning a function

def logger(msg):
	def log_message():
		print('Log: ', msg)

	return log_message

log_hi = logger('Hi')
log_hi()