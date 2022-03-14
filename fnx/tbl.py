#!/usr/bin/env python
import pprint
import sys

pp=pprint.pprint
headers=['COLL_A_','COLL_B_']
data=[	['CELL_A1','CELL_B1','CELL_C1'],
				['CELL_A2','CELL_B2','CELL_C2'],
				['CELL_A3','CELL_B3','CELL_C3'],
			]

def pivot(mtx) -> list:
		tmp=[[mtx[c[0]][r[0]] for c in enumerate(r)] for r in enumerate(mtx)]
		print(tmp)
		return tmp
		
def table(data):
	def idord(mtx):
		otbl	=	[]
		# otbl+= [['0']+[c+1 for c,coll in enumerate(mtx[0])]]
		otbl+= {[1+i]:row for i,row in enumerate(mtx)}
		return otbl
	
	def id(matrix):
		id={r:[row] for r,row in enumerate(matrix)}
		# for r,row in enumerate(matrix):
		# 	idxx[r]=[[] for col in row]
		# 	for c,col in enumerate(row):
		# 		idxx[r][c]=f'{c}{r+1}'
		return id

	rows=id(data)
	cols=id(pivot(data))

	# mtx_data_colls=
	
	tbl=[rows,cols]
	return tbl




tbl=table(data)


m=[[] for mtx in tbl]

for m,mtx in enumerate(tbl):
	for r,row in enumerate(mtx):
		print([tbl[i][r]for i,_ in enumerate(tbl)])
		pass




def xy(XY):
	return	[[int(XY[1])],[int(ord(XY[0]))]]

def idc_x(mtx):
		pass
table={}
