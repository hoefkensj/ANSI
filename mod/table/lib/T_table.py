#!/usr/bin/env python
import sys
import ANSI.lib.ansi
import ANSI.lib.m
import ANSI.fnx.m

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
	
	
def tbl_create(tbl):
	tbl					= ANSI.units.table.mod.mod_M_cfss.calc_lst_mrg(tbl)
	tbl					= ANSI.units.table.mod.mod_M_cfss.calc_lst_fss(tbl)
	tbl					= ANSI.units.table.mod.mod_M_cfss.calc_lst_lnmrg(tbl)
	tbl					= ANSI.units.table.mod.mod_M_cfss.calc_lst_css(tbl)
	tbl					= ANSI.units.table.mod.mod_M_cfss.calc_lst_lncss(tbl)
	tbl					= ANSI.units.table.mod.mod_M_cpdd.calc_lst_lncoll(tbl)
	tbl					= ANSI.units.table.mod.mod_C_offsets.calc_lst_offset_coll(tbl)
	
	tbl					= ANSI.units.table.mod.mod_D_data.calc_mtx_D_data(tbl)
	tbl					= ANSI.units.table.mod.mod_C_offsets.calc_mtx_offx(tbl)
	tbl					= ANSI.units.table.mod.mod_C_offsets.calc_mtx_offy(tbl)
	
	tbl					= ANSI.units.table.mod.mod_H_hdrs.calc_lst_H_hdrs(tbl)
	tbl					= ANSI.units.table.mod.mod_H_hdrs.calc_lst_H_hdrs_yxH(tbl)
	tbl					= ANSI.units.table.mod.mod_H_hdrs.calc_lst_H_cfss_yxH(tbl)
	
	tbl					= ANSI.units.table.mod.mod_D_data.calc_mtx_D_data_yxH(tbl)
	tbl					= ANSI.units.table.mod.mod_D_data.calc_mtx_D_cfss_yxH(tbl)
	tbl					= ANSI.units.table.mod.mod_D_data.calc_mtx_D_cfss(tbl)
	tbl					= ANSI.units.table.mod.mod_H_hdrs.sel_lst_H_jsthdrs(tbl)
	tbl					= idx_org(tbl)
	return tbl

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
		

def tbl_C_repl(tbl,txt=None,loc=0.0,):
	E=ANSI.lib.ansi.cursor['nextline']
	O=tbl['O']
	loc=O.get(loc)
	org=O.get(0.0)
	mxy=max([key for key in O.keys()])+2
	ANSI.fnx.m.stdout_mwrite(txt=[*loc,txt['txt']],style=txt['style']);sys.stdout.flush()
	ANSI.fnx.m.stdout_mwrite(txt=[*org,E(mxy)],style=[]);sys.stdout.flush()