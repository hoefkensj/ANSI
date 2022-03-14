#!/usr/bin/env python

import sys
import ANSI.lib.ansi
import ANSI.lib.m
import ANSI.fnx.m
import ANSI.fnx.table.mod_H_hdrs
import ANSI.fnx.table.mod_D_data



table_meta={
		'fss': '\u2502',  # \u250B',
		'pdd': {'char'	:	'-',
						'min':[2,4,4]},
		'mrg': {'char'	: ' ',
						'lns':[0,2,0]},
		'hal': {'l': [1],'c':[2,3],'r':[]},
		'dal': {'l': [1],'c':[],'r':[2,3]}
		}

table_data=[
		[1 , 'd2', '123'],
		[2 , 'data\tp2', 'somedata', ],
		[3 , 'Green', 'data5299'],
		]
table_calc={}


table1 = {
	'T': [['title'], ['subtitle']],  # T TITLES
	'H': ['idx', 'header1', 'header2'],  # H HEADERS
	'M': table_meta,  # M META
	'D': table_data,
	'F': [['help'], ['footer']],
	'C': table_calc,
	}

# table1 = {
# 	'T': [['title'], ['subtitle']],  # T TITLES
# 	'H': ['idx', 'header1', 'header2'],  # H HEADERS
# 	'M': {
# 		'fss': '\u2502',  # \u250B',
# 		'pdd': {'char':'-','min':[2,4,4]},
# 		'mrg': ' ',
# 		'al': ['l', 'c', 'r']
# 		},  # M META
# 	'D': [
# 		[1 , 'd2', '123'],
# 		[5 , 'data\tp2', '\033[1msomedata\033[0m', ],
# 		[3 , '\033[32mGreen\033[0m', 'data5299'],
# 		],
# 	'F': [['help'], ['footer']]
# 	}



def mtx_pivot(mtx) -> list:
	piv=[]
	pivr=[[] for c in mtx[0]]
	for r,row in enumerate(mtx):
		for c,col in enumerate(row):
			pivr[c]+=[col]
	piv+=pivr
	return piv

def calc_lst_mrg(tbl) -> list:
	mrg=tbl['M']['mrg']['char']
	nheaders=len(tbl['D'][0])
	lst_mrg=[['', mrg],*[[mrg,mrg] for _ in range(nheaders)][:-2],[mrg,'']]
	tbl['C']['lst_mrg']=lst_mrg
	return tbl

def calc_lst_lnmrg(tbl) -> list:
	import ANSI.lib.lib_tty
	ttyln=ANSI.lib.lib_tty.tty_len
	lst_mrg=tbl['C']['lst_mrg']
	lst_lnmrg=[ttyln(lst_mrg[m][1])+ttyln(lst_mrg[m+1][0]) for m,_ in enumerate(lst_mrg[:-1])]
	tbl['C']['lst_lnmrg']=lst_lnmrg
	return tbl

def calc_lst_pdd(tbl) -> list:
	pdd=tbl['M']['pdd']
	ncols=len(tbl['D'][0])
	char=pdd.get('char')
	if isinstance(pdd.get('min'), list):
		lst_pdd=[]
		min_pdd=pdd.get('min')
		for pd in min_pdd:
			lst_pdd+= [char*pd]
	else:
		min_pdd=char*pdd.get('min')
		lst_pdd=[min_pdd for i in range(ncols)]
	return lst_pdd

def calc_lst_lnpdd(tbl) -> list:
	import ANSI.lib.lib_tty
	lst_pdd=calc_lst_pdd(tbl)
	return [ANSI.lib.lib_tty.tty_len(pdd) for pdd in lst_pdd]

def calc_lst_fss(tbl) -> list:

	fs=tbl['M']['fss']
	nheaders=len(tbl['D'][0])
	lst_fss=[fs for _ in range(nheaders)][:-1]
	tbl['C']['lst_fss']=lst_fss
	return tbl

def calc_lst_css(tbl):
	lst_fss=tbl['C']['lst_fss']
	lst_mrg=tbl['C']['lst_mrg']
	lst_css=[f'{lst_mrg[i][1]}{lst_fss[i]}{lst_mrg[i+1][0]}' for i in range(len(lst_fss))]
	tbl['C']['lst_css']=lst_css
	return tbl

def calc_lst_lncss(tbl):
	import ANSI.lib.lib_tty
	lst_css=tbl['C']['lst_css']
	lst_lncss=[ANSI.lib.lib_tty.tty_len(css) for css in lst_css]
	tbl['C']['lst_lncss']=lst_lncss
	return tbl

def calc_lst_maxdataw(tbl) -> list:  # calculate the minimum width of collumn for all data in col to fit .
	
	mtx_dataw=calc_mtx_dataw(tbl['D'])
	piv_dataw=mtx_pivot(mtx_dataw)
	return [max(col) for col in piv_dataw]

def calc_lst_lncoll(tbl) -> list:
	lst_lnpdd=calc_lst_lnpdd(tbl)
	lst_maxdataw=calc_lst_maxdataw(tbl)
	tbl['C']['lst_lncoll']=[(lndata + lnpdd) for lndata, lnpdd in zip(lst_maxdataw, lst_lnpdd)]
	return tbl

