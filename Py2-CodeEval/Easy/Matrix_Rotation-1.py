import sys
import math
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    array = test.split()
    length = len(array)
    sroot = int(math.sqrt(length))
    rotatedline = []
    adjusted = sroot+1

    for i in range(1,adjusted):
        for j in range(1, adjusted):
            index = (sroot * (sroot - j) + i) - 1
            rotatedline += array[index]
    print ' '.join(rotatedline)


test_cases.close()
