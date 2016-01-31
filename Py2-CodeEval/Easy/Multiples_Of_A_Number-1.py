import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	if test:
		numx, numn = test.split(',')
		numx, numn = int(numx), int(numn)
		for i in xrange(1, numx):
			if numn * i >= numx:
				num = numn * i
				break
		print num
test_cases.close()