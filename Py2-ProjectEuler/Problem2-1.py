sumoffibs = 0
lastint = 1
sectolastint = 1
nextint = 0
while lastint <= 4000000:
	nextint = lastint + sectolastint
	sectolastint = lastint
	if lastint % 2 == 0:
		sumoffibs += lastint
	lastint = nextint
else:
	print sumoffibs