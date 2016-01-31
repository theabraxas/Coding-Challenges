import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test)
    test1 = test
    test2 = test
    counter = 1
    while test1 >= 10:
        test1 = test1 / 10
        counter += 1
    thesum = 0
    thecounter = counter
    while test >= 1:
        bleh = (test - test % 10 ** (counter - 1)) / (10 ** (counter -1))
        thesum += bleh ** thecounter
        test = test % 10 ** (counter-1)
        counter -= 1
    if thesum == test2:
        print "True"
    else:
        print "False"
        
test_cases.close()
