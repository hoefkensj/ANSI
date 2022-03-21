#!/usr/bin/env python
import sys
import ANSI.lib.ansi

F=ANSI.lib.ansi.cursor['prevline']
K=ANSI.lib.ansi.markup['clear_line']

def create_fn_Wtbl(table):
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
		surfy=len(table['D'])+1
		[print(K(2)) for row in range(surfy+2)]
		ANSI.fnx.m.stdout_mwrite(txt=[F(surfy+1),'\n'],style=[])
		# ANSI.fnx.m.stdout_mwrite(txt='\t\t\t\tt',style=[])
		table	= table.mod_table.tbl_create(table)
		def stdout_table():
			write_H_hdrs(table)
			write_C_cfss(table)
			write_D_data(table)
		return [table,stdout_table]
	return write_table(table)
	
	
