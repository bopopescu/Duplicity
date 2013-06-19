#!/usr/bin/env python

########################
#### SETUP DUPLICITY####
########################

import os

duplicity_dependencies = [
'librsync-0.9.7',
'boto-2.6.0',
'ncftp-3.2.5',
'pth-2.0.7',
'libksba-1.3.0',
'libgcrypt-1.5.1',
'libgpg-error-1.9',
'libassuan-2.1.0',
'gnupg-2.0.19',
'GnuPGInterface-0.3.2',
'Duplicity-0.6.21'
]

python_installation = [
'boto-2.6.0',
'GnuPGInterface-0.3.2',
'Duplicity-0.6.21'
]

non_make_install = ['librsync-0.9.7']

install_cmds = {
	'python': '; sudo python setup.py install',
	'normal': ';sudo ./configure && make'

}

def getInstallationCommand(name):
	if name in python_installation:
		return "; sudo python setup.py install"
	else if :
		print ''
		else:
			print ''

def install(path, type = 'default'):
	if type == 'python':
		install_cmd = "; sudo python setup.py install"
	else:
		#TODO: add make clean
		install_cmd = ";sudo ./configure && make "

	if make_install == True:
		install_cmd += " && make install"

	cmd = "cd " + path + install_cmd
	# print cmd
	os.system(cmd)

def setup():
	print "Setting up duplicity\n"
	print "List of dependencies: " + str(duplicity_dependencies)

	for lib in duplicity_dependencies:
		install(lib)

if __name__ == '__main__':
	setup()
