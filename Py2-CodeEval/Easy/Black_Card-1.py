for i in test_cases:
	line = i.split('|')
	shift = int(line[1])
	names = line[0].split(' ')
	names.pop()
	counter = 0
	identifier = 0
	while len(names) != 1:
		if identifier == len(names):
			identifier = 0
		if counter == shift:
			names.pop(identifier-1)
			counter = 0
			identifier = 0
		else:
			counter += 1
			identifier += 1
	else:
		print str(names[0])
test_cases.close()