import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    chars = []
    length = 0
    for x in test.strip():
        if x in chars:
            break
        else:
            length += 1
            chars += x
    print str(length)
test_cases.close()