#!/usr/bin/env python
import ANSI.fnx
import ANSI.lib.lib_tty

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
	lst_pdd=calc_lst_pdd(tbl)
	tbl['C']['lst_lnpdd']=[ANSI.lib.lib_tty.tty_len(pdd) for pdd in lst_pdd]
	return tbl

def calc_lst_lncoll(tbl) -> list:
	tbl=calc_lst_lnpdd(tbl)
	lst_lnpdd=tbl['C']['lst_lnpdd']
	tbl= ANSI.fnx.table.mod_D_data.calc_lst_maxdataw(tbl)
	lst_maxdataw=tbl['C']['lst_maxdataw']
	tbl['C']['lst_lncoll']=[(lndata + lnpdd) for lndata, lnpdd in zip(lst_maxdataw, lst_lnpdd)]
	return tbl