a = dict(['a1', 'b2', 'c3'])
print(a)

b = dict(('c5', 'd6', 'e7'))
print(b)

a.update(b)
print(a)

print(a.keys())
print(list(a.items()))

for item in a:
	print(item)