def calc_lst_offset_coll(tbl):
	lst_lncoll=tbl['C']['lst_lncoll']
	lst_lncss=tbl['C']['lst_lncss']
	def addrel(add,rel=[],offset=[0,]):
		rel+=[(sum(rel)+int(add))]
		offset+=[sum(rel)]
		return offset
	for lncoll in lst_lncoll:
		lst_offset_coll=addrel(lncoll+lst_lncss[0])
	tbl['C']['lst_offset_coll']= lst_offset_coll[:-1]
	return tbl

def calc_mtx_offx(tbl):
	lst_offset_coll=tbl['C']['lst_offset_coll']
	mtx_data=tbl['D']
	mtx_offx=[[]for row  in  mtx_data]
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

def calc_mtx_dataw(mtx_data):
	from ANSI.lib.lib_tty import tty_len
	
	dataw=[]
	for r,row in enumerate(mtx_data):
		roww=[]
		for cell in row:
			roww+=[tty_len(cell)]
		dataw+=[roww]
	return dataw

def calc_mtx_idxy(tbl):
	mtx_data=tbl['D']
	mtx_idxy=[[[] for col in row] for row in mtx_data]
	for r,row in enumerate(mtx_data):
		for c,col in enumerate(row):
			mtx_idxy[r][c]=(r+1,c+1)
	tbl['C']['mtx_idxy']=mtx_idxy
	return tbl

def tbl_calc(tbl):

	# ncols				=	len(tbl['D'][0])
	# mtx_dataw		=	calc_mtx_dataw(tbl['D'])
	# piv_dataw		=	mtx_pivot(mtx_dataw)
	# ln_pdd			=	ANSI.lib.lib_tty.tty_len(tbl['M']['pdd']['char'])
	# headers			=	tbl['H']
	# pdd					=	tbl['M']['pdd']
	tbl					=calc_mtx_idxy(tbl)
	tbl					=calc_lst_mrg(tbl)
	tbl					=calc_lst_fss(tbl)
	tbl					=calc_lst_lnmrg(tbl)
	tbl					=calc_lst_css(tbl)
	tbl					=calc_lst_lncss(tbl)
	tbl					=calc_lst_lncoll(tbl)
	tbl					=calc_lst_offset_coll(tbl)
	
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_data(tbl)
	tbl					=calc_mtx_offx(tbl)
	tbl					=calc_mtx_offy(tbl)

	tbl					= ANSI.fnx.table.mod_H_hdrs.calc_lst_H_hdrs(tbl)
	tbl					= ANSI.fnx.table.mod_H_hdrs.calc_lst_H_hdrs_yxH(tbl)
	tbl					= ANSI.fnx.table.mod_H_hdrs.calc_lst_H_cfss_yxH(tbl)
	
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_data_yxH(tbl)
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_cfss_yxH(tbl)
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_cfss(tbl)
	tbl					= ANSI.fnx.table.mod_H_hdrs.sel_lst_H_jsthdrs(tbl)
	return tbl


def tty_printtable(table):

	for h,(H_cfss_xyH,css) in enumerate(zip(table['C']['lst_H_cfss_yxH'],table['C']['lst_css'])):
		ANSI.fnx.m.stdout_mwrite(txt=[H_cfss_xyH,css],style=['red','uline']);sys.stdout.flush()
	for h,(headxy,head) in enumerate(zip(table['C']['lst_H_hdrs_yxH'],table['C']['lst_H_jsthdrs'])):
		ANSI.fnx.m.stdout_mwrite(txt=[headxy,head],style=['uline']);sys.stdout.flush()
	for r,row in enumerate(zip(table['C']['mtx_D_cfss_yxH'],table['C']['mtx_D_cfss'])):
		for c,(D_cfss_xyH,D_cfss) in enumerate(zip(*row)):
			ANSI.fnx.m.stdout_mwrite(txt=[D_cfss_xyH,D_cfss],style=['green']);sys.stdout.flush()
		sys.stdout.flush()
	for datax,row in zip(table['C']['mtx_D_data_yxH'],table['C']['mtx_D_data']):
		for dataxy,col in zip(datax,row):
			ANSI.fnx.m.stdout_mwrite(txt=[dataxy,col],style=[]);sys.stdout.flush()
		sys.stdout.write('\n')
	sys.stdout.write('\n')
	sys.stdout.flush()
	

def ext(collection):
	t=0
	sys.stdout.write('\n');sys.stdout.flush()
	def extl(lst,t):
		for sublist in lst:
			sys.stdout.write(str('\t')*t)
			sys.stdout.write(str(repr(sublist)))
			if isinstance(sublist,list):
				if isinstance(sublist[0],list):
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
			sys.stdout.write(str(key).ljust(15,'.'))
			sys.stdout.write(str(':').ljust(4,'.'))
			
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

table	= tbl_calc(table1)
# ext(table)
tty_printtable(table)

