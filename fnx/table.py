#!/usr/bin/env python

import shutil
import time
import sys
import ANSI.lib.ansi



table1 = {
	'T': [['title'], ['subtitle']],  # T TITLES
	'H': ['idx', 'header1', 'header2'],  # H HEADERS
	'M': {
		'tb': {False},
		'cb': {True},
		'fss': '\u2502',  # \u250B',
		'pdd': {'char':' ','min':[0,4,4]},
		'mrg': ' ',
		'al': ['l', 'c', 'r']
		},  # M META
	'D': [
		[1 , 'd2', '123'],
		[5 , 'data\tp2', '\033[1msomedata\033[0m', ],
		[3 , '\033[32mGreen\033[0m', 'data5299'],
		],
	'F': [['help'], ['footer']]
	}
# table1 = {
# 	'T': [['title'], ['subtitle']],  # T TITLES
# 	'H': ['idx', 'header1', 'header2'],  # H HEADERS
# 	'M': {# M META
# 		'fss': '\u250B',  # \u250B',
# 		'pdd': {'char':' ','min':4},
# 		'mrg': ' ',
# 		},
# 	'D': [
# 		[1, 'd2', '123'],
# 		[5, 'data\tp2', '\033[1msomedata ', ],
# 		[3, '\033[32mGreen\033[0m', 'data5299'],
# 		],
# 	}
#
	
# table2 = {
# 	'T': [['{title}'], ['{subtitle}']],  # T TITLES
# 	'H': ['{h-idx}', 'h-1', 'h-n', 'h-sub'],  # H HEADERS
# 	'M': {  # Meta
# 		'B'    : {  # Border
# 			'Tbl'  : {0, 0, 0, 0},
# 			'Col'  : {0, 1, 0, 0},  # LCRB # |Lc|c_b_c|c|cR|
# 			'style': {1, 1},
# 			'v_sbl': '\u250B',
# 			'h_sbl': '',
# 			'Xoff' : 0,
# 			'Yoff' : 0,
# 			},
# 		'LC_pd': '\t',
# 		'RC_pd': '\t',
# 		'mrgn' : ' ',
# 		'al'   : 'left'
# 		},  # M META
# 	'D': [  # Data
# 		[1, '{D:0,1}}', 'da1ta2'],
# 		[2, '      ', '\033[1msomedata ', ],
# 		[f'\033[32m{3}', 'selected row', 'data5299\033[0m'],
# 		],
# 	'F': [['help'], ['footer']]
# 	}

def std_cursorloc():
	import termios
	import tty
	import re
	
	buf = ""
	stdin = sys.stdin.fileno()
	tattr = termios.tcgetattr(stdin)
	try:
		tty.setcbreak(stdin, termios.TCSANOW)
		sys.stdout.write("\x1b[6n")
		sys.stdout.flush()
		while True:
			buf += sys.stdin.read(1)
			if buf[-1] == "R":
				break
	finally:
		termios.tcsetattr(stdin, termios.TCSANOW, tattr)
	# reading the actual values, but what if a keystroke appears while reading
	# from stdin? As dirty work around, getpos() returns if this fails: None
	try:
		matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
		groups = matches.groups()
	except AttributeError:
		return None
	return (int(groups[0]), int(groups[1]))
def terminal_width(**k):
	stored = k.get('stored')
	width = (shutil.get_terminal_size()[0] - 2)
	stored += [width]
	diff = (-1 * (stored[-2] - stored[-1]))
	return stored
def tty_conv(s,t=4):
	re = presets_re()
	wtab = '\u0020' * t
	s = re.repl_ESCt(wtab, str(s))
	return s
	
def tty_len(s):
	re = presets_re()
	s=tty_conv(s)
	s = re.repl_ANSIm('', str(s))
	return len(s)

def tty_str(s):
	re = presets_re()
	s=tty_conv(s)
	s = re.repl_ANSIm('', str(s))
	return s
def tty_mstr(s):
	s=tty_conv(s)
	return s
def presets_re():
	import types
	import re
	
	preset = types.SimpleNamespace()
	preset.repl_ANSIm = re.compile(r'\033\[[;\d]*m', re.VERBOSE).sub
	preset.repl_ESCt = re.compile(r'\t', re.VERBOSE).sub
	preset.repl_ESCs = re.compile(r' ', re.VERBOSE).sub
	return preset

def mtx_pivot(mtx) -> list:
	return [[mtx[c[0]][r[0]] for c in enumerate(r[1])] for r in enumerate(mtx)]

