#!/usr/bin/python
import sys, string, os, glob
from math import *






filelist = glob.glob('*.xyz')
#filelist = glob.glob('*B97-3c.out')

filelist.sort()
outputs=[]
all_lines = []
f = open('unique_out.txt', 'r')
for line in f:
	d = str.split(line)
	all_lines.append(d[0])		
f.close()
#print (all_lines)
for i in filelist:
	if i[0:-4]+'.out' in all_lines:
		os.system('cp '+i[0:-4]+'.dat'+' ..')
		os.system('cp '+i[0:-4]+'.xyz'+' ..')
		print (i)

