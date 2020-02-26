class Test:
	def __init__(self, limit):
		self.limit = limit

	# Called when iteration is initialized
	def __iter__(self):
		self.x = 10
		return self

	# To move to next element
	def __next__(self):
		x = self.x
		if x > self.limit:
			raise StopIteration

		self.x = x+1
		return x


# print numbers from 10 to 15
for i in Test(15):
	print(i)


# prints nothing
for i in Test(5):
	print(i)

