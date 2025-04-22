@echo off
del RunFuse /Q
rmdir RunFuse /Q
python -m nuitka --follow-imports --standalone --remove-output --windows-console-mode=attach --mingw64  main.py
rename main.dist RunFuse
rename RunFuse\main.exe RunFuse.exe