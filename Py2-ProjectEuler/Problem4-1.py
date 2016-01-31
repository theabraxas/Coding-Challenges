#Problem 4 - Largest Palindrome Product
largest = 0
for i in range(100,1000):
	for x in range(100,1000):
		product = i * x
		if largest < product:
			line = str(product)
			if line == line[::-1]:
				largest = product
print largest