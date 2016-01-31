import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.split()
    fizz = int(test[0])
    buzz = int(test[1])
    num_range = int(test[2]) + 1
    line = ""
    for i in range(1,num_range):
        if i % fizz == 0 and i % buzz == 0:
            line += "FB "
        elif i % fizz == 0:
            line += "F "
        elif i % buzz == 0:
            line += "B "
        else:
            line += str(i) + " "
    print line[:-1]
test_cases.close()