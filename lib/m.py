#!/usr/bin/env python

def dct_aliasses():
	return {
		0										:	0,
		'reset'							:	0,
		'bold'							:	1,
		'faint'							:	2,
		'italic'						:	3,
		'uline'							:	4,
		'sblink'						:	5,
		'fblink'						:	6,
		'inv'								:	7,
		'hide'							:	8,
		'strike'						:	9,
		'font_A'						:	10,
		'font_B'						:	11,
		'font_C'						:	12,
		'font_D'						:	13,
		'font_E'						:	14,
		'font_F'						:	15,
		'font_G'						:	16,
		'font_H'						:	17,
		'font_I'						:	18,
		'font_J'						:	19,
		#20
		'd_uline'						:	21,
		#22
		#23
		'no_uline'					:	24,
		'no_blink'					:	25,
		#26
		#27
		#28
		'no_strike'					:	29,
		'fg_black'					:	30,
		'fg_red'						:	31,
		'fg_green'					:	32,
		'fg_yellow'					:	33,
		'fg_blue'						:	34,
		'fg_magenta'				:	35,
		'fg_cyan'						:	36,
		'fg_white'					:	37,
		'fg_rgb'						:	38,
		'bg_black'					:	40,
		'bg_red'						:	41,
		'bg_green'					:	42,
		'bg_yellow'					:	43,
		'bg_blue'						:	44,
		'bg_magenta'				:	45,
		'bg_cyan'						:	46,
		'bg_white'					:	47,
		'bg_rgb'						:	48,
		'black'							:	30,
		'red'								:	31,
		'green'							:	32,
		'yellow'						:	33,
		'blue'							:	34,
		'magenta'						:	35,
		'cyan'							:	36,
		'white'							:	37,
		'rgb'								:	38,
		'bblack'						:	40,
		'bred'							:	41,
		'bgreen'						:	42,
		'byellow'						:	43,
		'bblue'							:	44,
		'bmagenta'					:	45,
		'bcyan'							:	46,
		'bwhite'						:	47,
		}

def str_seq(style):
	def mkup(m):
		dct_markup=dct_aliasses()
		return dct_markup.get(m)
	
	lst_seq=[str(mkup(s)) for s in style]
	str_seq=str(';').join(lst_seq)
	return str_seq