#Problem 25
fib = 1
old = 1
counter = 2 #starting with second term
for i in range(1,10001):
	oldfib = fib
	fib = fib + old
	old = oldfib
	counter += 1
	if len(str(fib)) == 1000:
		print counter
		break