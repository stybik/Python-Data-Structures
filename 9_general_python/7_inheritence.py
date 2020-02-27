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


class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_language):
		super().__init__(first, last, pay)
		self.prog_language = prog_language


class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('--->', emp.full_name())



dev1 = Developer('Bikram', 'Biswas', 50000, 'Python')
dev2 = Developer('Sagar', 'Desitti', 50000, 'PHP')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev1])

# print(dev1.email)
# print(dev1.prog_language)




# print(mgr_1.email)
# mgr_1.add_employee(dev2)
# mgr_1.remove_employee(dev1)
# mgr_1.print_emps()