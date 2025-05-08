@echo off
del RunFuse.exe
python -m nuitka --standalone --onefile --remove-output --enable-plugin=tk-inter --windows-icon-from-ico=logo.ico --mingw64  main.py
powershell sleep 3
rename main.exe RunFuse.exe

python -m nuitka --standalone --onefile --remove-output --windows-console-mode=disable --windows-uac-admin --windows-icon-from-ico=logo.ico --mingw64  uninstall.py

tar -vcjf RunFuse.tar RunFuse.exe uninstall.exe

python -m nuitka --standalone --onefile --remove-output --enable-plugin=tk-inter --windows-console-mode=disable --windows-uac-admin --include-data-files=RunFuse.tar=RunFuse.tar --windows-icon-from-ico=logo.ico --mingw64  installer.py

del uninstall.exe
del RunFuse.exe
del RunFuse.tar
del main.exe