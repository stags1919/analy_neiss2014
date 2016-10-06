# coding: utf-8
'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv
import matplotlib.pyplot as plt
import numpy as np
from readfile import Readfile

# for stack bar charts 
def plt_stack():
    ind = np.arange(len(data_plot))    #locate bar（x-axis）
    title = "Age - "+dimension+""
    width = 0.35    #bar width
    bottom=np.zeros(data_plot.shape[0])
    for i in range(data_plot.shape[1]):
        plt.bar(ind,                
                data_plot[:,i],        # height for each factor
                width,              
                bottom,             # reference point for bar 
                #color=colors[i],
                label=label[i] 
                )
        bottom += data_plot[:,i]   # stacking
        # set visualize    
    margin = 0.25
    plt.xlim(-margin, len(data_plot)-1+width+margin)   # adjust range
    plt.xticks(ind+width/2., xtics_factor,fontsize=8) # xtics
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.legend(bbox_to_anchor=(1.05, 1), loc = 'upper left', borderaxespad=0,fontsize=8,ncol=1) 
    plt.subplots_adjust(right=0.7,bottom=0.2,left=0.2) #adjust space
    #plt.savefig("age_"+dimension+".png") #generate graph png file
    plt.show()
    
### main
data = {}
dimension = "location"  # bodypart | diagnosis | disposition | location
factor = {}
# read codename from class readfile
read = Readfile()
read.read_codename(dimension)
factor = read.get_codename()
# read data
r = csv.reader(open('NEISS2014.csv', 'r'))
next(r)
for line in r:
    # read age and grouping
    age = int(line[5])
    if age>=100:
        buf_age=10
    else:
        buf_age = int(float(age)/10)
        
    if dimension=="diagnosis":
        code = int(line[9])
    elif dimension=="bodypart":
        code = int(line[11])
    elif dimension=="disposition":
        code = int(line[12])
    elif dimension=="location":
        code = int(line[13])
    
    # count data
    if not data.has_key(buf_age):
        data[buf_age] = {} 
    if not data[buf_age].has_key(code):
        data[buf_age][code] = 1
    else:
        data[buf_age][code] += 1

#check exist codename
for k in data.keys():
    for kk in data[k].keys():
        if not kk in factor.keys():
            factor[kk] = "null"

#++ generate data for plot
len_d = len(factor)
data_plot=np.array([[0 for i in range(len_d)] for j in range(11)])
label=[0 for i in range(len_d)]

xtics_factor=[0 for i in range(len(data.keys()))]

for k in range(min(data.keys()),max(data.keys())+1,1):
    nc = 0    
    for kk in factor.keys():
        label[nc] = factor[kk][0:20]
        if data[k].has_key(kk):
            data_plot[k][nc] = data[k][kk] 
        nc+=1
    #set xtics factor
    if k==0:
        xtics_factor[k] = "u10"
    elif k==10:
        xtics_factor[k] = "o100"
    else:
        kage=k*10
        xtics_factor[k] = ""+str(kage)+"'s"

#++ write graph
plt_stack()
