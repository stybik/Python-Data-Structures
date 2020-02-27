class Employee:

	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + "." + last + "@gmail.com"
		self.pay = pay

	def full_name(self):
		return "{} {}".format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	def __str__(self):
		return "{} - {}".format(self.full_name(), self.email)


emp1 = Employee("Bikram", "Biswas", 50000)
emp2 = Employee("Desitti", "Sagar", 60000)

print(repr(emp1))
print(str(emp1))