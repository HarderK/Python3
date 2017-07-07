fin = open('relativity',  'rt')
i = 0
for line in fin:
	i += 1
	print(line)

print(fin.read())
print(i)
fin.close()
# print(poem)