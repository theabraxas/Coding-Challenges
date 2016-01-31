#Problem 20
thesum = 1
for i in range(1,101):
	thesum *= i
newsum = 0
for i in str(thesum):
	newsum += int(i)

print newsum