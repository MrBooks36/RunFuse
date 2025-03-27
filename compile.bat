@echo off
del Packager.exe
C:\Users\%username%\AppData\Local\Programs\Python\Python312\python.exe -m nuitka --onefile --standalone --remove-output --mingw64  main.py
rename main.exe Packager.exe