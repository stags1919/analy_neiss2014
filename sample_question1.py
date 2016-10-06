'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv

# read BodyParts.csv
body = {}
r = csv.reader(open('BodyParts.csv', 'r'))
next(r)
for line in r:
    code = line[1]
    body[code] = line[0]

# read NEISS2014.csv and count each body parts
data = {}
r = csv.reader(open('NEISS2014.csv', 'r'))
next(r)
for line in r:
    code = line[11]
    if data.has_key(code):
        data[code] += 1
    else:
        data[code] = 1 

# sort and write
for k, v in sorted(data.items(), key=lambda x:x[1]):
    print "'"+str(body[k])+"'",",", v