#!/usr/bin/env python

import sys
import ANSI.lib.ansi
import ANSI.lib.m
import ANSI.fnx.m
import ANSI.fnx.table.mod_H_hdrs
import ANSI.fnx.table.mod_D_data
import ANSI.fnx.table.mod_M_cfss
import ANSI.fnx.table.mod_M_cpdd
import ANSI.fnx.table.mod_C_offsets

print('THERE ARE STILL SOME PROBLEMS ,... ONE OF THEM BEING WHEN THE [ENTER] LAUNCH IS BADLE DEBOUNCED THE WHOLE APP BREAKS')
table_meta={
		'fss': {
						'char': '\u250B',  # B',\u2502
						'show':	[0,1,0],
						},
		'pdd': {
						'char'	:	' ',
						'min':	[0,0,0]
						},
		'mrg': {
						'char'	: ' ',
						'lns':	[0,2,0]
						},
		'hal': {'l': [1],'c':[2,3],'r':[]},
		'dal': {'l': [1],'c':[],'r':[2,3]}
		}

table_data=[
		[1 , 'cell', '@#$%'],
		[2 , '\x1b[32mcolors', '\u255FUnicode\u255F' ],
		['\033[7m   3' , '\033[7m     SELECTIONS', '\033[7mCELL|ROW BASED'],
		[4 , 'Green', ''],
		[5 , 'ANSI', 'TABLE'],
		['\033[31m100%','\033[31mOOP FREE CODE','\033[31mTHE_UNLICENCE!']
			]
table_calc={}


