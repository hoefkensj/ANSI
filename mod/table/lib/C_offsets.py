#!/usr/bin/env python

def calc_lst_offset_coll(tbl):
	lst_lncoll=tbl['C']['lst_lncoll']
	lst_lncss=tbl['C']['lst_lncss']
	def addrel(add,subtot):
		tot=subtot+add
		return tot
	tot=0
	plncol=0
	lst_offset_coll=[]
	for lncoll,lncss in zip(lst_lncoll,lst_lncss[1:]):
		tot=addrel(lncoll+lncss,tot)
		lst_offset_coll+=[tot]
	tbl['C']['lst_offset_coll']= lst_offset_coll
	return tbl

def calc_mtx_offx(tbl):
	lst_offset_coll=tbl['C']['lst_offset_coll']
	mtx_data=tbl['D']
	mtx_offx=[[0,]for row  in  mtx_data]

	for r,row in enumerate(mtx_data):
		for c,col in enumerate(row):
			mtx_offx[r]+=[lst_offset_coll[c]]
	tbl['C']['mtx_offx']=	mtx_offx
	return tbl

def calc_mtx_offy(tbl):
	mtx_data=tbl['D']
	mtx_offy=[[]for row  in  mtx_data]
	for r,row in enumerate(mtx_data):
		for c,col in enumerate(row):
			mtx_offy[r]+=[r+1]
	tbl['C']['mtx_offy']=mtx_offy
	return tbl