#!/usr/bin/env python
import sys
import ANSI.lib.ansi
import ANSI.fnx.m
import ANSI.table

tbl_1=table1

tbl_1,write_table1=tty_printtable(tbl_1)
print('\n')

def respcol(val):
	color= 'red'
	if 300< val < 750 :
		color='yellow'
	if val > 750:
		color='green'
	return color



import time
def  str_mrepl(txt,style):
	mstring={
		'txt':f'{txt}',
		'style': style}
	return mstring
	
	
def counter():
	table.mod_table.tbl_C_repl(tbl_1, txt=str_mrepl(' LIVE PROGRESS:', ['red', 'sblink']), loc=4.2, )
	for count in range(1001):
		table.mod_table.tbl_C_repl(tbl_1, txt=str_mrepl(f'          {str(count).zfill(4)}', [respcol(count)]), loc=4.3, )
		time.sleep(0.005)
	table.mod_table.tbl_C_repl(tbl_1, txt=str_mrepl('         DONE!!', ['green', 'bold']), loc=4.2, )

write_table1()
counter()

E=ANSI.lib.ansi.cursor['nextline']
org=tbl_1['O'].get(0.0)
mxy=max([key for key in tbl_1['O'].keys()])+2
# ANSI.fnx.m.stdout_mwrite(txt=org,style=[]);sys.stdout.flush()
ANSI.fnx.m.stdout_mwrite(txt=[E(int(mxy))],style=[]);sys.stdout.flush()
# print('\n'*mxy)
# ext(tbl_1)