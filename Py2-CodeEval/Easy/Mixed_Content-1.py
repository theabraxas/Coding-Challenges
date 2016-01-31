import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.split(',')
    ints = []
    words = []
    string = ""
    for i in test:
        i = i.rstrip('\n')
        if i.isdigit():
            ints.append(i)
        elif type(i) == str:
            words.append(i)
    for i in words:
        string += i + ","
    string = string.strip()
    if len(string) > 1:
        string = string[:-1]
        string += '|'
    string = string.strip()
    for i in ints:
        string += i + ","
    print string[:-1].rstrip('\n')
test_cases.close()