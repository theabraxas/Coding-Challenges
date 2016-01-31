#Problem 17
number = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

length = 0
for i in range(1,1001):
	i = str(i)
	if len(i) < 2:
		length += len(number[int(i)])
	elif len(i) == 2:
		if int(i) < 20:
			length += len(number[int(i)])
		elif int(i[1]) == 0:
			length += len(number[int(i)])
		else:
			x = int(i) % 10
			y = i[1]
			length += len(number[int(x)]) + len(number[int(y)])
	elif len(i) == 3:
		if i[1:3] == "00":
			length += len(number[int(i[0])]) + len(number[100])
		elif int(i[1:3]) < 21:
			x = int(i) % 100
			y = i[1:3]
			z = 3
			if int(i[1]) == 0:
				print i
				print int(i[1])
				print int(i[2])
				length += len(number[int(x)]) + len(number[100]) + z + len(number[int(i[2])])
				print len(number[int(x)]) + len(number[100]) + z + len(number[int(i[2])])
			else:
				length += len(number[int(x)]) + len(number[100]) + z + len(number[int(y)])
		else:
			print i
			w = 3
			x = int(i) / 100
			y = int(i[1]) * 10
			z = int(i[2:4])
			if z == 0:
				length += len(number[int(x)]) + len(number[100]) + len(number[int(y)]) + w
			else:
				length += len(number[int(x)]) + len(number[100]) + w + len(number[int(y)]) + len(number[int(z)])
	elif len(i) == 4:
		length += len("onethousand")

print length