#Problem 50
import math
 
def primecheck(n):
    i = 3
    toggle = 0
    while i < int(math.sqrt(n))+1:
        if n % i == 0:
            return False
        i += 2
    print n
    

def prime_x(n):
    primes = 2 # 1 and 2
    count = 1
    iter = 3
    while count < n:
        if primecheck(iter):
            prime = iter
            count += 1
        iter += 2
    print prime

listofprimes = [2,3,5,7]
for i in range(11,1000000,2):
	listofprimes.append(primecheck(i))

count = 0
for i in listofprimes:
	count = 0
	for j in listofprimes:
		