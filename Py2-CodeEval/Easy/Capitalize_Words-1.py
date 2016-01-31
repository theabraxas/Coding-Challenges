import sys
for line in open(sys.argv[1], 'r'):
    if line.strip():
        output = ''
        for word in line.split():
            output += word[0].capitalize() + word[1:] + ' '
        print(output[:-1])