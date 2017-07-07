def func(arg1, arg2='test', **kw):
	print(arg1, arg2, kw['test1'])

func('hello', test1 = 'a', test2 = 'b')

while True:
	count = 1
	if count > 0: break

print(count)

def func2(arg, **kw):
	return arg + kw['test']

def func1(*arg, **kw):
	print(**kw)

print(func1(123, test = 1, test2 = 2))