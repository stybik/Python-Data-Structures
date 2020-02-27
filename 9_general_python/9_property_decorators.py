class Employee:

	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def email(self):
		return "{}.{}@gmail.com".format(self.first, self.last)

	@property
	def full_name(self):
		return "{} {}".format(self.first, self.last)

	@full_name.setter
	def full_name(self, name):
		first, last = name.split(" ")
		self.first = first
		self.last = last

	@full_name.deleter
	def full_name(self):
		print("Delete Name")
		self.first = None
		self.last = None

emp1 = Employee('John', 'Smith')

emp1.full_name = "Bikram Biswas"

print(emp1.first)
print(emp1.email)
print(emp1.full_name)

