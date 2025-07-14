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
for line in f:  # for each line in a file
	if 'final structure' in line: 
                i = i + 1

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

#print (coord)
# to fine the multiplecity
f.seek(0)
while str.find(s, "unpaired electrons") == -1 and s != "": 
        s = f.readline()
d = str.split(s)

mult = ''
if (len(d)>1) and (d[1] == 'unpaired'):
	mult = 2*int(d[3])*0.5 + 1
	mult = int(mult)
	print ('found m=',mult)
else:
	mult = 1

# to find the rotational symmetry number
f.seek(0)
sigma = 1
for line in f:
	if 'rotational number' in line:
		d = str.split(line)
		sigma = int(d[-2])
sigma = 1

# to find the last frequencies
f.seek(0)
i = 0
for line in f:  # for each line in a file
	if 'projected vibrational frequencies' in line: 
		i = i + 1    
print (i, "The number of frequencies jobs")

f.seek(0)
s = f.readline()


# to stop at the last mention of the frequencies!!!
for j in range(i):
	while str.find(s, 'projected vibrational frequencies') == -1 and s != "": 
		s = f.readline()
	s = f.readline()


#print s

freq = []
j=0
while str.find(s, "reduced masses") == -1:
	if 'eigval' in s:
		d = str.split(s)
		for i in range(2,len(d),1):
			if (float(d[i]) < 0) and (j>5):
				print ('Warning, imaginary frequency has been found: ', d[i])
				print ('Make it real anyway')
				freq.append(str(float(d[i])*-1))
			else:
				freq.append(d[i])		
			j=j+1
	s = f.readline()

# check if the first 6 frequencies are all zeroes 

if len(coord) > 2:
	tr_rotation = freq[0:6]
else:
	tr_rotation = freq[0:5]
NORM = True
for i in range(len(tr_rotation)):
	if abs(float(tr_rotation[i])) < 0.1:
		pass
	else:
		print ('please, pay attention to vibration: ', i)
		NORM = False

if NORM == True:
	if len(coord) > 2:
		freq = freq[6:]
	else:
		freq = freq[5:]         
else:
	print ('there is something wrong with the first 6 frequencies. exit.')
	exit(0)


# to check whether there is the internal rotation
Internal_rotation = False
if len(sys.argv)>2:
	if sys.argv[2] == 'ir':
		Internal_rotation = True


### to write everything in the file


fil = open(sys.argv[1][0:-4]+'.dat', 'w')

fil.write('\n')
fil.write('$molecule\n')
for i in range(len(coord)):
	fil.write('%2s %12s %10s %10s\n' % (coord[i][0], coord[i][1], coord[i][2], coord[i][3] ))
fil.write('$end\n')
fil.write('$temperature\n')	
fil.write('298.15\n')
fil.write('$end\n')	
fil.write('$mult\n')	
fil.write('%2i\n' % (mult))
fil.write('$end\n')	
fil.write('$sigma\n')	
fil.write('%2i\n' % (sigma))
fil.write('$end\n')	
fil.write('$pressure\n')	
fil.write('1.00000\n')
fil.write('$end\n')	
fil.write('$scale\n')
scale = sys.argv[2]	
fil.write(scale+'\n')
fil.write('$end\n')
# get msRRHO parameters
fil.write('$msrrho\n')
fil.write('$end\n')		
fil.write('$freq\n')	
for i in range(len(freq)):
	fil.write('%2s\n' % (freq[i]))
fil.write('$end\n')	


# if there is an internal rotation

if Internal_rotation:
	fil.write('$bond\n')	
	fil.write('specify the bond\n')
	fil.write('$end\n')	
	fil.write('$freq_rotor\n')	
	fil.write('freq correspond the rotor\n')
	fil.write('$end\n')	
	fil.write('$rotor\n')	
	fil.write('rotor\n')
	fil.write('$end\n')	
	fil.write('$accuracy\n')	
	fil.write('0.003\n')
	fil.write('$end\n')	
	fil.write('$steps\n')	
	fil.write('2300\n')
	fil.write('$end\n')	
	fil.write('$potential\n')	
	fil.write('...\n')
	fil.write('$end\n')	
