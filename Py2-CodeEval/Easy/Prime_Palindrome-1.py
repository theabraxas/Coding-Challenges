import sys
number = 0
for i in range(1,1001):
	isprime = True
	for j in range(2,32):
		if i % j == 0:
			isprime = False
			break
	if isprime == True:
		if i % 10 == (i - i % 100) / 100:
			number = i
print number
