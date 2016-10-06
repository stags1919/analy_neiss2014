'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv
import re

# sort and write def
def calc_ratio(str_disp):
    print "+++analyze for "+str(str_disp)+""
    for k in data.keys():
        #print k
        if re.search(str_disp, k, re.IGNORECASE):
            for kk, v in sorted(data[k].items(), key=lambda x:x[1]):
                print kk,float(v)/float(sum(data[k].values()))
    print

### main 
# read DiagnosisCodes.csv
diagnosis = {}
r = csv.reader(open('DiagnosisCodes.csv', 'r'))
next(r)
for line in r:
    code = line[1]
    diagnosis[code] = line[0]

#print diagnosis

# read Disposition.csv
disposition = {}
r = csv.reader(open('Disposition.csv', 'r'))
next(r)
for line in r:
    code = line[1]
    disposition[code] = line[0]

#print disposition


# read NEISS2014.csv and make a list of disposition-diagnosis
data = {}
n_hospital = 0
r = csv.reader(open('NEISS2014.csv', 'r'))
next(r)
for line in r:
    code_disp = line[12]
    code_diag = line[9]
    buf_disp = disposition[code_disp]
    buf_diag = diagnosis[code_diag]
    if not data.has_key(buf_disp):
        data[buf_disp] = {} 
    if not data[buf_disp].has_key(buf_diag):
        data[buf_disp][buf_diag] = 1
    else:
        data[buf_disp][buf_diag] += 1

#print data

#analyze and write
calc_ratio("hospitalization")
calc_ratio("Left without being seen")
