#!/usr/bin/env python
import ANSI.lib.tty

def calc_lst_mrg(tbl) -> list:
	mrg=tbl['M']['mrg']['char']
	ncdata=len(tbl['D'][0])
	lst_mrg=[['',mrg],*[[mrg,mrg] for  i in range(ncdata+1-2)],[mrg,'']]
	tbl['C']['lst_mrg']=lst_mrg
	return tbl

def calc_lst_lnmrg(tbl) -> list:
	ttyln=ANSI.lib.lib_tty.tty_len
	lst_mrg=tbl['C']['lst_mrg']
	lst_lnmrg=[ttyln(lst_mrg[m][1])+ttyln(lst_mrg[m+1][0]) for m,_ in enumerate(lst_mrg[:-1])]
	tbl['C']['lst_lnmrg']=lst_lnmrg
	return tbl

def calc_lst_fss(tbl) -> list:
	ncdata=len(tbl['D'][0])

	fs=tbl['M']['fss']['char']
	lst_fss=[fs for i  in  range(ncdata+1)]
	tbl['C']['lst_fss']=lst_fss
	return tbl

def calc_lst_css(tbl):
	ncdata=len(tbl['D'][0])
	fs_show=tbl['M']['fss']['show']
	lst_fs_show=[fs_show[0],*[fs_show[1] for i in range(ncdata+1-2)],fs_show[-1]]
	lst_fss=tbl['C']['lst_fss']
	lst_mrg=tbl['C']['lst_mrg']
	lst_css=[]
	for mrg,fss,show in zip(lst_mrg,lst_fss,lst_fs_show):
		lst_css+=[f'{mrg[0]}{fss}{mrg[1]}'*show]
	# lst_css=[f'{lst_mrg[i][1]}{lst_fss[i]}{lst_mrg[i+1][0]}' for i in range(len(lst_fss))]
	tbl['C']['lst_css']=lst_css
	return tbl

def calc_lst_lncss(tbl):
	lst_css=tbl['C']['lst_css']
	lst_lncss=[ANSI.lib.lib_tty.tty_len(css) for css in lst_css]
	tbl['C']['lst_lncss']=lst_lncss
	return tbl

def mtx_D_cfss_yxH(tbl):
	mtx_offx=tbl['C']['mtx_offx']
	mtx_offy=tbl['C']['mtx_offy']
	crd=lib.lib_tty.pos_cursor()
	H=lib.ansi.cursor['pos']
	lst_lncss=tbl['C']['lst_lncss']
	mtx_D_cfss_yxH=[[[] for col in row] for row in mtx_offx]
	for r,(rowx,rowy) in enumerate(zip(mtx_offx,mtx_offy)):
		for c,(colx,coly) in enumerate(zip(rowx,rowy)):
			x=str(colx+crd['x']-lst_lncss[c])
			y=str(coly+crd['y'])
			ansi=H(';'.join([y,x]))
			mtx_D_cfss_yxH[r][c]=ansi
	return {'mtx_D_cfss_yxH' : mtx_D_cfss_yxH }
	
def mtx_D_cfss(tbl):
	lst_css=tbl['C']['lst_css']
	mtx_D_data=tbl['C']['mtx_D_data']['l']
	tbl_data=tbl['D']
	mtx_D_cfss=[[[] for col in row] for row in tbl_data]
	for r,row in enumerate(mtx_D_data):
		for c,col in enumerate(row):
			mtx_D_cfss[r][c]=lst_css[c]
	return {'mtx_D_cfss': mtx_D_cfss}
