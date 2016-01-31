#Problem 14 - Highly divisible triangular number
tn = 1
value = 1
tndict = {}
highest = 0
while divs <= 500:
	print "TN is " + str(tn) + " value is " + str(value)
	counter = 0
	if value > 1:
		counter += 1
	for i in range(2,int(tn / 2)+1):
		if i < 3:
			counter += 1
		if tn % i == 0:
			counter += 1
		if counter >= 500:
			print str(tn) + " IS THE ANSWER, counter is %d" % counter
			exit()
	value += 1
	tn += value
	if counter > highest:
		highest = counter