pyinstaller clean_enshrouded.py -F --noconfirm --clean --version-file clean_enshrouded_version_info.txt
copy dist\clean_enshrouded.exe .
rem pyi-set_version clean_enshrouded_version_info.txt clean_enshrouded.exe
md5 -oclean_enshrouded.md5 clean_enshrouded.exe
