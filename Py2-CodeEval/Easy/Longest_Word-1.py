import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        sentences = test.split()
        max_word = ""
        for word in sentences:
            if len(max_word) < len(word):
                max_word = word
    print max_word
test_cases.close()
