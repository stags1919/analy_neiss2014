'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv
import re
from readfile import Readfile

# sort and write def
def calc_ratio(str_disp):
    print "+++analyze for "+str(str_disp)+""
    for k in data.keys():
        if re.search(str_disp, k, re.IGNORECASE):
            for kk, v in sorted(data[k].items(), key=lambda x:x[1]):
                print kk,float(v)/float(sum(data[k].values()))
    print

### main 
# read DiagnosisCodes.csv
read = Readfile()
read.read_codename("diagnosis")
diagnosis = {}
diagnosis = read.get_codename()


# read Disposition.csv
read = Readfile()
read.read_codename("disposition")
disposition = {}
disposition = read.get_codename()


# read NEISS2014.csv and make a list of disposition-diagnosis
data = {}
n_hospital = 0
r = csv.reader(open('NEISS2014.csv', 'r'))
next(r)
for line in r:
    code_disp = int(line[12])
    code_diag = int(line[9])
    buf_disp = disposition[code_disp]
    buf_diag = diagnosis[code_diag]
    if not data.has_key(buf_disp):
        data[buf_disp] = {} 
    if not data[buf_disp].has_key(buf_diag):
        data[buf_disp][buf_diag] = 1
    else:
        data[buf_disp][buf_diag] += 1


#analyze and write
calc_ratio("hospitalization")
calc_ratio("Left without being seen")
