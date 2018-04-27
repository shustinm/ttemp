from __future__ import print_function
from __future__ import absolute_import
import sys
import os
import time
import subprocess

TTEMP_FOLDER = os.path.join(os.path.expanduser('~'), 'ttemp')
TIME = time.localtime()


def open_folder_in_gui(folder_path):

	if sys.platform == 'darwin':
		subprocess.Popen(['open', folder_path])
	elif sys.platform == 'linux2':
		subprocess.Popen(['xdg-open', folder_path])
	else:
		os.startfile(folder_path)

def create_nested_folders(folder_list):
	for folder in folder_list:
		crete_folder_and_chdir(folder)
	open_folder_in_gui('.')
		
def crete_folder_and_chdir(folder_path):
	try:
		os.mkdir(folder_path)
	except OSError:
		pass
	finally:
		os.chdir(folder_path)

def main():
	try:
		os.mkdir(TTEMP_FOLDER)
	except OSError:
		pass
	finally:
		os.chdir(TTEMP_FOLDER)

	create_nested_folders((str(TIME.tm_year), str(TIME.tm_mon), str(TIME.tm_mday)))

if __name__ == '__main__':
	main()