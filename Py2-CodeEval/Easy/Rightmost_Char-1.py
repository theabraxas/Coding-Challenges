import sys
test_cases = open(sys.argv[1], 'r')
last = -1
for test in test_cases:
    test = test.strip()
    search = test[-1:]
    test = test[:-1]
    y = 0
    for x in test:
        if x == search:
            last = y
        y += 1
    if last == -1:
        print str(-1)
    else:
        print str(last)
    last = -1
test_cases.close()