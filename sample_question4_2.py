# coding: utf-8
'''
Created on 2016/05/25

@author: Daisuke Murakami
'''

import csv
from readfile import Readfile

dimension={}
dimension[0] = "bodypart"
dimension[1] = "diagnosis"
dimension[2] = "disposition"
dimension[3] = "location"

data = {}
factor = {}
for i,k in dimension.items():
    data[i] = {}
    # set codename such as factor[0][94]="Ear" from Bodypart.csv by class Readfile
    factor[i] = {}
    read = Readfile()
    read.read_codename(dimension[i])
    factor[i] = read.get_codename()
    r = csv.reader(open('NEISS2014.csv', 'r'))
    next(r)
    for line in r:
        # read age and grouping
        age = int(line[5])
        if age>=100:
            buf_age=10
        else:
            buf_age = int(float(age)/10)
        # read code
        if k=="diagnosis":
            code = int(line[9])
        elif k=="bodypart":
            code = int(line[11])
        elif k=="disposition":
            code = int(line[12])
        elif k=="location":
            code = int(line[13])
        
        if not data[i].has_key(code):
            data[i][code] = {} 
        if not data[i][code].has_key(buf_age):
            data[i][code][buf_age] = 1
        else:
            data[i][code][buf_age] += 1
    
    # calc ratio to the total in each dimension
    buf_sum = 0
    for v in data[i].values():
        buf_sum += sum(v.values())
    for j,v in data[i].items():
        for jj in data[i][j].keys():
            data[i][j][jj] /= float(buf_sum)
            data[i][j][jj] *= 100.0 #percentage            
    #check exist codename
    for ii in data[i].keys():
        if not ii in factor[i]:
            factor[i][ii] = "null"

#+++ generate table formatted by html
f = open("age_relation.html","w") 
width=75
fsize=3.5
buf="<html>"\
    "<head>"\
    "<title>Age - injure relationship [%] </title>"\
    "</head>"\
    "<body>"\
    "<table border=2 rules=group cellspacing=0 cellpadding=1.5><tr bgcolor=#ffffc0>"\
    "<caption>Age - injure relationship [%]</caption>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>Dimension</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>Detail</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>under 10</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>10's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>20's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>30's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>40's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>50's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>60's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>70's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>80's</b></font></td>"\
    "<td width="+str(width)+" align=center><font size="+str(fsize)+"><b>90's</b></font></td>"\
    "<td><font size=3.5><b>over 100</b></font></td>"\
    "</tr>"

f.write(buf)
for i,k in dimension.items():
    f.write("<tbody border=1>")
    nc = 0
    for ii in data[i].keys():
        f.write("<tr>")
        if nc == 0:
            num_row = len(data[i])
            f.write("<th align=center rowspan="+str(num_row)+")>"+str(k)+"</th>\n")
        f.write("<td align=center>"+str(factor[i][ii][0:30])+"</td>\n")
        for iii in range(0,11,1):
            ratio = "-"
            #set color for higher percentage:red, lower one: blue
            color = "ffffff" 
            if data[i][ii].has_key(iii):
                ratio = round(data[i][ii][iii],3)
                if ratio > float(100)/(num_row*11)*1.9:
                    color = "ff0000"
                elif ratio > float(100)/(num_row*11)*1.75:
                    color = "ff4646"
                elif ratio > float(100)/(num_row*11)*1.5:
                    color = "ffaaaa"
                elif ratio < float(100)/(num_row*11)*0.1:
                    color = "7476d6"
                elif ratio < float(100)/(num_row*11)*0.25:
                    color = "9c9ee2"
                elif ratio < float(100)/(num_row*11)*0.5:
                    color = "bdbeec"    
            else:
                color = "7476d6"
                             
            f.write("<td bgcolor="+str(color)+" align=center>"+str(ratio)+"</td>\n")
        f.write("</tr>")
        nc += 1
    f.write("</tbody>")
f.write("</table>")
f.write("</body>")
f.write("</html>")

f.close()

