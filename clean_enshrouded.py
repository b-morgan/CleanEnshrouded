#!/usr/bin/python3
#
# clean_enshrouded.py V0.2
#
# A python3 program written by: Brad Morgan
#
# Clean the ...\"Saved Games"\Enshrouded directory by 
# assuring the base world files are the most recent and 
# removing all the other world files.
#
import os
import time
import json
import datetime
import argparse
import subprocess
#
# slots contains a list of the Enshrouded filenames in slot order (-1)
# ext1 contains a list of filenames built from slots and ext1
# ext2 contains a list of the index files built from slots and ext2
# ext3 contains a list of filenames built from slots and ext1 and ext3
#
slots = ["3ad85aea", "3bd85c7d", "38d857c4", "39d85957", "36d8549e", "37d85631", "34d85178", "35d8530b", "32d84e52", "33d84fe5"]
ext1 = ["","_info"]
ext2 = ["-index", "_info-index"]
ext3 = ["", "-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9"]

#
# Configure command line arguments (in addition to the default -h, --help)
# The -c, --clean argument is required to take any action on the files.
#
parser = argparse.ArgumentParser(description='Process Enshrouded world files.')
parser.add_argument('-b', '--backup', action='store_true', help='backup all the world files first')
parser.add_argument('-c', '--clean', action='store_true', help='remove all but the base world files')
parser.add_argument('-w', '--wait', help='wait N seconds before exiting')
parser.add_argument('-d', '--directory', help='directory to process')
args = parser.parse_args()

if args.directory:
	os.chdir(args.directory)
print("\nProcessing files in:",os.getcwd(),"\n")

#
# Backup all the Enshrouded world files (filenames that start with 3)
# requires the program 7-zip, https://www.7-zip.org/
# or use 'powershell Compress-Archive -Path ".\3*" -DestinationPath ".\backup.zip" -Force'
#
if args.backup:
	try:
		f = open("backup.zip")
	except:
		pass
	else:
		f.close()
		os.remove("backup.zip")
	subprocess.run("7z a -x!*.* backup.zip 3*", stdout = subprocess.DEVNULL)
	print("Created backup.zip\n")

#
# Loop through the slot filenames
#
for slot, val in enumerate(slots, start=1):
	try:
		f = open(val)
	except:
		pass
	else:
		f.close()
		info = ""
#
# See if an _info file exists
#
		try:
			f = open(val+"_info")
		except:
			pass
		else:
			info = "and has a "+f.name
			f.close()
		print(val,"exists as slot", slot, info)
#
# See if there are -index json files
#
		for i, ext in enumerate(ext2):
			try:
				f = open(val+ext)
			except:
				pass
			else:
#
# Get the json data from the file
#
				jdat = json.load(f)
				f.close()
#
# Convert the epoch timestamp into a human readable value
#
				dt = datetime.datetime.fromtimestamp(jdat["time"])
				print("    ",f.name,"exists and points to",jdat["latest"])
#
# See if the file pointed to by the "latest" value exists
#
				try:
					f = open(val+ext1[i]+ext3[jdat["latest"]])
				except:
					print("    ",val+ext1[i]+ext3[jdat["latest"]],"not found")
				else:
#
# Convert the modified time of the file into a human readable value
#
					statinfo = os.stat(val+ext1[i]+ext3[jdat["latest"]])
					fdt = datetime.datetime.fromtimestamp(int(statinfo.st_mtime)) # the epoch is an integer
					if dt == fdt:
						match = "and they match"
					else:
						match = "and they don't match"
					print("    ","index time is",dt,val+ext1[i]+ext3[jdat["latest"]],"time is",fdt,match)
				f.close()
#
# The following code is only executed if there is a "-c" or "--clean" on the command line
#
				if args.clean:
#
# Rename the latest -n file to the base file
#
					if jdat["latest"] != 0:
						print("Deleting",val+ext1[i])
						os.remove(val+ext1[i])
						print("Renaming", val+ext1[i]+ext3[jdat["latest"]], "to", val+ext1[i])
						os.rename(val+ext1[i]+ext3[jdat["latest"]], val+ext1[i])
#
# Remove the -index file
#
					print("Deleting",val+ext)
					os.remove(val+ext)
# 		end of enumerate(ext2)
#
# Remove any other -n files
#
	if args.clean:
		print("Cleaning up any old -n files")
		for j, dash in enumerate(ext3):
			if j != 0:
				try:
					f = open(val+dash)
				except:
					pass
				else:
					f.close()
					print("Deleting",val+dash)
					os.remove(val+dash)
				try:
					f = open(val+"_info"+dash)
				except:
					pass
				else:
					f.close()
					print("Deleting",val+"_info"+dash)
					os.remove(val+"_info"+dash)
		print("Done cleaning:", val,"\n")
# end of enumerate(slots)
#
# Give some time to view the results (when run from an Explorer window)
# (default is 10 seconds)
#
if args.wait:
	time.sleep(args.wait)
else:
	time.sleep(10)