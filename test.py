import math
from collections import Iterable
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

d.pop('Bob')

print(d)

s = set([1, 2, 3])
print(s)

int('123')
int(12.32)
float('12.34')
str(1.23)
bool(1)
bool('')


def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-22))

def nop():
	pass

print(nop())

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

print(x, y)

def power(x, n = 2):
	s = 1.23
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(2))

def add_end(L = []):
	L.append('END')
	return L

print(add_end([1, 2]))
print(add_end())
print(add_end())


def add(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum

print(add(1, 3, 5))

print(add(*[1, 3, 5]))

def person(name, age, **kw):
	print('name:', name, 'age:', age, 'others:', kw);

person('HarderK', 24, city="beijing")

extra = {'city': 'Beijing', 'job': 'Engineer'}

person('HarderK', 24, **extra)

def person1(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:', name, 'age:', age, 'others:', kw);

person1('HarderK', 24)


def person2(name, age, *, city='Beijing', job='Engineer'):
	print(name, age, city, job)

person2('HarderK', 24)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[-2:-1])

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
	print(d[key])

print(isinstance(d, Iterable))


for i, value in enumerate(['a', 'b', 'c']):
	print(i, value)


L = []
for x in range(1, 10):
	L.append(x * x)

print(L)

print([x * x for x in range(1, 10)])

print([ m + n for m in 'ABC' for n in 'XYZ'])


g = (x * x for x in range(10))
print(next(g))


def fib(max): 
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	return 'done'

for n in fib(6):
	print(n)

def triangles(max):
	L = [1]
	n = 1
	while n < max:
		li = []
		for key, value in enumerate(L):
			li.append(value)