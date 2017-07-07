a = [1, 23, 3]
b = list(range(5))
print(b[1: -1])

print( 5 in b)
print(a.sort())
print(a)
a.extend(b)
print(a)
a.sort()
print(a)
a.pop(3)
print(a)
c = a.copy()
print(c)
c[1]=22
print(c)
print(a)
print(a.count(1))