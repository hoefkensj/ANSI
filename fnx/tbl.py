#!/usr/bin/env python
import pprint
import sys

pp=pprint.pprint
headers=['COLL_A_','COLL_B_']
data=[	['CELL_A1','CELL_B1','CELL_C1'],
				['CELL_A2','CELL_B2','CELL_C2'],
				['CELL_A3','CELL_B3','CELL_C3'],
			]
pp(data)
def table(data):
	def idord(mtx):
		otbl	=	[]
		otbl+= [['O']+[chr(65+c) for c,coll in enumerate(mtx[0])]]
		otbl+= [[1+i]+row for i,row in enumerate(mtx)]
		return otbl
	
	def idxy(matrix):
		idxx=[[]for row in matrix]
		for r,row in enumerate(matrix):
			idxx[r]=[[] for col in row]
			for c,col in enumerate(row):
				idxx[r][c]=f'{chr(65+c)}{r+1}'
		return idxx

	ords=idxy(data)
	mtx_ords=idord(ords)
	mtx_data=idord(data)
	tbl=[mtx_ords,mtx_data]
	return tbl




tbl=table(data)
verz=[[] for row in tbl[0] ]

m=[[] for mtx in tbl]

for r,row in enumerate(tbl[0]):
	line=f'{tbl[0][r]}\t\t{tbl[1][r]}'
	sys.stdout.write(line)
	sys.stdout.write('\n')




def xy(XY):
	return	[[int(XY[1])],[int(ord(XY[0]))]]

def idc_x(mtx):
		pass





table={}

# table['IDXX']	=	idxy(data)
# table['DATA'] = data


# print(repr(table))
# print(ord('A'))
