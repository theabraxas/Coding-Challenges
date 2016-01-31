import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.split(' ')
    new = ""
    line = ""
    for i in test:
        i = i.rstrip('\n')
        a = i[0]
        b = i[-1]
        c = i[1:-1]
        new = b + c + a
        line += new + " "
    print line.rstrip()
test_cases.close()