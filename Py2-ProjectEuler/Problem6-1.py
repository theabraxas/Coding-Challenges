#Sum square difference
squares = []
sumofsquares = 0
squareofsum = 0
counter = 0
for i in range(0,101):
	counter +=1 
	n = i ** 2 
	squares.append(n)
	print counter
for i in squares:
	sumofsquares += i
for i in range(0,101):
	squareofsum = squareofsum + i

squareofsum = squareofsum ** 2

print squareofsum - sumofsquares