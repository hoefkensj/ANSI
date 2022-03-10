#!/usr/bin/env python
import sys
import ANSI.lib.m
import ANSI.lib.std
import ANSI.lib.ansi
fn=ANSI.lib.ansi.fn()
esc_m=fn.markup.m

def set_style(style) -> string :
	str_ansim=ANSI.lib.m.m_seq(style)
	txt='{ANSI}{STRING}'.format(ANSI=str_ansim,STRING='{STRING}')
	return txt
	
def stdwset_style(style) -> function :
	template=set_style(style)
	def stdout_write(txt):
		txt=template.format(STRING=str(txt))
		ANSI.lib.std.stdout_w(txt)
	return stdout_write

def stdout_mwrite(txt,style) -> string :
	sys.stdout.write('{ANSI}{STRING}'.format(ANSI=ANSI.lib.m.m_seq(style),STRING=str(txt)));sys.stdout.flush()
	return '{ANSI}{STRING}'.format(ANSI=ANSI.lib.m.m_seq(style),STRING=str(txt))

# test=std_mwrite('test',style=['blue'])
# test()
# stdout_mwrite('ikkel',style=[0,'uline'])