@echo off
python -m nuitka --follow-imports --standalone --remove-output --mingw64  main.py
rename "main.dist"/main.exe Packager.exe
rename main.dist Packager