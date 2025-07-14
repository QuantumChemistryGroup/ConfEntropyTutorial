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


def IsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False


f = open(sys.argv[1])

s = f.readline()

i = 0
for line in f:  # for each line in a file
	if 'Atomic Coordinates:' in line: i = i + 1   
print (i)

f.seek(0)
s = f.readline()



for j in range(i):
	while str.find(s, " Atomic Coordinates") == -1 and s != "": s = f.readline()
	s = f.readline(1)


elements = {
        'H ': ' 1 ',
        'He ': ' 2 ',
        'Li ': ' 3 ',
        'Be ': ' 4 ',
        'B ': ' 5 ',
        'C ': ' 6 ',
        'N ': ' 7 ',
        'O ': ' 8 ',
        'F ': ' 9 ',
        'Ne ': ' 10 ',
        'Na ': ' 11 ',
        'Mg ': ' 12 ',
        'Al ': ' 13 ',
        'Si ': ' 14 ',
        'P ': ' 15 ',
        'S ': ' 16 ',
        'Cl ': ' 17 ',
        'Ar ': ' 18 ',
        'K ': ' 19 ',
        'Ca ': ' 20 ',
        'Sc ': ' 21 ',
        'Ti ': ' 22 ',
        'V ': ' 23 ',
        'Cr ': ' 24 ',
        'Mn ': ' 25 ',
        'Fe ': ' 26 ',
        'Co ': ' 27 ',
        'Ni ': ' 28 ',
        'Cu ': ' 29 ',
        'Zn ': ' 30 ',
        'Ga ': ' 31 ',
        'Ge ': ' 32 ',
        'As ': ' 33 ',
        'Se ': ' 34 ',
        'Br ': ' 35 ',
        'Kr ': ' 36 ',
        'Rb ': ' 37 ',
        'Sr ': ' 38 ',
        'Y ': ' 39 ',
        'Zr ': ' 40 ',
        'Nb ': ' 41 ',
        'Mo ': ' 42 ',
        'Tc ': ' 43 ',
        'Ru ': ' 44 ',
        'Rh ': ' 45 ',
        'Pd ': ' 46 ',
        'Ag ': ' 47 ',
        'Cd ': ' 48 ',
        'In ': ' 49 ',
        'Sn ': ' 50 ',
        'Sb ': ' 51 ',
        'Te ': ' 52 ',
        'I ': ' 53 ',
        'Xe ': ' 54 ',
        'Cs ': ' 55 ',
        'Ba ': ' 56 ',
        'La ': ' 57 ',
        'Ce ': ' 58 ',
        'Pr ': ' 59 ',
        'Nd ': ' 60 ',
        'Pm ': ' 61 ',
        'Sm ': ' 62 ',
        'Eu ': ' 63 ',
        'Gd ': ' 64 ',
        'Tb ': ' 65 ',
        'Dy ': ' 66 ',
        'Ho ': ' 67 ',
        'Er ': ' 68 ',
        'Tm ': ' 69 ',
        'Yb ': ' 70 ',
        'Lu ': ' 71 ',
        'Hf ': ' 72 ',
        'Ta ': ' 73 ',
        'W ': ' 74 ',
        'Re ': ' 75 ',
        'Os ': ' 76 ',
        'Ir ': ' 77 ',
        'Pt ': ' 78 ',
        'Au ': ' 79 ',
        'Hg ': ' 80 ',
        'Tl ': ' 81 ',
        'Pb ': ' 82 ',
        'Bi ': ' 83 ',
        'Po ': ' 84 ',
        'At ': ' 85 ',
        'Rn ': ' 86 ',
        'Fr ': ' 87 ',
        'Ra ': ' 88 ',
        'Ac ': ' 89 ',
        'Th ': ' 90 ',
        'Pa ': ' 91 ',
        'U ': ' 92 ',
        'Np ': ' 93 ',
        'Pu ': ' 94 ',
        'Am ': ' 95 ',
        'Cm ': ' 96 ',
        'Bk ': ' 97 ',
        'Cf ': ' 98 ',
        'Es ': ' 99 ',
        'Fm ': ' 100 ',
        'Md ': ' 101 ',
        'No ': ' 102 ',
        'Lr ': ' 103 ',
        'Rf ': ' 104 ',
        'Db ': ' 105 ',
        'Sg ': ' 106 ',
        'Bh ': ' 107 ',
        'Hs ': ' 108 ',
        'Mt ': ' 109 ',
        'Ds ': ' 110 ',
        'Rg ': ' 111 ',
        'Cn ': ' 112 ',
        'Uut ': ' 113 ',
        'Fl ': ' 114 ',
        'Uup ': ' 115 ',
        'Lv ': ' 116 ',
        'Uuh ': ' 117 ',
        'Uuh ': ' 118 ',
}

coordinates = []

while str.find(s, '#') == -1:
	s = f.readline()
	new = s
	for key in elements.keys():
		new = new.replace(elements[key], key)
	coordinates.append(new)
coordinates = coordinates[0:-1]
coordinates[0] =  '  '+str(coordinates[0]) 
f.seek(0)


# to fine the multiplecity
mult = int(sys.argv[1][1])

# to find the rotational symmetry number

sigma = 1

# to find the last frequencies
f.seek(0)
i = 0
for line in f:  # for each line in a file
	if 'VIBRATIONAL ANALYSIS and THERMOCHEMISTRY' in line: 
		i = i + 1    
print (i, "The number of frequencies jobs")

f.seek(0)
s = f.readline()


# to stop at the last mention of the frequencies!!!
for j in range(i):
	while str.find(s, 'VIBRATIONAL ANALYSIS and THERMOCHEMISTRY') == -1 and s != "": 
		s = f.readline()
	s = f.readline()


s = f.readline()
#print s
while str.find(s, 'Mode | Freq.   | Mass.') == -1 and s != "": 
	s = f.readline()
s = f.readline()
s = f.readline()
#print (s)

freq = []
while str.find(s, "*------*---------*--------*") == -1:
	d = str.split(s)
	if IsFloat(d[3]) == True:
		freq.append(d[3])
	else:
		F = re.findall(r"[-+]?\d*\.\d+|\d+", d[3])[0]
		print ('Warning, imaginary frequency has been found: ', d[3])
		freq.append(F)
	s = f.readline()


# to check whether there is the internal rotation
Internal_rotation = False
if len(sys.argv)>3:
	if sys.argv[3] == 'ir':
		Internal_rotation = True


### to write everything in the file


fil = open(sys.argv[1][0:-3]+'dat','w')

fil.write('\n')
fil.write('$molecule\n')
for i in range(len(coordinates)):
	fil.write(coordinates[i])
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
