"""This script will attempt to add ttemp to a %PATH% folder"""
from __future__ import print_function
import os
import sys
import shutil

SRC_FOLDER_NAME = 'src'
SCRIPT_FILE_NAME = 'ttemp.py'
SCRIPT_RUNNER_NAME = 'ttemp.bat'
ENV_PATH = os.environ['PATH'].split(';')


def find_best_folder():
	# Best is 'C:\Python27\Scripts'
	py_scripts_folder = os.path.join(sys.path[1], 'Scripts')
	if py_scripts_folder in (os.path.normpath(p) for p in ENV_PATH):
		return py_scripts_folder

	# Next comes 'C:\Python27'
	if os.path.normpath(sys.path[1]) in (os.path.normpath(p) for p in ENV_PATH):
		return os.path.normpath(sys.path[1])

	# Use 'C:\Windows' if all else fails, safe to assume this is in %PATH%
	return os.environ['WINDIR']

def copy_file_to_folder(file, folder):
	try:
		shutil.copy2(file, folder)
	except shutil.Error as e:
		print("An Error occured when trying to copy! Try running this with Admin privileges.\n" + str(e))
		exit(1)


def main():
	best_folder = find_best_folder()
	# Find the script and copy it
	script_src_folder = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, SRC_FOLDER_NAME)
	copy_file_to_folder(os.path.join(script_src_folder, SCRIPT_FILE_NAME), best_folder)	

	# Write the .bat file that will run the script
	with open(os.path.join(best_folder, 'ttemp.bat'), 'w') as f:
		f.write('start pythonw {}\nexit'.format(os.path.join(best_folder, SCRIPT_FILE_NAME)))

	print("Transferred script to pathed folder: '{}'".format(best_folder))
	print("Try running 'ttemp' from the command prompt!")

if __name__ == '__main__':
	main()
