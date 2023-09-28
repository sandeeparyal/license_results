#!/usr/bin/env python

import os
import csv
import sys
from datetime import datetime
import argparse
import glob

# Intro Text
print("\033[1;34;40m\n\nCSV listing of files \033[0m")

def options():
	parser = argparse.ArgumentParser(description="Create a list of images from a folder in a CSV file")
	parser.add_argument("-f", "--folder", help="Target folder of images.", required=True)
	parser.add_argument("-r", "--recurse", help="Search recursively.", default=False, action="store_true")
	args = parser.parse_args()
	return args

def main():

	# Get options
	args = options()

	# Identify the target directory
	target_raw = args.folder

	# Clean up Windows file paths
	if sys.platform.startswith('win'):
		target_raw = target_raw.replace('\\', '/')
		if not target_raw.endswith('/'):
			target = target_raw+"/"
	else: 
		target = os.path.join(target_raw, '') # Add trailing slash if missing
	print("The target directory is", target, '\nScanning folder for files...')

	# Generate Time Stamp and generate CSV name with timestamp
	thedate = datetime.now()
	filedatestring = thedate.strftime("%Y%m%d%H%M%S%f")
	csv_file_name = "File-List-"+filedatestring+".csv"
	csv_file = target+csv_file_name
	fieldnames = ['filepath', 'filetype']
	
	# Create CSV file
	with open(csv_file, 'w', newline='') as file:
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()

	# Check if search is to be recursive
	if args.recurse is True:
		state = True
		desc = '**/*.*'
	else:
		state = False
		desc = '*.*'

	# Iterate through folder and list files
	for f in glob.glob(target+desc, recursive=state):
		if sys.platform.startswith('win'): # Forward slashes in Windows
			f = f.replace("\\", "/")
		with open(csv_file, 'a', newline='') as file:
			writer = csv.DictWriter(file, fieldnames=fieldnames)
			writer.writerow({'filepath':f, 'filetype':'pdf'})

	# Statement
	print("\033[1;32;40mComplete! \033[0m Your CSV was saved to", csv_file)

if __name__ == '__main__':
	main()
