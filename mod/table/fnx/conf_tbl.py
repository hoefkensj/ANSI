#!/usr/bin/env python




META={
		'tit':	{'tit'			: None,	'sub'			:	None,	},
		'fss':	{'chr'	: '\u2502', 'dsp'	:	[0,1,0],	},
		'pdd':	{'chr'	:	' ',			'dsp'	:	[0,0,0]		},
		'mrg':	{'chr'	: ' ',			'dsp'	:	[0,2,0]		},
		'hal':	{'l': 	[1],	'c':	[2,3],'r':	[]		},
		'dal':	{'l':	[1],		'c':	[],		'r':	[2,3]	},
		}
HDRS= 	['2k22', 'HOEFKENSJ', 																	 '@GitHub'],  # H HEADERS





DATA_LAYERS=[['mtx_IDXY'],['mtx_XYAH'],['mtx_AM_row']['mtx_AM_col'],['mtx_AM_row'],['mtx_D_cell']['mtx_ansiM_reset']]



def create_table_conf():
	cfg_table={}
	cfg_table['META']=META