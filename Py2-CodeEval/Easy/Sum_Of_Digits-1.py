import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases.read().splitlines():
  print sum([int(c) for c in test])   