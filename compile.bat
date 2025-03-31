@echo off
del Packager /Q
rmdir Packager /Q
python -m nuitka --follow-imports --standalone --remove-output --mingw64  main.py
rename main.dist Packager
rename Packager\main.exe Packager.exe