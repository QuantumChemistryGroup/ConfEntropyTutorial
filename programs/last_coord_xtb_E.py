#!/usr/bin/python
import sys, string
from math import *
import re

# to write the input to td programs


# Main program starts here

# to get the last coordinates from gaussian out

# to grab the integer

def find_int(N):
	F = re.findall(r'[0-9 ]+', N)
	F = int(F[0])
	return F




f = open(sys.argv[1])

s = f.readline()
i = 0
E = 'NaN'
for line in f:  # for each line in a file
	if 'final structure' in line: 
		i = i + 1
	elif ':: total energy' in line:
		d = str.split(line)
		E = float(d[3])       

#print i

f.seek(0)
s = f.readline()

for j in range(i):
	while str.find(s, 'final structure') == -1 and s != "": 
                s = f.readline()
	s = f.readline()

s = f.readline()
s = f.readline()
s = f.readline()
coord = []
while str.find(s, "Bond Distances") == -1:
	d = str.split(s)
	if len(d) == 4:
		g = [d[0], d[1], d[2], d[3]]
		coord.append(g)
	s = f.readline()

f.close()
fil = open(sys.argv[1][0:-4]+'.xyz', 'w')

fil.write('   '+str(len(coord))+'\n')
fil.write('   '+str(E)+'\n')
for i in range(len(coord)):
	fil.write('%2s %18s %18s %18s\n' % (coord[i][0], coord[i][1], coord[i][2], coord[i][3] ))
