import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.split()
    print words[len(words)-2]
test_cases.close()
