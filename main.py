from PyInstaller.__main__ import run
from os import system, getcwd, path
from sys import argv



run([
    '--onedir',
    '--add-data=data/test.py;.',
    argv[1],
])

name = argv[1].replace('.py', "")

system(f'move "{getcwd()}\\dist\\{name}"  {name}')
system(f'del "{getcwd()}\\{name}.spec"')
system(f'rmdir /s /q "{getcwd()}\\dist"')
system(f'rmdir /s /q "{getcwd()}\\build\\{name}\\localpycs"')
system(f'rmdir /s /q "{getcwd()}\\build\\{name}"')
system(f'rmdir /s /q "{getcwd()}\\build"')
system(f'tar -rf {name}.mrb36 {name}')