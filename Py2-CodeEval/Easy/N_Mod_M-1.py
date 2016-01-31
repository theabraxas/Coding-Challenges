import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n, m = (int(i) for i in test.split(','))
    print n - (int(n / m) * m)

test_cases.close()
