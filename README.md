# CleanEnshrouded
Clean the Saved Games Enshrouded directory by assuring the base world files are the most recent and 
removing all the other world files.

This is a Python3 program and a Python3 installation is needed if you wish to use the .py file. 
An executable file is provided so a Python3 installation is not needed.

## Command line options
```
usage: clean_enshrouded.exe [-h] [-b] [-p] [-c] [-w WAIT] [-d DIRECTORY]

V1.0 - Clean Enshrouded world file directory.

options:
  -h, --help            show this help message and exit
  -b, --backup          backup all the world files first (using 7z)
  -p, --powershell      backup all the world files first (using powershell)
  -c, --clean           remove all but the base world files
  -w WAIT, --wait WAIT  wait N seconds before exiting
  -d DIRECTORY, --directory DIRECTORY
                        directory to process
```

## Recommendations

By default (i.e. no switches on the command line), the program just analyzes the current directory and exits. 
A `-c` on the command line is needed to actually process the directory. Enshrouded should not be running while
using this program.

While a copy of the program can be placed in the same location as the world files, it can be installed in one location and 
one (or more) shortcut(s) can be created. The `Target:` can be edited to add command line switches (from above) and 
the `Start in:` can be edited to the location of the world save files.

It is recommended to make a backup first. The program will first create a `backup.zip` file in the current directory 
if `-b` or `-p` command line switches are present. The `-b` switch uses the program 7-zip, https://www.7-zip.org/ and 
the `-p` switch uses PowerShell. The `backup.zip` only contains the world files.

The program output is sent to a console window. If started from an Explorer window (or a shortcut), 
this console window will close when the program exits. 
A "sleep" for 10 seconds before exiting allows some time for the output to be read and 
this time can be changed with the `-w` switch.

The `-d` switch is optional and if present, the program will switch to that directory before processing begins.

## Cautions

This program has not been tested on the directory used by Enshrouded Dedicated Servers.

This program has not been tested on the directory used when Steam Cloud saves are enabled and
there is a chance that data corruption and/or a loss of worlds could happen. 

It has been tested on a copy of the Steam Cloud save directory.
