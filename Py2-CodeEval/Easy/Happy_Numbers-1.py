import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test)
    primer = 1
    history = []
    old = 0
    while test != 1:
        temp = []
        history.append(old)
        old = 0
        for i in str(test):
            temp.append(int(i) * int(i))
        test = 0
        for i in temp:
            test = int(test) + i
        old = test
        if test in history and primer > 1:
            print 0
            test = 1
        else:
            if test == 1:
                print 1
        primer = 2
test_cases.close()