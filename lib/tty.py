#!/usr/bin/env python
import shutil
import sys
import types
import termios
import tty
import re


def presets_re():
	preset = types.SimpleNamespace()
	preset.repl_ANSIm = re.compile(r'\033\[[;\d]*m', re.VERBOSE).sub
	preset.repl_ESCt = re.compile(r'\t', re.VERBOSE).sub
	preset.repl_ESCs = re.compile(r' ', re.VERBOSE).sub
	return preset

def pos_cursor():
	if sys.stdout.isatty():
		buf = ""
		stdin = sys.stdin.fileno()
		tattr = termios.tcgetattr(stdin)
		try:
			tty.setcbreak(stdin, termios.TCSANOW)
			sys.stdout.write("\x1b[6n")
			sys.stdout.flush()
			while True:
				buf += sys.stdin.read(1)
				if buf[-1] == "R":
					break
		finally:
			termios.tcsetattr(stdin, termios.TCSANOW, tattr)
		# reading the actual values, but what if a keystroke appears while reading
		# from stdin? As dirty work around, getpos() returns if this fails: None
		try:
			matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
			groups = matches.groups()
		except AttributeError:
			return None
		x=int(groups[1])
		y=int(groups[0])
	else:
		#no tty
		x=20
		y=1
	return {'x': x ,'y':  y}

def terminal_width(**k):
	stored = k.get('stored')
	width = (shutil.get_terminal_size()[0] - 2)
	stored += [width]
	diff = (-1 * (stored[-2] - stored[-1]))
	return stored





def stdout_w(txt):
	sys.stdout.write(txt)
	sys.stdout.flush()
	return

def tty_conv(s,t=4):
	re = presets_re()
	wtab = '\u0020' * t
	s = re.repl_ESCt(wtab, str(s))
	return s
	
def tty_len(symbol,lntab=4,re=presets_re()):

	space='\u0020'
	wtab = f"{space * lntab}"
	sym = re.repl_ESCt(wtab,str(symbol))
	s = re.repl_ANSIm('',str(sym))
	lnstr=len(s)
	return lnstr

def tty_str(s):
	re = presets_re()
	s=tty_conv(s)
	s = re.repl_ANSIm('', str(s))
	return s
def tty_mstr(s):
	s=tty_conv(s)
	return s