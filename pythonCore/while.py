count = 1
while count < 5:
	print(count)
	if(count % 2 == 0):
		print('even')
		# break
	count += 1
else:
	print('%d is even' % count)

days = ('MON', 'Tue', 'Thu')
sports = ['Running', 'Basketball', 'Swimming']

print(list(zip(days, sports)))