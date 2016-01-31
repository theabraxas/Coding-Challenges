def TriangleNumberFinder(n)
	divs = 0
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
				#print "divisible by self counter is %d" % counter
			if tn % i == 0:
				counter += 1
				#print 'divisible by %d' % i
			if counter >= 500:
				return str(tn) + " IS THE ANSWER, counter is %d" % counter
				exit()
			# if i == 0 and value != 1:
			# 	counter = counter + 1
		value += 1
		tn += value
		if counter > highest:
			highest = counter