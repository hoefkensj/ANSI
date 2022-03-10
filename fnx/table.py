#!/usr/bin/env python

import shutil
import time
import sys
import ANSI.lib.ansi


'''
A 	Cursor Up 	(n=1) 	Move cursor up by n
B 	Cursor Down 	(n=1) 	Move cursor down by n
C 	Cursor Forward 	(n=1) 	Move cursor forward by n
D 	Cursor Back 	(n=1) 	Move cursor back by n

E 	Cursor Next Line 	(n=1) 	Move cursor to the beginning of the line n lines down
F 	Cursor Previous Line 	(n=1) 	Move cursor to the beginning of the line n lines up
G 	Cursor Horizontal Absolute 	(n=1) 	Move cursor to the the column n within the current row
H 	Cursor Position 	(n=1, m=1) 	Move cursor to row n, column m, counting from the top left corner

J 	Erase in Display 	(n=0) 	Clear part of the screen. 0, 1, 2, and 3 have various specific functions
K 	Erase in Line 	(n=0) 	Clear part of the line. 0, 1, and 2 have various specific functions

S 	Scroll Up 	(n=1) 	Scroll window up by n lines
T 	Scroll Down 	(n=1) 	Scroll window down by n lines

s 	Save Cursor Position 	() 	Save current cursor position for use with u
u 	Restore Cursor Position 	() 	Set cursor back to position last saved by s
f 	… 	… 	(same as G)
'''
ANSI=ANSI.lib.ansi.fn()


table1 = {
	'T': [['title'], ['subtitle']],  # T TITLES
	'H': ['idx', 'header1', 'header2'],  # H HEADERS
	'M': {
		'tb': {False},
		'cb': {True},
		'fs': '|',  # \u250B',
		'pd': '-',
		'mg': '_',
		'al': ['l', 'c', 'r']
		},  # M META
	'D': [
		[1, 'd2', '123'],
		[5, 'data\tp2', '\033[1msomedata ', ],
		[3, '\033[32mGreen\033[0m', 'data5299'],
		],
	'F': [['help'], ['footer']]
	}
table2 = {
	'T': [['{title}'], ['{subtitle}']],  # T TITLES
	'H': ['{h-idx}', 'h-1', 'h-n', 'h-sub'],  # H HEADERS
	'M': {  # Meta
		'B'    : {  # Border
			'Tbl'  : {0, 0, 0, 0},
			'Col'  : {0, 1, 0, 0},  # LCRB # |Lc|c_b_c|c|cR|
			'style': {1, 1},
			'v_sbl': '\u250B',
			'h_sbl': '',
			'Xoff' : 0,
			'Yoff' : 0,
			},
		'LC_pd': '\t',
		'RC_pd': '\t',
		'mrgn' : ' ',
		'al'   : 'left'
		},  # M META
	'D': [  # Data
		[1, '{D:0,1}}', 'da1ta2'],
		[2, '      ', '\033[1msomedata ', ],
		[f'\033[32m{3}', 'selected row', 'data5299\033[0m'],
		],
	'F': [['help'], ['footer']]
	}

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
def tty_len(*a, **k):
	re = presets_re()
	wtab = '\u0020' * (k.get('t') or 4)
	s = str(k.get('s')) or a.s
	s = re.repl_ESCt(wtab, str(s))
	s = re.repl_ANSIm('', str(s))
	return len(s)
def presets_re():
	import types
	import re
	
	preset = types.SimpleNamespace()
	preset.repl_ANSIm = re.compile(r'\033\[[;\d]*m', re.VERBOSE).sub
	preset.repl_ESCt = re.compile(r'\t', re.VERBOSE).sub
	return preset
def std_wr(s):
	sys.stdout.write(str(s))
	sys.stdout.flush()


