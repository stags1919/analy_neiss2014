'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv
from readfile import Readfile


# read BodyParts.csv by class Readfile
read = Readfile()
read.read_codename("bodypart")
body = {}
body = read.get_codename()

# read NEISS2014.csv and count each body parts
data = {}
r = csv.reader(open('NEISS2014.csv', 'r'))
next(r)
for line in r:
    code = int(line[11])
    if data.has_key(code):
        data[code] += 1
    else:
        data[code] = 1 

# sort and write
for k, v in sorted(data.items(), key=lambda x:x[1]):
    print "'"+str(body[k])+"'",",", v