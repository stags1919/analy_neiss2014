'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv
import re

# read NEISS2014.csv and count body
data = {}
ave_age = 0
n_skate = 0
n_female = 0

# read data
r = csv.reader(open('NEISS2014.csv', 'r'))
next(r)
i=0
for line in r:
    narr = line[17]
    #re.search("skateboard", narr, re.IGNORECASE)
    if re.search("skateboard", narr, re.IGNORECASE):
        i+=1
        #print i,narr
        n_skate += 1
        ave_age += float(line[5])
        sex = line[6]
        if re.search("Female", sex, re.IGNORECASE):
            n_female += 1

ave_age /= float(n_skate)

# write
print "a number of injuries of a skateboard = ", n_skate
print "Male = ", float(n_skate-n_female)*100.0/float(n_skate), "%, FeMale = ", float(n_female)*100.0/float(n_skate), "%"
print "average of age =", ave_age