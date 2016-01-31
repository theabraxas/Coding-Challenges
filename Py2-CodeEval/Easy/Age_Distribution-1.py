import sys
test_cases = open(sys.argv[1], 'r')

categories = {
    tuple(xrange(3)) : "Still in Mama's arms",
    tuple(xrange(3, 5)) : "Preschool Maniac",
    tuple(xrange(5, 12)) : "Elementary school",
    tuple(xrange(12, 15)) : "Middle school",
    tuple(xrange(15, 19)) : "High school",
    tuple(xrange(19, 23)) : "College",
    tuple(xrange(23, 66)) : "Working for the man",
    tuple(xrange(66, 101)) : "The Golden Years"
    }

for test in test_cases:
    age, human = int(test), False
    for i in categories.keys():
        if age in i:
            print categories[i]
            human = True
            break
    if not human:
        print "This program is for humans"
test_cases.close()