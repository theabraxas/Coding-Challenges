#Problem 9
import time
a = 0
b = 0
c = 0

start = time.time()

for i in range(1,1000):
	for j in range(1,1000):
		for k in range(1,1000):
			if i < j and j < k and i + j + k == 1000:
				if i**2 + j**2 == k**2:
					print i * j * k
					elapsed = (time.time() - start)		
					print elapsed
					exit()