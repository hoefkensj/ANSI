#!/usr/bin/env python

'''
A 	Cursor Up 	(n=1) 	Move cursor up by n
B 	Cursor Down 	(n=1) 	Move cursor down by n
C 	Cursor Forward 	(n=1) 	Move cursor forward by n
D 	Cursor Back 	(n=1) 	Move cursor back by n

E 	Cursor Next Line 	(n=1) 	Move cursor to the beginning of the line n lines down
F 	Cursor Previous Line 	(n=1) 	Move cursor to the beginning of the line n lines up
G 	Cursor Horizontal Absolute 	(n=1) 	Move cursor to the the column n within the current row
H 	Cursor Position 	(n=1, m=1) 	Move cursor to row n, column m, counting from the top left corner

J 	Erase in Display 	(n=0) 	Clear part of the screen. 0, 1, 2, and 3 have various specific functions
K 	Erase in Line 	(n=0) 	Clear part of the line. 0, 1, and 2 have various specific functions

S 	Scroll Up 	(n=1) 	Scroll window up by n lines
T 	Scroll Down 	(n=1) 	Scroll window down by n lines

s 	Save Cursor Position 	() 	Save current cursor position for use with u
u 	Restore Cursor Position 	() 	Set cursor back to position last saved by s
f 	… 	… 	(same as G)
'''


def esc_fn(str_escfn):
	def esc_seq(seq):
		return str_escfn.format(seq)
	return esc_seq

cursor={
				'up' 								:	esc_fn('\x1B[{}A'), 			#			(n=1) 	Move cursor up by n
				'down' 							:	esc_fn('\x1B[{}B'), 		#	(n=1) 	Move cursor down by n
				'forward'						:	esc_fn('\x1B[{}C'), 		#	(n=1) 	Move cursor forward by n
				'back' 							:	esc_fn('\x1B[{}D'), 		#	(n=1) 	Move cursor back by n
				'nextline'					:	esc_fn('\x1B[{}E'), 		#	(n=1) 	Move cursor to the beginning of the line n lines down
				'prevline' 					:	esc_fn('\x1B[{}F'), 		#	(n=1) 	Move cursor to the beginning of the line n lines up
				'hzabsolute'				:	esc_fn('\x1B[{}G'), 		#	(n=1) 	Move cursor to the the column n within the current row
				'pos' 							:	esc_fn('\x1B[{}H'), 		#	(n=1, m=1) 	Move cursor to row n, column m, counting from the top left corner
				'savepos' 					:	esc_fn('\x1B[{}s'),			#	() 	Save current cursor
				'restpos' 					:	esc_fn('\x1B[{}u'),			#	() 	Set cursor back to position last saved by s
}
markup={
				'markup'										:	esc_fn('\x1B[{}m'),
				'm'													:	esc_fn('\x1B[{}m'),
				'clear_disp'								:	esc_fn('\x1B[{}J'),		#	(n=0) 	Clear part of the screen. 0, 1, 2, and 3 have various specific functions
				'clear_line'								:	esc_fn('\x1B[{}K'),	#	(n=0) 	Clear part of the line. 0, 1, and 2 have various specific functions
				'scroll_up'									:	esc_fn('\x1B[{}S'),	#	(n=1) 	Scroll
				'scroll_dn'									:	esc_fn('\x1B[{}T'),	#	(n=1) 	Scroll window
}

'\x1B'
'\u001b'

def fn() -> dict:
	global cursor
	global markup
	return {'cursor':cursor,'markup':markup,}


























	# csr			=	types.SimpleNamespace()
	# csr.up 											=	esc_fn('\x1B[{}A')		#			(n=1) 	Move cursor up by n
	# csr.dn 											=	esc_fn('\x1B[{}B')	#	(n=1) 	Move cursor down by n
	# csr.fw											=	esc_fn('\x1B[{}C')	#	(n=1) 	Move cursor forward by n
	# csr.bk 											=	esc_fn('\x1B[{}D')	#	(n=1) 	Move cursor back by n
	# csr.nl											=	esc_fn('\x1B[{}E')#	(n=1) 	Move cursor to the beginning of the line n lines down
	# csr.pl 											=	esc_fn('\x1B[{}F')	#	(n=1) 	Move cursor to the beginning of the line n lines up down by n lin
	# csr.ha											=	esc_fn('\x1B[{}G')	#	(n=1) 	Move cursor to the the column n within the current row
	# csr.ps 											=	esc_fn('\x1B[{}H')
	# csr.sp 											=	esc_fn('\x1B[{}s')	#	() 	Save current cursor
	# csr.rp 											=	esc_fn('\x1B[{}u')	#	() 	Set cursor back to position last saved by s