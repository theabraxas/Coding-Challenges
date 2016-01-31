import sys
test_cases = open(sys.argv[1], 'r')
fibseries = [0, 1, 1]
for test in test_cases:
    if test:
        count = int(test)
        if count >= len(fibseries):
            while len(fibseries) <= count:
                nextfib = fibseries[-1] + fibseries[-2]
                fibseries.append(nextfib)
        print fibseries[count]
    
test_cases.close()