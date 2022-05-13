#!/usr/bin/env python
import lib.tty
import lib.mtx

def mtx_T_data(arr_data)->dict:
	for row in arr_data:


def mtx_D_cells(tbl)-> dict:



def mtx_D_data(tbl):
	lst_lncoll=tbl['C']['lst_lncoll']
	tbl_data=tbl['D']
	char=tbl['M']['pdd']['char']
	pdd=tbl['D']
	mtx_datal=[[[] for col in row] for row in tbl_data]

	for r,row in enumerate(tbl_data):
		for c,cell in enumerate(row):
			str_tty					=	lib.lib_tty.tty_str(str(cell))
			str_mtty				=	lib.lib_tty.tty_mstr(str(cell))
			str_tty_l 			= str_tty.ljust(lst_lncoll[c],char)

			str_mtty_l 			= str_tty_l.replace(str_tty,str_mtty)

			mtx_datal[r][c]	=	str_mtty_l

	mtx_data= {
		'l'	:	mtx_datal,
		}
	return {'mtx_D_just': mtx_data}

def mtx_D_data(tbl):
	lst_lncoll=tbl['C']['lst_lncoll']
	tbl_data=tbl['D']
	char=tbl['M']['pdd']['char']
	pdd=tbl['D']
	mtx_datal=[[[] for col in row] for row in tbl_data]
	mtx_datar=[[[] for col in row] for row in tbl_data]
	mtx_datac=[[[] for col in row] for row in tbl_data]

	for r,row in enumerate(tbl_data):
		for c,cell in enumerate(row):
			str_tty					=	lib.lib_tty.tty_str(str(cell))
			str_mtty				=	lib.lib_tty.tty_mstr(str(cell))
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
	return {'mtx_D_just': mtx_data}


def mtx_D_data_yxH(tbl):
	mtx_offx=tbl['C']['mtx_offx']
	mtx_offy=tbl['C']['mtx_offy']
	crd=lib.lib_tty.pos_cursor()
	H=lib.ansi.cursor['pos']
	mtx_D_data_yxH=[[[] for col in row] for row in mtx_offx]
	for r,row in enumerate(zip(mtx_offx,mtx_offy)):
		for c,col in enumerate(zip(row[0],row[1])):
			x=str(col[0]+crd['x'])
			y=str(col[1]+crd['y'])
			ansi=H(';'.join([y,x]))
			mtx_D_data_yxH[r][c]=ansi
	return {'mtx_D_data_yxH': mtx_D_data_yxH}



def mtx_D_w(tbl) -> dict:
	return {'mtx_D_w': [[lib.lib_tty.tty_len(cell) for cell in row]for row in tbl['D']]}

def lst_D_wmax(tbl) -> list:  # calculate the minimum width of collumn for all data in col to fit .
	mtx_D_w=tbl['C']['mtx_D_w']
	piv_D_w=lib.mtx.mtx_pivot(mtx_D_w)
	return {'lst_maxdataw' : [max(col) for col in piv_D_w]}