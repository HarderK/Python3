# 对象
class Person():
	def __init__(self, name):
		self.name = name

hunter = Person('Fudd')

print(hunter.name)

class Man(Person):
	def __init__(self, name):
		self.name = 'man:' + name

man = Man('hello')

print(man.name)

class EmailPerson(Person):
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email

email = EmailPerson('HarderK', 'yan_harder@163.com')


class A():
	count = 0
	def __init__(self):
		A.count += 1
	@classmethod
	def kids(cls):
		print('A has', cls.count, 'little objects')

easy_a = A()
breezy_a = A()
print(A.count)