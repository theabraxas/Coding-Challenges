import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if len(test) > 55:
        test = test[:40].rsplit(' ', 1)[0] + '... <Read More>'
    print test

test_cases.close()
