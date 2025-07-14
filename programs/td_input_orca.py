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
	if 'CARTESIAN COORDINATES (ANGSTROEM)' in line: 
                i = i + 1

#print i

f.seek(0)
s = f.readline()

for j in range(i):
	while str.find(s, 'CARTESIAN COORDINATES (ANGSTROEM)') == -1 and s != "": 
                s = f.readline()
	s = f.readline()

s = f.readline()
coord = []
while str.find(s, "--------") == -1:
	d = str.split(s)
	if len(d) > 3:
		g = [d[0], d[1], d[2], d[3]]
		coord.append(g)
	s = f.readline()


# to fine the multiplecity
f.seek(0)
while str.find(s, "Multiplicity") == -1 and s != "": 
        s = f.readline()
d = str.split(s)
mult = int(d[-1])

# check for spin contamination

f.seek(0)
UHF = False
S2 = ''
for line in f:
        if 'Deviation                       :' in line:
                UHF = True
                d = str.split(line)
                S2 = d[-1]
if UHF == True:
	if float(S2) > 0.1:
		print ('Warning! Large spin contamination detected. Deviation from ideal S2: ', S2)

# to find the rotational symmetry number
f.seek(0)
while str.find(s, "Symmetry Number") == -1 and s != "": 
	s = f.readline()
d = str.split(s)
sigma = find_int(d[-1])
symm = str.split(d[2],',')[0]
if symm == 'C1':
	print ('No symmetry has been detected')
else:
	print ('ORCA has found a symmetry: ', symm)

# to find the last frequencies
f.seek(0)
i = 0
for line in f:  # for each line in a file
	if 'VIBRATIONAL FREQUENCIES' in line: 
		i = i + 1    
print (i, "The number of frequencies jobs")

f.seek(0)
s = f.readline()


# to stop at the last mention of the frequencies!!!
for j in range(i):
	while str.find(s, 'VIBRATIONAL FREQUENCIES') == -1 and s != "": 
		s = f.readline()
	s = f.readline()


s = f.readline()
#print s

freq = []
while str.find(s, "--------") == -1:
	d = str.split(s)
	if len(d) == 3:
		freq.append(d[1])
		if float(d[1]) < 0:
			print ('Warning, imaginary frequency has been found: ', d[1])
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
if len(sys.argv)>3:
	if sys.argv[3] == 'ir':
		Internal_rotation = True


### to write everything in the file


fil = open(sys.argv[1][0:-3]+'dat','w')

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
'''
try:
	if sys.argv[3].lower() == 'ho':
		fil.write('0.00001\n')
		fil.write('1000.0\n')
		fil.write('0\n')
	elif sys.argv[3].lower()[0:2] == 'gr':
		gr = []
		try:
			d = sys.argv[3].split('_')
			gr = [d[1], d[2], d[3]]
		except:
			print ("Your msRRHO parameters are not clear")
			print ("I am using the default: 100 4 1")
			gr = ['100', '4', '1']
		fil.write(gr[0]+'\n')
		fil.write(gr[1]+'\n')
		fil.write(gr[2]+'\n')
except:
	print ("Specify:")
	print ("HO = harmonic oscillator")
	print ("GR_100_4_0 = msRRHO, tau = 100, alpha = 4, enthapy is from HO")
	print ("GR_100_4_1 = msRRHO, tau = 100, alpha = 4, enthapy is corrected")
	sys.exit(0)
'''		
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
