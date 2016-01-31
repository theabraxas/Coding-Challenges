#Largest Prime Factor
import math
thenum= 600851475143
i = 2
while i * i < thenum:
	if thenum % i == 0:
		thenum = thenum / i
	i += 1
print thenum

# n = 600851475143
# i = 2
# while i * i < n:
#     while n % i == 0:
#         n = n / i
#     i = i + 1
# print n