import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip()
    numbers = test.split(';')
    string = ""
    for word in numbers:
        if word == "zero":
            string += "0"
        if word == "one":
            string +="1"
        if word == "two":
            string +="2"
        if word == "three":
            string += "3"
        if word == "four":
            string +="4"
        if word == "five":
            string += "5"
        if word == "six":
            string +="6"    
        if word == "seven":
            string += "7"
        if word == "eight":
            string +="8"
        if word == "nine":
            string += "9"
    print string
test_cases.close()