import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    print ' '.join(('{:.3f}'.format(f) for f in
                    sorted((float(i) for i in test.split()))))