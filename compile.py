def make_mrb36(argv):
    from PyInstaller.__main__ import run
    from os import system, getcwd, path
    from shutil import rmtree
    name = argv[2].replace('.py', "")
    if path.exists(name):
     rmtree(name)

    if not path.exists(name+'.spec'):
     run([name+'.py','--noconfirm'])

    run([name+'.spec','--noconfirm'])

    system(f'move "{getcwd()}\\dist\\{name}"  {name}')
    rmtree(f'{getcwd()}\\dist')
    rmtree(f'{getcwd()}\\build')

    system(f'tar -rf {name}.mrb36 {name}')
    rmtree(name)