# #10001st Prime
import math
import time
 
def primecheck(n):
    i = 3
    while i < int(math.sqrt(n))+1:
        if n % i == 0:
            return False
        i += 2
    return True

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



start = time.time()
prime = prime_x(50001)
elapsed = (time.time() - start)

print "found %s in %s seconds" % (prime,elapsed)