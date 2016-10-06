'''
Created on 2016/05/30

@author: Daisuke MUrakami
'''

import csv
  
class Readfile:
    def __init__(self):
        self.str=""
        self.factor={}
    def read_codename(self,str):
        self.str=str
        if self.str == "diagnosis":
            fname = "DiagnosisCodes.csv"
        elif self.str == "bodypart":
            fname = "BodyParts.csv"
        elif self.str == "disposition":
            fname = "Disposition.csv"
        elif self.str == "location":
            fname = "locate_code.csv"
        r = csv.reader(open(fname, 'r'))
        next(r)
        for line in r:
            code = int(line[1])
            self.factor[code] = line[0]
    def get_codename(self):
        return self.factor
        
