#!/usr/bin/python
import sys, string, os, glob, re
import subprocess
from math import *
from multiprocessing import Pool
import multiprocessing
import random

path = os.path.dirname(sys.argv[0])
path = path+'/' 

def IsFloat(s):
	try: 
		float(s)
		return True
	except ValueError:
		return False


def parallel_chunk(j):
	dup = []
	for i in range(len(j)):
		if j[i] not in dup:
			for m in range(i+1,len(j),1):
				if j[m] not in dup:
					out = subprocess.check_output("python3 "+path+"calculate_rmsd.py "+j[i][0]+' '+j[m][0]+' -e --use-reflections-keep-stereo --reorder --reorder-method inertia-hungarian', shell=True)
					#out = out.decode(encoding)
					#out = re.findall("\d+\.\d+", out)
					out = float(out)
					if out < thld:
						dup.append(j[m])
					#print (j[i][0], j[m][0], out)	
	return dup

def parallel_chunk_min(j):
	dup = []
	min_rmsd = []
	for i in range(len(j)):
		if j[i] not in dup:
			data = []
			for m in range(i+1,len(j),1):
				if j[m] not in dup:
					out = subprocess.check_output("python3 "+path+"calculate_rmsd.py "+j[i][0]+' '+j[m][0]+' -e --use-reflections-keep-stereo --reorder --reorder-method inertia-hungarian', shell=True)
					#out = out.decode(encoding)
					#out = re.findall("\d+\.\d+", out)
					out = float(out)
					if out < thld:
						dup.append(j[m])
					else:
						if (len(data)==0):
							data.append([j[i][0],j[m][0],out])
						else:
							if data[0][2] > out:
								data=[]
								data.append([j[i][0],j[m][0],out])
					#print (j[i][0], j[m][0], out)	
			min_rmsd.append(data)
	return min_rmsd


if __name__ == '__main__':
	filelist = glob.glob('*.xyz')
	#filelist = glob.glob('*B97-3c.out')
	
	filelist.sort()
	outputs=[]
	
	for i in filelist:
	#       print (i)
		f = open(i, 'r')
		E = 'NaN'
		s = f.readline()
		s = f.readline()
		d = str.split(s)
		if len(d) == 1 and IsFloat(d[0]) == True:
			E = float(d[0])
		else:
			E = 'NaN'
		if E !='NaN':
			outputs.append([i,E])
		else:
			print ("Warning: E= ",E, " in ", i)
	
	outputs.sort(key=lambda x: x[1])
	
	for j in outputs:
		print (j[0]+' : '+str(j[1]))
	
	n = int(sys.argv[1])
	thld = float(sys.argv[2])
	iter1 = int(sys.argv[3])
	perm = int(sys.argv[4])
	pm=0
	encoding='utf-8'
	dup_all = []

	for it in range(iter1):
		print("iteration: ",it, "permutation: ",pm)
		a = len(dup_all)
		# devide initial list into n chuncks 
		chunks = []
		for i in range(0, len(outputs), n):
			chunks.append(outputs[i:i + n])
		#print (chunks)
		cpu_count = multiprocessing.cpu_count()
		with Pool(cpu_count) as pool:
#			dup = []
			dup = pool.map(parallel_chunk,chunks)
			#print (dup, len(dup))
			for mm in dup:
				if len(mm) !=0:
					for i in mm:
						dup_all.append(i)
	
		print ("LEN: ", len(dup_all))
		if len(dup_all) == a and pm >= perm:
			break 
		elif len(dup_all) == a and pm < perm:
			#n=int(n+n*(0.1)*pm)
			random.shuffle(outputs)
			pm=pm+1
		else:
			for j in dup_all:
				if j in outputs:
					outputs.remove(j)

	outputs.sort(key=lambda x: x[1])
	print('UNI:  '+str(len(outputs)))
	dup_all.sort(key=lambda x: x[1])
	f = open('unique.txt', 'w')
	for j in outputs:
		#print (j[0]+' : '+str(j[1]))
		f.write(j[0]+' : '+str(j[1])+'\n')
	f.close()
	f = open('unique_out.txt', 'w')
	for j in outputs:
		#print (j[0]+' : '+str(j[1]))
		f.write(j[0][0:-4]+'.out'+' : '+str(j[1])+'\n')
	f.close()
	#print ("---\n")
	f = open('dup.txt', 'w')
	for j in dup_all:
		#print (j[0]+' : '+str(j[1]))
		f.write(j[0]+' : '+str(j[1])+'\n')
	f.close()	
	print("Minimum RMSD. \n")
	a = len(dup_all)
	# devide initial list into n chuncks 
	chunks = []
	for i in range(0, len(outputs), n):
		chunks.append(outputs[i:i + n])
	#print (chunks)
	cpu_count = multiprocessing.cpu_count()
	min_all = []
	with Pool(cpu_count) as pool:
		min_chunk = []
		min_chunk = pool.map(parallel_chunk_min,chunks)
		#print (dup, len(dup))
		for mm in min_chunk:
			if len(min_chunk) !=0:
				for i in mm:
					min_all.append(i)
	f = open('rmsd_min.txt', 'w')
	for i in range(len(min_all)):
		if len(min_all[i]) !=0:
			if min_all[i][0][2] < 0.5:
				f.write(min_all[i][0][0]+' : '+min_all[i][0][1]+' : '+str(min_all[i][0][2])+'\n')
			#print (min_all[i][0])
	f.close()
	'''
	for j in outputs:
		print (j[0]+' : '+str(j[1]))
	print ("---\n", len(outputs))
	for j in dup_all:
		print (j[0]+' : '+str(j[1]))
	'''
