#!/usr/bin/env python
"""
ANSI: ^ESC[]m module
"""
import sys
import ANSI.lib.m
import ANSI.lib.std
import ANSI.lib.ansi

fn=ANSI.lib.ansi.fn()
esc_m=fn.markup.m

def str_style(style) -> str :
	str_seq=ANSI.lib.m.str_seq(style)
	str_ansim=esc_m(str_seq)
	txt='{ANSI}{STRING}'.format(ANSI=str_ansim,STRING='{STRING}')
	return txt
	
def stdwset_style(style) -> callable:
	template=str_style(style)
	def stdout_write(txt):
		txt=template.format(STRING=str(txt))
		ANSI.lib.std.stdout_w(txt)
	return stdout_write

def stdout_mwrite(txt,style) -> str :
	template='{TEMP}'
	
	if len(style) > 0 and(style[-1] == 0 or style[-1] =='reset'):
		str_fin=ANSI.lib.m.str_seq([0])
		str_seq=ANSI.lib.m.str_seq(style[:-1])
		str_ansim=esc_m(str_seq)
		str_finm=esc_m(str_fin)
		template=template.format(TEMP=str().join([str_ansim, '{TEMP}']))
		template=template.format(TEMP=str().join(['{TEMP}',str_finm]))
	else:
		str_seq=ANSI.lib.m.str_seq(style)
		str_ansim=esc_m(str_seq)
		template=template.format(TEMP=str().join([str_ansim, '{TEMP}']))
	
	str_mwrite=template.format(TEMP=str().join([chunk for chunk in txt]))
	sys.stdout.write(str_mwrite)
	sys.stdout.flush()
	# sys.stdout.write('{ANSI}{STRING}'.format(ANSI=str_ansim,STRING=str(txt)));sys.stdout.flush()
	return str_mwrite

