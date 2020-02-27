def outer_func():
	message = "Hi"

	def inner_function():
		print(message)

	return inner_function

my_func = outer_func()
my_func()
print(my_func.__name__)