#challenge 1
import sys
import csv
import dateutil.parser
import datetime
from pprint import pprint

d = {}

with open("turnstile1.txt", "r") as file:
    reader = csv.reader(file)
    next(reader, None)
    for num, row in enumerate(reader):
    	if num  == 1000:
        	break
        key = tuple(row[0:4])
        value = row[4:]
        d.setdefault(key,[])
        d[key].append(value)

        

#print d [('A002','R051','02-00-01','LEXINGTON AVE')]

#challenge 2
import dateutil.parser
d2 ={}

for k, v in d.iteritems():
	list2 = []
	for index, el in enumerate(v):
		if index == 0:
			continue
		datetimecombo = el[2] +" " + el[3]
		date2 = dateutil.parser.parse(datetimecombo)
		count = int(el[5]) - int(v[index-1][5])
		list2= [ date2, count ]

		if k in d2:
			d2[k].append(list2)
		else:
			d2[k] = [ list2 ]

pprint(d2)
		
#challenge 3
sum_val = 0
new = 6


	

        