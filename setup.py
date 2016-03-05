#!/usr/bin/python

"""
setup.py for SWIG
"""

from distutils.core import setup, Extension
#from distutils.sysconfig import get_python_inc
#import os

#incdir = os.path.join(get_python_inc(plat_specific=1), 'Numerical')

wallaby_module = Extension(
	'_wallaby', 
	sources=[
		'wallaby_wrap.c',
		#'/home/root/libwallaby/libwallaby/src/wallaby_p.cpp'
		],
	include_dirs=[
		#incdir,
		'/usr/include',
		'/home/root/libwallaby/libwallaby/include/wallaby/',
		'/home/root/libwallaby/libwallaby/src/',
		#'/usr/include/wallaby/',
		#'/usr/include/c++/4.9.2/',
		#'/usr/include/c++/4.9.2/arm-poky-linux-gnueabi/',
		#'/lib/',
		],
	libraries=[
		'wallaby'
		],
	swig_opts=[
		'-python',
		'-I/usr/include/wallaby/',
		'wallaby.i',
		] 
	)

setup (name = 'wallaby',
	version = '1.0',
	author = "NOT_KISS",
	description = """kovan/wallaby SWIG thing""",
	#packages=['distutils, 'distutils.command'],
	ext_modules = [
		wallaby_module,
		],
	py_modules = ["wallaby"],
	)
