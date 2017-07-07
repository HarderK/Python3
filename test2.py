# 列表推导式
number_list = [number * number for number in range(1, 10)]
print(number_list)

a_list = [number for number in range(0, 10) if number % 2 == 0]
print(a_list)

cells = [(row, col) for row in range(1, 5) for col in range(0, 3)]
print(cells)

for (row, col) in cells:
	print(row, col)

# 字典推导式
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# 元组是没有推导式的
# 圆括号之间的是生成器推导式
print((number for number in range(0, 10)))

def my_range(first = 0, last = 10, step = 1):
	number = first
	while number < last:
		yield number
		number += step


print (my_range())

# 装饰器
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function

@document_it
def add_ints(a, b):
	return a + b

add_ints(3, 5)


animal = 'fruitbat'
def print_global():
	global animal
	print('inside print_global:', animal)
	animal = 'hello'
	print('after change value', animal)

print_global()

def change_local():
	animal = 'wombat'
	print('locals:', locals())

change_local()

print('globals:', globals())


# 异常
short_list = [1, 2, 3]
position = 3
try:
	print(short_list[position])
except IndexError as err:
	print('Bad Index:', err, position)
except Exception as other:
	print('Something else broke:', other)

