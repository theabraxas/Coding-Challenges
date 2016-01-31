import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    state = True
    the_range = len(test) -1
    for i in range(0,9):
        for char in test:
            if int(char) == test.count(str(i)):
                state = True
            else:
                state = False
    if state == True:
        print "1"
    else:
        print "0"

test_cases.close()