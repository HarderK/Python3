import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s()', func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def sayHello(arg):
	print('hello', arg)

sayHello('world')
print(sayHello.__name__)