import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = ""
    past = ""
    for c in test:
        if c == past:
            line = line
        else:
            line += c
        past = c
    print line
test_cases.close()