#!/usr/bin/env python
import types
import collections
import string



def main():
	pass


if __name__ == '__main__':
	main()


def fn(fn):
	def ansi(SEQ):
		def ANSIseq(ESC='\033', SEQ='{SEQ}', FN='{FN}'):
			return '{ESC}[{SEQ}{FN}'.format(ESC=ESC,SEQ=SEQ,FN=FN)
		return ANSIseq(SEQ=SEQ,FN=fn)
	return ansi
def markup(*a,**k):
	from . import markup
	return
