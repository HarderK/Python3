a = {'a', 'b', 'c'}
b = set(['d1', 'c2'])
print(a, b)

print(a | b)
print(a.union(b))
print(a)

c = {'b', 'c'}

print(a > c)