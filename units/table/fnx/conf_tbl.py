#!/usr/bin/env python
import ANSI.fnx.markup

cfg_table_block={
'keys': [],
'vals':	[],
}

cfg_table_tits=cfg_table_block
cfg_table_hdrs={}
cfg_table_meta={}
cfg_table_data={}
cfg_table_ftrs={}
cfg_table_clcd={}
cfg_table_orgs={}


META={
		'fss': {
						'char'	: '\u2502',  # B',\u2502
						'show'	:	[0,1,0],
						},
		'pdd': {
						'char'	:	' ',
						'show'	:	[0,0,0]
						},
		'mrg': {
						'char'	: ' ',
						'show'	:	[0,2,0]
						},
		'hal': {
						'l': 	[1],
						'c':	[2,3],
						'r':	[]
						},
		'dal': {
						'l':	[1],
						'c':	[],
						'r':	[2,3]
						}
		}
HDRS= 	['2k22', 'HOEFKENSJ', '@GitHub'],  # H HEADERS
DATA=[
				[1 , 'cell', '@#$%'],
				[2 , '\x1b[32mcolors', '\u255FUnicode\u255F' ],
				['3' , '\033[7m     SELECTIONS', '\033[7mCELL|ROW BASED'],
				[4 , 'Green', ''],
				[5 , 'ANSI', 'TABLE'],
				['\033[31m100%','\033[31mOOP FREE CODE','\033[31mTHE_UNLICENCE!']
			]
table_calc={}


table1 = {
	'T': [['title'], ['subtitle']],  # T TITLES
	
	'M': table_meta,  # M META
	'D': table_data,
	'F': [['help'], ['footer']],
	'C': table_calc,
	}

cfg_table={
	'T':{},
	'H':{},
	'M':META,
	'D':DATA,
	'F':{},
	'C':{},
	'O':{},
}