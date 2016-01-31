import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    newline = ""
    for char in test:
        if char.isalpha() == True:
            if char.islower() == True:
                char = char.upper()
                newline += char
            else:
                char = char.lower()
                newline += char
        else:
            newline += char
    print newline[:-1]
            
test_cases.close()
