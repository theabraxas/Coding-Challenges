import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    items = test.split('|')
    
    fhalf = items[0].split()
    shalf = items[1].split()
    
    final = ""
    
    for i in range(len(fhalf)):
        count = 1
        mult = int(fhalf[i]) * int(shalf[i])
        final += str(mult) + " "
    
    print final[:-1]
test_cases.close()
