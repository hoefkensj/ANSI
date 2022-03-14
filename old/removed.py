#!/usr/bin/env python



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




# def ANSI(**k) -> types.SimpleNamespace:
# 	"""
# 	returns the namespace for all ansi functions
# 	:param k: keywords : [ns,]
# 	:keyword ns: a namespace to work with this can just be "types.SimpleNamespace"
# 	:return: the ansi functions in a Namespace where namespace.$[a-Z] ~\033[x;x;x$[a-Z]
# 	"""
# 	NS		=	k.get('ns')
# 	NS.A	=	fn('E')
# 	NS.B	=
# 	NS.C	=
# 	NS.D	=
# 	NS.E	= fn('E')
# 	NS.F	= fn('F')
# 	NS.G	= fn('G')
# 	NS.H	= fn('H')
# 	NS.I
# 	NS.J
# 	NS.K	= fn('K')
# 	NS.m	= fn('m')
# 	return ANSI
#
#
# ANSI=ANSI()
# ANSI_E= fn('E')
# ANSI_F= fn('F')
# ANSI_G= fn('G')
# ANSI_H= fn('H')
# ANSI_K= fn('K')
# ANSI_m= fn('m')


# ANSI.m=fn('m')


# table['IDXX']	=	idxy(data)
# table['DATA'] = data


# print(repr(table))
# print(ord('A'))
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
#

# def lst_ltorg(fs,cellw) -> list:
# 	lst_leftbounds = [0, ]
# 	lst_cellbwidths = [0, ] + [i + tty_len(s=fs) for i in cellw]
# 	lst_leftbounds += [lst_cellbwidths[i] + cell + tty_len(s=fs) for i, cell in enumerate(cellw[:-1])]
# 	return lst_leftbounds

# def terminal_width(**k):
# 	stored = k.get('stored')
# 	width = (shutil.get_terminal_size()[0] - 2)
# 	stored += [width]
# 	diff = (-1 * (stored[-2] - stored[-1]))
# 	return stored




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
						'heads_yxH'		: lst_heads_yxH,
					},
	'mtx':	{
						'idxy'				:	mtx_idxy,
						'data'				: mtx_data,
			      'dataw' 			: mtx_dataw,
		    	  'piv_dataw'   :	piv_dataw,
		    	  'offx'				: mtx_offx,
						'offy'				: mtx_offy,
						'data_yxH'		: mtx_data_yxH,
						'cfss_xyH'		:	mtx_cfss_xyH,
					},
	}