def tty_writesbl(s):
	def stdout_write():
		sys.stdout.write(s)
		sys.stdout.flush()
		return tty_len()
	return stdout_write

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
	fs = table.get('M').get('fs')
	tbl.meta.pd = table.get('M').get('pd')
	tbl.meta.al = table.get('M').get('al')
	tbl.meta.mg = table.get('M').get('mg')
	return tbl

def mtx_tblsurface(fs, mg, pd, data):
	# cell= padd[:x]+data+padd[x:]
	# fs= mg+fs+mg
	cells_dmy = [str().ljust(mx, '#').ljust(mx + tty_len(pd), pd) for mx in lst_datamax(data)]
	len_fs = tty_len(s=f'{mg}{fs}{mg}')
	
	rowdummy = f'{mg}{fs}{mg}'.join(cells_dmy)
	print(('dummy', rowdummy) for line in data)



def lst_mrg(mrg, headers) -> list:
	return	[['', mrg],*[[mrg,mrg] for ncol in headers][:-2],[mrg,'']]

def lst_lnmrg(lst_mrg) -> list:
	return [(tty_len(mrg[m-1][1])+tty_len(mrg[m][0])) for m,mrg in enumerate(lst_mrg,start=1)]

def lst_pdd(pdd, headers) -> list:
	return [pdd for ncol in headers]

def lst_lnpdd(lst_pdd) -> list:
	return [tty_len(pdd) for pdd in lst_pdd]

def lst_fss(fs,headers) -> list:
		return ['',]+[fs for item in headers]

def lst_css(lst_fss,lst_mrg):
	return [f'{lst_mrg[i-1][1]}{fss}{lst_mrg[i][0]}' for i,fss in enumerate(lst_fss,start=1)]

def lst_lncss(lst_css):
	return [tty_len(css) for css in lst_css]

def lst_maxdataw(piv_dataw) -> list:  # calculate the minimum width of collumn for all data in col to fit .
	return [max(col) for col in piv_dataw]

def lst_lncoll(lst_maxdataw,lst_lnpdd) -> list:
	return [(lndata + lnpdd) for lndata, lnpdd in zip(lst_maxdataw, lst_lnpdd)]

def lst_offset_coll(lst_lncoll,lst_lncss):
	def addrel(add,rel=[],offset=[0,]):
		rel+=[add]
		offset+=[sum(rel)]
		return offset
	for lncoll,lncss in zip(lst_lncoll,lst_lncss):
		lst_offset_coll=addrel(lncoll+lncss)
	return lst_offset_coll
	

def lst_ltorg(fs,cellw) -> list:
	lst_leftbounds = [0, ]
	lst_cellbwidths = [0, ] + [i + tty_len(s=fs) for i in cellw]
	lst_leftbounds += [lst_cellbwidths[i] + cell + tty_len(s=fs) for i, cell in enumerate(cellw[:-1])]
	return lst_leftbounds



def lst_stdw_ltorg() -> list:
	return [tty_writesbl(s=G(lb)) for lb in lst_ltorg(**k)]

def lst_stdw_fsorg() -> list:
	return [tty_writesbl(s=G(pd)) for pd in lst_fsorg(**k)]

def mtx_dataw(mtx_data) -> list:
	return [[tty_len(s=cell) for cell in row] for row in mtx_data]

def mtx_relorg(data) -> list:
	return [[[f'{F(r)}{G(lst_cellw(**k)[c])}'] for c, cell in enumerate(data[r])] for r, row in enumerate(data)]

