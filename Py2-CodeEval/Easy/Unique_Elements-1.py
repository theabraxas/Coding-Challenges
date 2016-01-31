import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    test = test.split(',')
    output = ""
    uniques = []
    for i in test:
        if int(i) not in uniques:
            uniques.append(int(i))
    unique = sorted(uniques)
    for i in uniques:
        output += str(i) + ","
    print output[0:-1]
test_cases.close()