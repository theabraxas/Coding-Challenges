import sys
test_cases = open(sys.argv[1], 'r')
phrases = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]
counter = 0
toggle = 0
for test in test_cases:
    newline = ""
    for i in test:
        if counter > 7:
            counter = 0
        if i == "!" or i == "." or i == "?":
            if toggle == 0:
                toggle = toggle + 1
                newline += i
            else:
                newline += phrases[counter]
                counter += 1
                toggle = toggle - 1
        else:
            newline += i
    newline = newline.strip()
    print newline

test_cases.close()