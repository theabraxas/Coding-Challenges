import sys
for n in range(1,13):
    line = ""
    for i in range(1,13):
        x = n * i
        x = str(x)
        if len(x) == 1:
            line = line + "   " + x
        elif len(x) == 2:
            line = line + "  " + x
        else:
            line = line + " " + x
    print line.lstrip()