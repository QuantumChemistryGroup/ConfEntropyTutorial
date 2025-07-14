#!/usr/bin/python
import sys, string
from math import *




# Main program starts here

atoms = []
x = []
y = []
z = []
g = []
el = []
a = []
coord = []
E = 'NaN'
f = open(sys.argv[1])

s = f.readline()
i = 0
for line in f:  # for each line in a file
	if 'CARTESIAN COORDINATES (ANGSTROEM)' in line: i = i + 1   
print (i)

f.seek(0)
for line in f:
	if 'FINAL SINGLE POINT' in line:
		d = str.split(line)
		E = d[-1]
f.seek(0)
s = f.readline()



for j in range(i):
	while str.find(s, 'CARTESIAN COORDINATES (ANGSTROEM)') == -1 and s != "": s = f.readline()
	s = f.readline()

s = f.readline()
#s = f.readline()
#print s

while str.find(s, "--------") == -1:
	d = str.split(s); 
	if len(d) == 4:
		g = (d[0], d[1], d[2], d[3])
		coord.append(g); s = f.readline()
	else: 
		print ("All the coordinates read")
		s = f.readline()



for q in coord:
	t1, t2, t3, t4 = q
	el.append(t1), x.append(t2), y.append(t3), z.append(t4)



f = open(sys.argv[1][0:-3]+'xyz','w')
f.write(str(len(el))+'\n')
f.write('      '+E+'\n')
for i in range(len(el)):
	f.write('%2s %12s %12s %12s\n' % (el[i], x[i], y[i], z[i] ))
f.close()
	




