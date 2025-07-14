#!/usr/bin/python
from __future__ import division
import sys, string
import os
import re
import numpy

def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def IsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False



f = open(sys.argv[1], 'r')
i=0
while True:
	s = f.readline()
#	print s
	if not s:
		print ('EOF reached')
		break
	if IsInt(s) == True:
		# molecule start has been found
		Nat = int(s)
		E = 'NaN'
		s = f.readline()
		d = str.split(s)
		E = float(d[-1])
		s = f.readline()
		d = str.split(s)
		f1 = open(sys.argv[1][0:-4]+'_'+str(i)+'.xyz', 'w')
		f1.write(' '+str(Nat)+'\n')
		f1.write('   '+str(E)+'\n')
		if E == 'NaN':
			print("warning, E = NaN in ", sys.argv[1][0:-4]+'_'+str(i)+'.xyz')
		last_pos = f.tell()
		while len(d) == 4:
			f1.write(d[0]+'   '+d[1]+'   '+d[2]+'   '+d[3]+'\n')
			last_pos = f.tell()
			s = f.readline()
			d = str.split(s)
		f1.close()
		f.seek(last_pos)	
		i = i + 1
'''
	else:
		while IsInt(s) == True:
			d = str.split(s)
			f1 = open(sys.argv[1][0:-4]+'_'+str(i)+'.xyz', 'w')
			while len(d) == 4:
				f1.write(d[0]+'   '+d[1]+'   '+d[2]+'   '+d[3]+'\n')
				s = f.readline()
				d = str.split(s)
			f1.close()
			i = i + 1		
'''
f.close()
