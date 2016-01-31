#Problem 36

palindromes = []
for i in range(1,1000000):
	x = 0
	i = str(i)
	if i == i[::-1]:
		# print "reverse i is %s" % str(i)
		x = bin(int(i))
	if x > 0:
		x = str(x)
		x = x[2::]

		if x == x[::-1]:
			print "yes!"
			palindromes.append(int(i))
total = 0
for i in palindromes:
	total += i
print total