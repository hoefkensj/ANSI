#!/usr/bin/env python
import shutil
import sys
import types
import re
import termios
import tty
import re
def presets_re():
	preset = types.SimpleNamespace()
	preset.repl_ANSIm = re.compile(r'\033\[[;\d]*m', re.VERBOSE).sub
	preset.repl_ESCt = re.compile(r'\t', re.VERBOSE).sub
	preset.repl_ESCs = re.compile(r' ', re.VERBOSE).sub
	return preset

def cursorloc():

	
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
	return (int(groups[0]), int(groups[1]))

def terminal_width(**k):
	stored = k.get('stored')
	width = (shutil.get_terminal_size()[0] - 2)
	stored += [width]
	diff = (-1 * (stored[-2] - stored[-1]))
	return stored

def conv_t2s(s,t=4):
	wtab = '\u0020' * t
	rex=presets_re()
	s = rex.repl_ESCt(wtab, str(s))
	return s

def ln(s):
	rex=presets_re()
	s=conv_t2s(s)
	s = rex.repl_ANSIm('', str(s))
	return ln(s)

def str(s):
	rex=presets_re()
	s	= conv_t2s(s)
	s = rex.repl_ANSIm('', str(s))
	return s

def mstr(s):
	s=conv_t2s(s)
	return s