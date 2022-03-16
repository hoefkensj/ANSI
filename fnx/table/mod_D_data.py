#!/usr/bin/env python
import ANSI.lib.lib_tty
import ANSI.fnx.table.table


def calc_mtx_D_data(tbl):
	import ANSI.lib.lib_tty
	lst_lncoll=tbl['C']['lst_lncoll']
	tbl_data=tbl['D']
	char=tbl['M']['pdd']['char']
	pdd=tbl['D']
	mtx_datal=[[[] for col in row] for row in tbl_data]
	mtx_datar=[[[] for col in row] for row in tbl_data]
	mtx_datac=[[[] for col in row] for row in tbl_data]

	for r,row in enumerate(tbl_data):
		for c,cell in enumerate(row):
			str_tty					=	ANSI.lib.lib_tty.tty_str(str(cell))
			str_mtty				=	ANSI.lib.lib_tty.tty_mstr(str(cell))
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
	tbl['C']['mtx_D_data']=mtx_data
	return tbl

def calc_mtx_D_cfss(tbl):
	import ANSI.lib.lib_tty
	lst_css=tbl['C']['lst_css']
	mtx_D_data=tbl['C']['mtx_D_data']['l']
	tbl_data=tbl['D']
	mtx_D_cfss=[[[] for col in row] for row in tbl_data]
	for r,row in enumerate(mtx_D_data):
		for c,col in enumerate(row):
			mtx_D_cfss[r][c]=lst_css[c]
	tbl['C']['mtx_D_cfss']=mtx_D_cfss
	return tbl
	
def calc_mtx_D_data_yxH(tbl):
	import ANSI.lib.lib_tty
	mtx_offx=tbl['C']['mtx_offx']
	mtx_offy=tbl['C']['mtx_offy']
	crd=ANSI.lib.lib_tty.pos_cursor()
	H=ANSI.lib.ansi.cursor['pos']

	mtx_D_data_yxH=[[[] for col in row] for row in mtx_offx]
	for r,row in enumerate(zip(mtx_offx,mtx_offy)):
		for c,col in enumerate(zip(row[0],row[1])):
			x=str(col[0]+crd['x'])
			y=str(col[1]+crd['y'])
			ansi=H(';'.join([y,x]))
			mtx_D_data_yxH[r][c]=ansi
	tbl['C']['mtx_D_data_yxH']=mtx_D_data_yxH
	return tbl

def calc_mtx_D_cfss_yxH(tbl):
	import ANSI.lib.lib_tty
	mtx_offx=tbl['C']['mtx_offx']
	mtx_offy=tbl['C']['mtx_offy']
	crd=ANSI.lib.lib_tty.pos_cursor()
	H=ANSI.lib.ansi.cursor['pos']
	lst_lncss=tbl['C']['lst_lncss']
	mtx_D_cfss_yxH=[[[] for col in row] for row in mtx_offx]
	for r,(rowx,rowy) in enumerate(zip(mtx_offx,mtx_offy)):
		for c,(colx,coly) in enumerate(zip(rowx,rowy)):
			x=str(colx+crd['x']-lst_lncss[c])
			y=str(coly+crd['y'])
			ansi=H(';'.join([y,x]))
			mtx_D_cfss_yxH[r][c]=ansi
	tbl['C']['mtx_D_cfss_yxH']=mtx_D_cfss_yxH
	return tbl

def calc_mtx_dataw(tbl):
	mtx_data=tbl['D']
	dataw=[]
	for r,row in enumerate(mtx_data):
		roww=[]
		for cell in row:
			roww+=[ANSI.lib.lib_tty.tty_len(cell)]
		dataw+=[roww]
	tbl['C']['mtx_dataw']=dataw
	return tbl

def calc_lst_maxdataw(tbl) -> list:  # calculate the minimum width of collumn for all data in col to fit .
	tbl=ANSI.fnx.table.mod_D_data.calc_mtx_dataw(tbl)
	mtx_dataw=tbl['C']['mtx_dataw']
	piv_dataw= ANSI.fnx.table.table.mtx_pivot(mtx_dataw)
	tbl['C']['lst_maxdataw']=[max(col) for col in piv_dataw]
	return tbl