def dcon_table(table):
	def allign():
		if len(al) != len(tbl.headers):
			if len(al) == 1:
				al = [al[0] for header in tbl.headers]
	import types
	
	tbl = types.SimpleNamespace()
	tbl.titles = table.get('T')
	tbl.headers = table.get('H')
	tbl.footers = table.get('F')
	tbl.data = table.get('D')
	tbl.meta = types.SimpleNamespace()
	tbl.meta.fss = table.get('M').get('fss')
	tbl.meta.pdd = table.get('M').get('pdd')
	tbl.meta.al = table.get('M').get('al')
	tbl.meta.mrg = table.get('M').get('mrg')
	return tbl

def calc_lst_mrg(mrg, nheaders) -> list:
	return	[['', mrg],*[[mrg,mrg] for _ in range(nheaders)][:-2],[mrg,'']]

def calc_lst_lnmrg(lst_mrg) -> list:
	return [(tty_len(lst_mrg[m][1])+tty_len(lst_mrg[m+1][0])) for m in range(len(lst_mrg)-1)]

def calc_lst_pdd(pdd, ncols) -> list:
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

def calc_lst_lnpdd(lst_pdd) -> list:
	return [tty_len(pdd) for pdd in lst_pdd]

def calc_lst_fss(fs,nheaders) -> list:
		return [fs for _ in range(nheaders)][:-1]

def calc_lst_css(lst_fss,lst_mrg):
	return [f'{lst_mrg[i][1]}{lst_fss[i]}{lst_mrg[i+1][0]}' for i in range(len(lst_fss))]

def calc_lst_lncss(lst_css):
	return [tty_len(css) for css in lst_css]

def calc_lst_maxdataw(piv_dataw) -> list:  # calculate the minimum width of collumn for all data in col to fit .
	return [max(col) for col in piv_dataw]

def calc_lst_lncoll(lst_maxdataw,lst_lnpdd) -> list:
	return [(lndata + lnpdd) for lndata, lnpdd in zip(lst_maxdataw, lst_lnpdd)]

def calc_lst_offset_coll(lst_lncoll,lst_lncss):
	def addrel(add,rel=[],offset=[0,]):
		rel+=[add]
		offset+=[sum(rel)]
		return offset
	for lncoll in lst_lncoll:
		lst_offset_coll=addrel(lncoll+lst_lncss[0])
	return lst_offset_coll[:-1]

def calc_lst_heads(tbl_heads,lst_lncoll,pdd):
	mtx_datal=[[] for col in tbl_heads]
	mtx_datar=[[] for col in tbl_heads]
	mtx_datac=[[] for col in tbl_heads]
	for c,cell in enumerate(tbl_heads):
		mtx_datal[c]=str('{}'.format(tty_str(str(cell))).ljust(lst_lncoll[c],pdd.get('char'))).replace(tty_str(str(cell)),tty_mstr(str(cell)))
		mtx_datar[c]=str('{}'.format(tty_str(str(cell))).rjust(lst_lncoll[c],pdd.get('char'))).replace(tty_str(str(cell)),tty_mstr(str(cell)))
		mtx_datac[c]=str('{}'.format(tty_str(str(cell))).center(lst_lncoll[c],pdd.get('char'))).replace(tty_str(str(cell)),tty_mstr(str(cell)))
	return {'l':mtx_datal,'r':mtx_datar,'c':mtx_datac}

def lst_ltorg(fs,cellw) -> list:
	lst_leftbounds = [0, ]
	lst_cellbwidths = [0, ] + [i + tty_len(s=fs) for i in cellw]
	lst_leftbounds += [lst_cellbwidths[i] + cell + tty_len(s=fs) for i, cell in enumerate(cellw[:-1])]
	return lst_leftbounds

def calc_mtx_offx(mtx_data,lst_offset_coll):
	mtx_offx=[[]for row  in  mtx_data]
	for r,row in enumerate(mtx_data):
		for c,col in enumerate(row):
			mtx_offx[r]+=[lst_offset_coll[c]]
	return mtx_offx

def calc_mtx_offy(mtx_data):
	mtx_offy=[[]for row  in  mtx_data]
	for r,row in enumerate(mtx_data):
		for c,col in enumerate(row):
			mtx_offy[r]+=[r]
	return mtx_offy

def calc_mtx_dataw(mtx_data):
	mtx_dataw=[[] for row in mtx_data]
	for r,row in enumerate(mtx_data):
		for cell in row:
			mtx_dataw[r]+= [tty_len(cell)]
	return mtx_dataw

def calc_mtx_idxy(mtx_data):
	mtx_idxy=[[[] for col in row] for row in mtx_data]
	for r,row in enumerate(mtx_data):
		for c,col in enumerate(row):
			mtx_idxy[r][c]=(r+1,c+1)
	return mtx_idxy

