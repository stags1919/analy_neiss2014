'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv
import re


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
r = csv.reader(open('NEISS2014.csv', 'r'))
next(r)
for line in r:
    code_disp = line[12]
    code_diag = line[9]
    buf_disp = disposition[code_disp]
    buf_diag = diagnosis[code_diag]
    if re.search("Left", buf_disp, re.IGNORECASE) and re.search("Other/Not Stated", buf_diag, re.IGNORECASE):
        buf_diag_other = line[10]
        #print buf_diag_other
        if data.has_key(buf_diag_other):
            data[buf_diag_other] += 1
        else:
            data[buf_diag_other] = 1
   
# write diag_other ratio         
for k, v in sorted(data.items(), key=lambda x:x[1]):
    print k,float(v)/float(sum(data.values()))
print

# PAIN, BACK PAIN, KNEE PAIN,... are grouped into "PAIN_all"
sum_pain = 0
data2 = {}
for k,v in data.items():
    if re.search("pain",k,re.IGNORECASE):
        sum_pain += float(v) 
        data2["PAIN_all"] = sum_pain
    else:
        data2[k] = v
# write ratio
for k, v in sorted(data2.items(), key=lambda x:x[1]):
    print k,float(v)/float(sum(data2.values()))

