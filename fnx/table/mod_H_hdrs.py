#!/usr/bin/env python
import ANSI.lib.lib_tty

def calc_lst_H_hdrs(tbl):
	import ANSI.lib.lib_tty
	lst_lncoll=tbl['C']['lst_lncoll']
	tbl_heads=tbl['H']
	char=tbl['M']['pdd']['char']
	hal=tbl['M']['hal']
	lst_headsl=[[] for col in tbl_heads]
	lst_headsr=[[] for col in tbl_heads]
	lst_headsc=[[] for col in tbl_heads]
	for c,cell in enumerate(tbl_heads):

		str_tty					=	ANSI.lib.lib_tty.tty_str(str(cell))
		str_mtty				=	ANSI.lib.lib_tty.tty_mstr(str(cell))
		str_tty_l 			= str_tty.ljust(lst_lncoll[c],char)
		str_tty_c 			= str_tty.center(lst_lncoll[c],char)
		str_tty_r 			= str_tty.rjust(lst_lncoll[c],char)
		str_mtty_l 			= str_tty_l.replace(str_tty,str_mtty)
		str_mtty_c 			= str_tty_c.replace(str_tty,str_mtty)
		str_mtty_r 			= str_tty_r.replace(str_tty,str_mtty)
		lst_headsl[c]	=	str_mtty_l
		lst_headsc[c]	=	str_mtty_c
		lst_headsr[c]	=	str_mtty_r
		dct_lsthdrs= {
			'l'	:	lst_headsl,
			'r'	:	lst_headsr,
			'c'	:	lst_headsc,
			}
	
	tbl['C']['dct_lsthdrs']=dct_lsthdrs
	return tbl

def calc_lst_H_hdrs_yxH(tbl):
	import ANSI.lib.lib_tty
	lst_offx=tbl['C']['lst_offset_coll']
	H=ANSI.lib.ansi.cursor['pos']
	crd=ANSI.lib.lib_tty.pos_cursor()
	lst_H_hdrs_yxH=[0 for  item in lst_offx]
	y=crd['y']
	for c,colx in enumerate(lst_offx):
		x=-1+colx+crd['x']
		lst_H_hdrs_yxH[c]=H(';'.join([str(y),str(x)]))
	tbl['C']['lst_H_hdrs_yxH']=lst_H_hdrs_yxH
	return tbl

def sel_lst_H_jsthdrs(tbl):
	dct_jsthdrs=tbl['M']['hal']
	lst_H_hdrs=tbl['H']
	dct_lsthdrs=tbl['C']['dct_lsthdrs']
	lst_H_jsthdrs=[]
	for c,col in enumerate(lst_H_hdrs,start=1):
		for al in dct_jsthdrs:
			if c in dct_jsthdrs[al]:
				lst_H_jsthdrs+=[dct_lsthdrs[al][c-1]]
	tbl['C']['lst_H_jsthdrs']=lst_H_jsthdrs
	return tbl

def calc_lst_H_cfss_yxH(tbl):
	import ANSI.lib.lib_tty
	lst_offx=tbl['C']['mtx_offx'][0]
	lst_css=tbl['C']['lst_css']
	ln_cfss=ANSI.lib.lib_tty.tty_len(lst_css[0])
	crd=ANSI.lib.lib_tty.pos_cursor()
	H=ANSI.lib.ansi.cursor['pos']
	lst_H_cfss_yxH=[[] for col in lst_offx[1:]]
	
	for c,col in enumerate(lst_offx[1:]):
		lst_H_cfss_yxH[c]=H(';'.join([str(crd['y']+1),str(col-1+crd['x']-ln_cfss)]))
	tbl['C']['lst_H_cfss_yxH']=lst_H_cfss_yxH
	print(repr(tbl['C']['lst_H_cfss_yxH']))
	return tbl