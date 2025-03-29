@echo off
del Packager.exe
C:\Users\%username%\AppData\Local\Programs\Python\Python312\python.exe -m nuitka --follow-imports --standalone --remove-output --mingw64  main.py
rename "main.dist"/main.exe Packager.exe
rename main.dist Packager