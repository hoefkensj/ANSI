#!/usr/bin/env python
import sys

def ext(collection):
	t=0
	sys.stdout.write('\n');sys.stdout.flush()
	def extl(lst,t):
		for sublist in lst:
			sys.stdout.write(str('')*t)
			sys.stdout.write(str(repr(sublist)))
			if isinstance(sublist,list):
				if len(sublist)> 0 and isinstance(sublist[0],list):
					sys.stdout.write('\n')
					extl(sublist,t)
			elif isinstance(sublist,dict):
				sys.stdout.write('\n')
				extd(sublist,t)
			else:
				sys.stdout.flush()
			t-=1
		t-=1
	def extd(dct,t):
		for key in dct.keys():
			
			sys.stdout.write('\n')
			sys.stdout.write(str('\t')*t)
			sys.stdout.write(str(key).ljust(15,''))
			sys.stdout.write(str(':').ljust(4,''))
			
			if isinstance(dct[key],list):
				t+=1
				extl(dct[key],t)
			elif isinstance(dct[key],dict):
				t+=1
				extd(dct[key],t)
			else:
				sys.stdout.write(repr(dct[key]));sys.stdout.flush()
			t-=1
		t-=1
	# sys.stdout.write(str(collection));sys.stdout.flush()
	if isinstance(collection,list):extl(collection,t)
	elif isinstance(collection,dict):extd(collection,t)
	else:sys.stdout.write('\n');sys.stdout.flush()
