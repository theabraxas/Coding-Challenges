with open("Problem13Input.txt", "r") as f:
	bigint = 0
	for line in f.readlines():
		bigint += int(line)
	print str(bigint)[0:10]