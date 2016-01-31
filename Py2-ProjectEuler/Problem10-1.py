#Problem 10
import math
def primecheck(n):
    i = 3
    while i < int(math.sqrt(n))+1:
        if n % i == 0:
            return False
        i += 2
    return True

def prime_x(n):
    primes = 2 # 1 and 2
    count = 2
    iter = 3
    while iter < 2000000:
        if primecheck(iter):
            prime = iter
            count += prime
        iter += 2
    return count

result = prime_x(2000000)
print result