#Problem 37
import math
import time
start_time = time.clock()
def primecheck(n):
    i = 2
    while i < int(math.sqrt(n))+1:
        if n % i == 0:
            return False
        i += 1
    return True

#Generate List of Primes
listofprimes = [2,3,5,7]
for i in range(11,1000000,2):
    if primecheck(i) == True:
        listofprimes.append(i)

#Check if primes are palindromes

primepals = []
for i in listofprimes:
    primepals.append(int(i))

trunkprimepals = []
for i in primepals:
    x = str(i)
    y = x
    check = "Yes"
    for j in range(0,len(x)):
        if primecheck(int(x)) is not True or x[0] == "0" or x == "1":
            check = "No"
        x = x[1:]
    if check == "Yes":
        z = y
        for j in range(0,len(z)):
            if primecheck(int(z)) is not True or z[0] == "0" or z == "1":
                check = "No"
            z = z[:-1]
    if check == "Yes":
        trunkprimepals.append(i)

thesum = 0
print trunkprimepals

for i in trunkprimepals:
    if i not in [2,3,5,7]:
        thesum += int(i)

print time.clock() - start_time
print thesum