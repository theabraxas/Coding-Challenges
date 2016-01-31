#First attempt to solve the problem, simple logical approach using way too many steps. 
##Can be improved by reducing number of variables (perhaps grab all 4 numbers on a first pass and assign types based on position
##It would also be simpler to track one '# of kids' variable instead of tracking vnum, znum, etc.

import sys
import re
test_cases = open(sys.argv[1], 'r')

#candy modifiers
vamps = 3
zombs = 4
witcz = 5

for test in test_cases:
    points = 0
    group = 0
    thelist = test.split(",")
    for i in thelist:
        if "Vampire" in i:
            vnum = int(re.search(r'\d+', i).group())
            points += (vnum * vamps)
            group += vnum
        elif "Zombie" in i:
            znum = int(re.search(r'\d+', i).group())
            points += (znum * zombs)
            group += znum
        elif "Witch" in i:
            wnum = int(re.search(r'\d+', i).group())
            points += (wnum * witcz)
            group += wnum
        elif "House" in i:
            houses = int(re.search(r'\d+', i).group())
        else:
            print "Bad input?"
    total_candies = points * houses
    cpk = total_candies / (vnum + znum +wnum)
    print cpk

test_cases.close()test