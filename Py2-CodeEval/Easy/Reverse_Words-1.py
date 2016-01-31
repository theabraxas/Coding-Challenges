import sys
import re
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
        z = re.split('\W+',test)
        z.reverse()
        print ' '.join(z)
test_cases.close()