def calc_mtx_data(tbl_data,lst_lncoll,pdd):
	char=pdd.get('char')
	mtx_datal=[[[] for col in row] for row in tbl_data]
	mtx_datar=[[[] for col in row] for row in tbl_data]
	mtx_datac=[[[] for col in row] for row in tbl_data]
	
	for r,row in enumerate(tbl_data):
		for c,cell in enumerate(row):
			str_tty					=	tty_str(str(cell))
			str_mtty				=	tty_mstr(str(cell))
			str_tty_l 			= str_tty.ljust(lst_lncoll[c],char)
			str_tty_c 			= str_tty.center(lst_lncoll[c],char)
			str_tty_r 			= str_tty.rjust(lst_lncoll[c],char)
			str_mtty_l 			= str_tty_l.replace(str_tty,str_mtty)
			str_mtty_c 			= str_tty_c.replace(str_tty,str_mtty)
			str_mtty_r 			= str_tty_r.replace(str_tty,str_mtty)
			mtx_datal[r][c]	=	str_mtty_l
			mtx_datac[r][c]	=	str_mtty_c
			mtx_datar[r][c]	=	str_mtty_r
	mtx_data= {
		'l'	:	mtx_datal,
		'r'	:	mtx_datar,
		'c'	:	mtx_datac,
		}
	return mtx_data

def calc_mtx_ansih(mtx_offx,mtx_offy):
	import ANSI.lib.ansi
	ANSI=ANSI.lib.ansi.fn()
	coord=std_cursorloc()
	H=ANSI.cursor.position
	mtx_ansih=[[[] for col in row] for row in mtx_offx]
	for r,(rowx,rowy) in enumerate(zip(mtx_offx,mtx_offy)):
		for c,(colx,coly) in enumerate(zip(rowx,rowy)):
			mtx_ansih[r][c]=H(';'.join([str(1+coly+coord[0]),str(-1+colx+coord[1])]))
	return mtx_ansih
	
def tbl_calc(table):
	tbl					= dcon_table(table)
	ncols				=	len(tbl.data[0])
	mtx_dataw		=	calc_mtx_dataw(tbl.data)
	piv_dataw		=	mtx_pivot(mtx_dataw)
	ln_pdd			=	tty_len(tbl.meta.pdd.get('char'))
	headers			=	tbl.headers
	pdd					=	tbl.meta.pdd
	
	lst_mrg			= calc_lst_mrg(tbl.meta.mrg, ncols)
	lst_lnmrg					=calc_lst_lnmrg(lst_mrg)
	lst_pdd						=calc_lst_pdd(pdd, ncols)
	lst_lnpdd					=calc_lst_lnpdd(lst_pdd)
	lst_fss						=calc_lst_fss(tbl.meta.fss,ncols)
	lst_css						=calc_lst_css(lst_fss,lst_mrg)
	lst_lncss					=calc_lst_lncss(lst_css)
	lst_maxdataw			=calc_lst_maxdataw(piv_dataw)
	lst_lncoll				=calc_lst_lncoll(lst_maxdataw,lst_lnpdd)
	lst_offset_coll		=calc_lst_offset_coll(lst_lncoll,lst_lncss)
	lst_heads					=calc_lst_heads(headers,lst_lncoll,tbl.meta.pdd)
	mtx_idxy					=calc_mtx_idxy(tbl.data)
	mtx_data					=calc_mtx_data(tbl.data,lst_lncoll,tbl.meta.pdd)
	mtx_offx					=calc_mtx_offx(tbl.data,lst_offset_coll)
	mtx_offy					=calc_mtx_offy(tbl.data)
	mtx_ansih					=calc_mtx_ansih(mtx_offx,mtx_offy)
	
	ccld={ #calculated
		'lst': {
							'mrg'					:	lst_mrg,
		        	'lnmrg'				:	lst_lnmrg,
		        	'pdd'					:	lst_pdd,
		        	'lnpdd'				:	lst_lnpdd,
		        	'fss'					:	lst_fss,
		        	'css'					:	lst_css,
		        	'lncss'				:	lst_lncss,
		        	'maxdataw'		:	lst_maxdataw,
		        	'lncoll'			:	lst_lncoll,
		        	'offset_coll'	:	lst_offset_coll,
		        	'heads'				:	lst_heads,
						},
		'mtx':	{
							'idxy'				:	mtx_idxy,
							'data'				: mtx_data,
				      'dataw' 			: mtx_dataw,
			    	  'piv_dataw'   :	piv_dataw,
			    	  'offx'				: mtx_offx,
							'offy'				: mtx_offy,
							'ansih'				: mtx_ansih,
						},
		}
	return ccld

calc = tbl_calc(table1)
css=['',*calc['lst']['css']]

tbl_mtx=calc['mtx']
tbl_mtx_data=tbl_mtx['data']['l']

