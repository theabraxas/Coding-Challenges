#Digit_Fifth_Powers
numbers = []
thesum = 0
for i in range(10,1000000):
	string = 0
	i = str(i)
	for j in i:
		x = str(int(j)**5)
		string += int(x)
	if int(i) == string:
		print 'success'
		numbers.append(string)
for i in numbers:
	thesum += int(i)
	print i
print thesum