#Smallest Multiple
divisors = [11,12,13,14,15,16,17,18,19,20]
base = 19 * 20
newproduct = base
trials = 0
z = False
loops = 0
while z == False:
	loops += 1
	count = 0
	for x in divisors:
		trials +=1
		if newproduct % x == 0:
			count += 1
			if count == 10:
				print newproduct
				print "Solution found at step %s in loop after %s tests" % (loops, trials)
				z = True
	else:
		newproduct = newproduct + base