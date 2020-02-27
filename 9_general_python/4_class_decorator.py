class decorator_class(object):
	
	def __init__(self, orginal_function):
		self.original_function = orginal_function


	def __call__(self, *args, **kwargs):
		print("call method executed this before: {} ".format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)


@decorator_class
def display_info(name, age):
	print("display_info ran with arguments ({} {})".format(name, age))


display_info("Bikram", 23)