# CleanEnshrouded
Clean the Saved Games Enshrouded directory by assuring the base world files are the most recent and removing all the other world files.

A Python3 installation is needed if you wish to use the .py file. Alternatively, an executable file is provided in the dist directory.

It is recommended to run the program from a command window. The program processes files in the current directory. It is recommended to make a backup first.

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
