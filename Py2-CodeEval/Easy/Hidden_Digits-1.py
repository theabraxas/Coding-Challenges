import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    original = ""
    hidden = ""
    empty = False
    go = True
    for char in test:
        if char == 'a':
            hidden += "0"
            go = False
        elif char == 'b':
            hidden += "1"
            go = False
        elif char == 'c':
            hidden += "2"
            go = False
        elif char == 'd':
            hidden += "3"
            go = False
        elif char == 'e':
            hidden += "4"
            go = False
        elif char == 'f':
            hidden += "5"
            go = False
        elif char == 'g':
            hidden += "6"
            go = False
        elif char == 'h':
            hidden += "7"
            go = False
        elif char == 'i':
            hidden += "8"
            go = False
        elif char == 'j':
            hidden += "9"
            go = False
        elif char.isdigit() == True:
            hidden += char
            go = False
        elif go == True:
            empty = True
    if hidden == original:
        print "NONE"
    else:
        print hidden
test_cases.close()