# for section in calc.keys():
# 	for key in calc[section].keys():
# 		if isinstance(calc[section][key],list):
# 			if isinstance(calc[section][key][0],list):
				# print(section+':'+key+':\t')
				# for item in calc[section][key]:
					# print('\t\t',item)
# 				pass
# # 			else:
# 				print(section+':'+key+':\t'+str(calc[section][key]))
# 		elif isinstance(calc[section][key],dict):
# dct= calc[section][key]
# 			print(section+':'+key+':\t')
# 			for key in dct.keys():
# 				if isinstance(dct[key],list):
# 					for item in dct[key]:
# 						print('\t\t',item)
# 				else:
# 					print('\t\t',key,':',dct[key])
# 		else:
# 			print(section+':'+key+':\t'+str(calc[section][key]))
#
import ANSI.fnx.m

for h,(head,fs) in enumerate(zip(calc['lst']['heads']['c'],css)):
	ANSI.fnx.m.stdout_mwrite(txt=fs,style=['d_uline'])
	sys.stdout.write(head)
	sys.stdout.flush()
sys.stdout.write('\n')
for posx,row in zip(tbl_mtx['ansih'],tbl_mtx_data):
	for posxy,col,fs in zip(posx,row,css):
		sys.stdout.write(posxy)
		sys.stdout.write(fs)
		sys.stdout.write(col)
		sys.stdout.flush()
	sys.stdout.write('\n')
	sys.stdout.flush()
	
# listprt2([calc.lst_stdw_ltorg])
# listprt2([calc.lst_stdw_fsorg])
#
#
# import time
#
# # row_next = tty_writesbl(s=M('10;10'))
#
# # tpl_org=std_cursorloc()
# # tbl_org=ANSI_H(f'{tpl_org[1]};{tpl_org[0]}')
# # tpl_org=std_cursorloc()
# dat_org = H('2;0')  # ANSI_H(f'{tpl_org[1]+2};{tpl_org[0]}')
# # def fn(fnx):
# # 	time.sleep(1)
# # 	sys.stdout.write(f'{fnx}1');sys.stdout.flush()
# # 	time.sleep(1)
# # 	sys.stdout.write(f'\033[10{fnx}');sys.stdout.flush()
# # 	time.sleep(1)
# # 	sys.stdout.write(f'{fnx}2');sys.stdout.flush()
# # 	time.sleep(1)
# #
# # import string
# # alfab=string.ascii_uppercase
# # print(alfab)
# # for f in alfab:
# # 	fn(f)
#
#
# # 	def tmp():
# # 		for r,row in enumerate(tbl_data):
# # 			for c,cell in enumerate(row):
# # 				sys.stdout.write(f'\033[{calc_leftbounds()[c]}G{cell}')
# # 			for b,border in enumerate(calc_borderorg()):
# # 				sys.stdout.write(f'\033[0m\033[{calc_borderorg()[b]}G{fs}')
# # 			sys.stdout.write('\n')
# #
# #
# #
# # # [print(row) for row in rows]
# # # print()
# # # print()
# #
# # upper = [chr(i) for i in range(65, 91)]
# # lower = [chr(i) for i in range(96, 123)]
# #
# #
# #
# # calc_dimensions(tbl=table1)
# #
# # calc_dimensions(tbl=table2)
# def lst_stdw_ltorg() -> list:
# 	return [tty_writesbl(s=G(lb)) for lb in lst_ltorg(**k)]
#
# def lst_stdw_fsorg() -> list:
# 	return [tty_writesbl(s=G(pd)) for pd in lst_fsorg(**k)]
# def mtx_dataw(mtx_data) -> list:
# 	return [[tty_len(s=cell) for cell in row] for row in mtx_data]
#
# def mtx_relorg(data) -> list:
# 	return [[[f'{F(r)}{G(lst_cellw(**k)[c])}'] for c, cell in enumerate(data[r])] for r, row in enumerate(data)]
#
#
# def mtx_tblsurface(fs, mg, pd, data):
# 	# cell= padd[:x]+data+padd[x:]
# 	# fs= mg+fs+mg
# 	cells_dmy = [str().ljust(mx, '#').ljust(mx + tty_len(pd), pd) for mx in lst_datamax(data)]
# 	len_fs = tty_len(s=f'{mg}{fs}{mg}')
#
# 	rowdummy = f'{mg}{fs}{mg}'.join(cells_dmy)
# 	print(('dummy', rowdummy) for line in data)
# def std_wr(s):
# 	sys.stdout.write(str(s))
# 	sys.stdout.flush()
#
#
# def tty_writesbl(s):
# 	def stdout_write():
# 		sys.stdout.write(s)
# 		sys.stdout.flush()
# 		return tty_len()
# 	return stdout_write
