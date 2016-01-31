import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    items = test.split('|')
    string = str(items[0])
    var = items[1].strip()
    output = ""
    nums = var.split()
    for i in nums:
        output+=string[int(i)-1]
    print output
test_cases.close()