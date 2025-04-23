@echo off
python -m nuitka --standalone --remove-output --windows-console-mode=disable --enable-plugin=tk-inter --windows-icon-from-ico=logo.ico --mingw64  main.py
powershell sleep 3
rename main.dist RunFuse
rename RunFuse\main.exe RunFuse.exe