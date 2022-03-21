#!/usr/bin/env python
import os
import configparser
import logging


def new(*a):
	"""
	create an empty configparser with: extended interpolation, : for delimiter and allowing empty value's for keys
	:return: configerparser obj.
	"""
	cfg = configparser.ConfigParser(	interpolation		=	configparser.ExtendedInterpolation(),
																		delimiters			=	':',
																		allow_no_value	=	True	)  # create empty config
	cfg.optionxform = lambda option: option
	return cfg

# def set(key,value,section,file):
# 	set_key(file=file, section=section, key=key, value=value)
	
def readfile(**k):
	"""
	gets config
	:param k: path,conf
	:keyword path: path
	:keyword c: config parser
	:return:
	"""
	c=k.get('c')
	path=k.get('f')
	if os.path.exists(path):
		c.read(path)
	return c

def savefile(**k) -> None:
	"""
	writes the configparser config to a file.
	:param k: keywords:file,conf
	:keyword file: file to save the config to
	:keyword conf: config(configparser) to be saved
	:return:
	"""
	file= k.get('f')
	conf=k.get('c')
	with open(file, 'w') as file:
			conf.write(file)


def set_key(**k):
	"""
	
	:keyword key:
	:keyword val:
	:keyword section:
	:keyword file:
	:return: config
	"""
	G=k.get('c')
	file = k.get('f')
	section=k.get('s')
	key=k.get('key')
	val=k.get('val')
	config=G[file] if G.get(file) else new()
	config[section]= G[file][section] if dict(config).get(section) else {}
	config[section][key]=str(val)
	G[file]=config
	return G


def set_dict(dct,cfg):
	"""
	loads a dictionary formatted config group into the config ,
	the dictionary needs to meet the following specifications:
	the first two key:val pairs are file:<filename >and section:<section-name> within the file
	example:
	config={file : btrwin,
					section: PATH,
					key1: val1}
	:param dct: dictionary where the first two key:val pairs are file:filename and section within the file
	:return:
	"""
	file = dct.pop('file')
	section= dct.pop('section')
	for key in dct.keys():
		G=set_key(key=key,val=dct[key],section=section,file=file,config=cfg)
	return G


