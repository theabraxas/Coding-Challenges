import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	rc = ""
	toggle = 0
	for char in test:
		if char.isalpha() == True:
			if toggle == 0:
				rc += char.upper()
				toggle = 1
			elif toggle == 1:
				rc += char.lower()
				toggle = 0
		else:
			rc += char
	print rc
test_cases.close()