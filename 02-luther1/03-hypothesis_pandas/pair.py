import sys

for line in sys.stdin:
    line = line[:-1]            # remove trailing newline
    print line[::-1]            # print out reversed
