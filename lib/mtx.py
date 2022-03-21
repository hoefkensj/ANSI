#!/usr/bin/env python
def mtx_pivot(mtx) -> list:
	piv=[]
	pivr=[[] for c in mtx[0]]
	for r,row in enumerate(mtx):
		for c,col in enumerate(row):
			pivr[c]+=[col]
	piv+=pivr
	return piv