def tbl_calc(table):
	tbl = dcon_table(table)
	
	def calc(fn,a):
		return fn(*a)

	def c():
		import types
		c 					= types.SimpleNamespace()
		c.lst				=types.SimpleNamespace()
		c.lst.pdd					= calc(lst_pdd, 			[tbl.meta.pd ,tbl.headers])  # [4, 4, 4]
		c.lst.collw 			= calc(lst_datamax, 	[tbl.data,])  # +___[5, 10, 9]
		c.lst.cellw 			= calc(lst_cellw, 		[c.lst.pdd,c.lst.collw])  # =		[9, 14, 13] __/_+2
		c.lst.ltorg 			= calc(lst_ltorg, 		[tbl.meta.fs,c.lst.cellw ])  # [0, 11, 27] 		/	+ =
		c.lst.fsorg 			= calc(lst_fsorg, table)  # [9, 25] 			| field separator
		c.lst.stdw_ltorg	= calc(lst_stdw_ltorg, table)
		c.lst.stdw_fsorg	= calc(lst_stdw_fsorg, table)
		c.mtx				=types.SimpleNamespace()
		c.mtx.dataw = tbl_dim(mtx_dataw, table)  # [	[1, 2, 3], [[['\x1b[0F\x1b[9G'], ['\x1b[0F\x1b[14G'], ['\x1b[0F\x1b[13G']],
		c.mtx.relorg = tbl_dim(mtx_relorg, table)  # [5, 10, 9]	[['\x1b[1F\x1b[9G'], ['\x1b[1F\x1b[14G'], ['\x1b[1F\x1b[13G']]
		return c  # [1, 5, 8]]	[['\x1b[2F\x1b[9G'], ['\x1b[2F\x1b[14G'], ['\x1b[2F\x1b[13G']]]
	
	mtx_tblsurface(table)
	return calc()

def listprt(lst):
	for tem in lst:
		print(repr(tem))

def listprt2(lst):
	print('fn')
	for tm in lst:
		[print(t) for t in tm]





calc = calc_dimensions(table1)
listprt2([calc.lst_pdd, calc.lst_collw, calc.lst_cellw, calc.lst_ltorg, calc.lst_fsorg, calc.mtx_dataw, calc.mtx_relorg, ])
# listprt2([calc.lst_stdw_ltorg])
# listprt2([calc.lst_stdw_fsorg])


calc = calc_dimensions(table=table1)
mtx_relorg = calc.mtx_relorg
stdw_table = []
# tbl=dcon_table(table=table1)
for r, row in enumerate(tbl.data):
	for c, cell in enumerate(row):
		calc.lst_stdw_ltorg[c]()
		(calc.lst_stdw_ltorg[c](), std_wr(tbl.data[r][c]))
		[(b(), std_wr(f'\033[0m{fs}')) for b in calc.lst_stdw_fsorg]
	std_wr('\n')

import time

row_next = tty_writesbl(s=M('10;10'))

# tpl_org=std_cursorloc()
# tbl_org=ANSI_H(f'{tpl_org[1]};{tpl_org[0]}')
# tpl_org=std_cursorloc()
dat_org = H('2;0')  # ANSI_H(f'{tpl_org[1]+2};{tpl_org[0]}')
# def fn(fnx):
# 	time.sleep(1)
# 	sys.stdout.write(f'{fnx}1');sys.stdout.flush()
# 	time.sleep(1)
# 	sys.stdout.write(f'\033[10{fnx}');sys.stdout.flush()
# 	time.sleep(1)
# 	sys.stdout.write(f'{fnx}2');sys.stdout.flush()
# 	time.sleep(1)
#
# import string
# alfab=string.ascii_uppercase
# print(alfab)
# for f in alfab:
# 	fn(f)


# 	def tmp():
# 		for r,row in enumerate(tbl_data):
# 			for c,cell in enumerate(row):
# 				sys.stdout.write(f'\033[{calc_leftbounds()[c]}G{cell}')
# 			for b,border in enumerate(calc_borderorg()):
# 				sys.stdout.write(f'\033[0m\033[{calc_borderorg()[b]}G{fs}')
# 			sys.stdout.write('\n')
#
#
#
# # [print(row) for row in rows]
# # print()
# # print()
#
# upper = [chr(i) for i in range(65, 91)]
# lower = [chr(i) for i in range(96, 123)]
#
#
#
# calc_dimensions(tbl=table1)
#
# calc_dimensions(tbl=table2)
