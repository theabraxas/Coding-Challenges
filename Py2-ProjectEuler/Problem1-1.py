multiples = []
sum = 0
for i in range(0,1000):
	if i % 3 == 0:
		multiples.append(i)
	elif i % 5 == 0:
		multiples.append(i)
for i in multiples:
	sum += i

print sum