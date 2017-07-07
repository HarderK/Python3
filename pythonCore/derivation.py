word = "letter"


print({letter: word.count(letter) for letter in set(word)})


number_thing = (number for number in range(1, 20))
print(number_thing)
print([i for i in number_thing if i < 5 ])
print(list(number_thing))
print(list(number_thing))

print(None is None)

a = {}
b = a
print(a is b)

print(isinstance(a, dict))

c = ['a', 'b']
print('a' + 'b')
