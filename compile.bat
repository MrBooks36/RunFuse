@echo off
del RunFuse /Q
rmdir RunFuse /Q
python -m nuitka --follow-imports --standalone --remove-output --windows-console-mode=attach --enable-plugin=tk-inter --windows-icon-from-ico=logo.ico --mingw64  main.py
rename main.dist RunFuse
rename RunFuse\main.exe RunFuse.exe