#Set Intersection

import sys
test_cases = open('SetIntersection.txt', 'r')
for test in test_cases:
	if len(test) > 1:
		# print "This is iteration " + str(count)
		line = test.strip()
		string1 = line.split(';')[0]
		string2 = line.split(';')[1]
		numstr = ""
		str1nums = []
		str2nums = []
		intersection = []
		string = ""
		los = []
		for i in string1:
			if i == ',':
				str1nums.append(numstr)
				numstr = ""
			else: 
				numstr += i
		for i in string2:
			if i == ',':
				str2nums.append(numstr)
				numstr = ""
			else: 
				numstr += i
		for i in str1nums:
			if i in str2nums:
				intersection.append(i)
		for i in intersection:
			string += str(i) + " "
		los.append(string)
		if los:
			for i in los:
				if len(str(i)) > 1:
					print str(i)
				else:
					print ""
test_cases.close()