table1 = {
	'T': [['title'], ['subtitle']],  # T TITLES
	'H': ['2k22', 'HOEFKENSJ', '@GitHub'],  # H HEADERS
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

def tbl_index():
	def calc_mtx_idxy(tbl):
		lst_hdrs=tbl['H']
		mtx_data=tbl['D']
		mtx_content=[lst_hdrs,*mtx_data]
		mtx_idxy=[[[] for col in row] for row in mtx_content]
		for r,row in enumerate(mtx_content):
			for c,col in enumerate(row):
				mtx_idxy[r][c]=(r,c+1)
		tbl['C']['mtx_idxy']=mtx_idxy
		return tbl
	def calc_mtx_cloc(tbl):
		for h,H_hdrs_yxH in enumerate(tbl['C']['lst_H_hdrs_yxH']):
			H_hdrs_yxH=''
		
		
	# tbl					=calc_mtx_idxy(tbl)
def tbl_create(tbl):

		

	tbl					= ANSI.fnx.table.mod_M_cfss.calc_lst_mrg(tbl)
	tbl					= ANSI.fnx.table.mod_M_cfss.calc_lst_fss(tbl)
	tbl					= ANSI.fnx.table.mod_M_cfss.calc_lst_lnmrg(tbl)
	tbl					= ANSI.fnx.table.mod_M_cfss.calc_lst_css(tbl)
	tbl					= ANSI.fnx.table.mod_M_cfss.calc_lst_lncss(tbl)
	tbl					= ANSI.fnx.table.mod_M_cpdd.calc_lst_lncoll(tbl)
	tbl					= ANSI.fnx.table.mod_C_offsets.calc_lst_offset_coll(tbl)
	
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_data(tbl)
	tbl					= ANSI.fnx.table.mod_C_offsets.calc_mtx_offx(tbl)
	tbl					= ANSI.fnx.table.mod_C_offsets.calc_mtx_offy(tbl)

	tbl					= ANSI.fnx.table.mod_H_hdrs.calc_lst_H_hdrs(tbl)
	tbl					= ANSI.fnx.table.mod_H_hdrs.calc_lst_H_hdrs_yxH(tbl)
	tbl					= ANSI.fnx.table.mod_H_hdrs.calc_lst_H_cfss_yxH(tbl)
	
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_data_yxH(tbl)
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_cfss_yxH(tbl)
	tbl					= ANSI.fnx.table.mod_D_data.calc_mtx_D_cfss(tbl)
	tbl					= ANSI.fnx.table.mod_H_hdrs.sel_lst_H_jsthdrs(tbl)
	tbl					= idx_org(tbl)
	return tbl

def tbl_C_repl(tbl,txt=None,loc=0.0,):
	E=ANSI.lib.ansi.cursor['nextline']
	O=tbl['O']
	loc=O.get(loc)
	org=O.get(0.0)
	mxy=max([key for key in O.keys()])+2

	ANSI.fnx.m.stdout_mwrite(txt=[*loc,txt['txt']],style=txt['style']);sys.stdout.flush()
	ANSI.fnx.m.stdout_mwrite(txt=[*org,E(mxy)],style=[]);sys.stdout.flush()

def idx_org(tbl):
	tbl['O']={}
	org=None
	for H_hdrs_yxH in tbl['C']['lst_H_hdrs_yxH']:
		org=f"{H_hdrs_yxH.split(';')[0]};{int(H_hdrs_yxH.split(';')[1][:-1])-1}H" if not org else org
	tbl['O']={
		0.0:org,}
	for r,locs in enumerate(tbl['C']['mtx_D_data_yxH'],start=1):
		for c,loc in enumerate(locs,start=1):
			tbl['O'][float(f'{r}.{c}')]=[loc]
	return  tbl

def tty_printtable(table):

	H=ANSI.lib.ansi.cursor['pos']
	F=ANSI.lib.ansi.cursor['prevline']
	E=ANSI.lib.ansi.cursor['nextline']
	B=ANSI.lib.ansi.cursor['down']
	K=ANSI.lib.ansi.markup['clear_line']
	
	surfy=len(table['D'])

	def write_H_hdrs(tbl):
		def stdout_headers():
			ANSI.fnx.m.stdout_mwrite(txt=K(2),style=[])
			ANSI.fnx.m.stdout_mwrite(txt=F(1),style=[])
			
			for h,(H_hdrs_yxH,H_jsthdrs) in enumerate(zip(table['C']['lst_H_hdrs_yxH'],table['C']['lst_H_jsthdrs'])):
				ANSI.fnx.m.stdout_mwrite(txt=[H_hdrs_yxH,H_jsthdrs],style=['uline','blue']);sys.stdout.flush()
			for h,(H_cfss_xyH,css) in enumerate(zip(table['C']['lst_H_cfss_yxH'],table['C']['lst_css'])):
	 			ANSI.fnx.m.stdout_mwrite(txt=[H_cfss_xyH,css],style=['uline','blue']);sys.stdout.flush()
			sys.stdout.write('\n')
			sys.stdout.flush()
		return stdout_headers()
		
	def write_C_cfss(tbl):
		mtx_D_cfss_yxH=table['C']['mtx_D_cfss_yxH']
		mtx_D_cfss=table['C']['mtx_D_cfss']
		def stdout_cfss():
			ANSI.fnx.m.stdout_mwrite(txt=(f'\n{K(2)}'*surfy),style=[])
			ANSI.fnx.m.stdout_mwrite(txt=F(3),style=[])
			for r,(D_cfss_yH,D_cfssy) in enumerate(zip(mtx_D_cfss_yxH,mtx_D_cfss)):
				for c,(D_cfss_xyH,D_cfssc) in enumerate(zip(D_cfss_yH,D_cfssy)):
					ANSI.fnx.m.stdout_mwrite(txt=[D_cfss_xyH,D_cfssc],style=['blue']);sys.stdout.flush()
			sys.stdout.write('\n')
			sys.stdout.flush()
		return stdout_cfss()
	
	def write_D_data(tbl):
		def stdout_data():
			for datax,row in zip(table['C']['mtx_D_data_yxH'],table['C']['mtx_D_data']['r']):
				for dataxy,col in zip(datax,row):
					ANSI.fnx.m.stdout_mwrite(txt=[dataxy,col],style=[]);sys.stdout.flush()
				sys.stdout.write('\n')
		return stdout_data()
	#
	def write_table(table):
		surfy=len(table['D'])
		[print(K(2)) for row in range(surfy+1)]
		ANSI.fnx.m.stdout_mwrite(txt=[F(surfy+1)],style=[])
		# ANSI.fnx.m.stdout_mwrite(txt='\t\t\t\tt',style=[])
		table	= tbl_create(table)
		def stdout_table():
			write_H_hdrs(table)
			write_C_cfss(table)
			write_D_data(table)
		return [table,stdout_table]
		
	# for r,row in enumerate(zip(table['C']['mtx_D_cfss_yxH'],table['C']['mtx_D_cfss'])):
	# 	for c,(D_cfss_xyH,D_cfss) in enumerate(zip(*row)):
	# 		ANSI.fnx.m.stdout_mwrite(txt=[D_cfss_xyH,D_cfss],style=['green']);sys.stdout.flush()
	#
	# org=ANSI.lib.lib_tty.pos_cursor()['y']
	# crd=H(f"{ANSI.lib.lib_tty.pos_cursor()['y']};{ANSI.lib.lib_tty.pos_cursor()['x']}")	#
	# # [print(i) for i in range(18)]
	# # crd=H(f"{ANSI.lib.lib_tty.pos_cursor()['y']};{ANSI.lib.lib_tty.pos_cursor()['x']}")
	# # print(repr(table['C']['lst_H_cfss_yxH']),repr(table['C']['lst_css']))
	# print('crd:',repr(crd))
	return write_table(table)

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

# table	= tbl_calc(table1)
tbl_1=table1

tbl_1,write_table1=tty_printtable(tbl_1)
print('\n')

def respcol(val):
	color= 'red'
	if 300< val < 750 :
		color='yellow'
	if val > 750:
		color='green'
	return color



import time
def  str_mrepl(txt,style):
	mstring={
		'txt':f'{txt}',
		'style': style}
	return mstring
	
	
def counter():
	tbl_C_repl(tbl_1,txt=str_mrepl(' LIVE PROGRESS:',['red','sblink']),loc=4.2,)
	for count in range(1001):
		tbl_C_repl(tbl_1,txt=str_mrepl(f'          {str(count).zfill(4)}',[respcol(count)]),loc=4.3,)
		time.sleep(0.005)
	tbl_C_repl(tbl_1,txt=str_mrepl('         DONE!!',['green','bold']),loc=4.2,)

write_table1()
counter()

E=ANSI.lib.ansi.cursor['nextline']
org=tbl_1['O'].get(0.0)
mxy=max([key for key in tbl_1['O'].keys()])+2
# ANSI.fnx.m.stdout_mwrite(txt=org,style=[]);sys.stdout.flush()
ANSI.fnx.m.stdout_mwrite(txt=[E(int(mxy))],style=[]);sys.stdout.flush()
# print('\n'*mxy)
# ext(tbl_1)