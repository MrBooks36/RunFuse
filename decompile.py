def decompile(argv):
    from os import getcwd, chdir, system
    from os.path import basename
    from shutil import rmtree
    if 'mrb36' in  argv[1]:
     ogpath = getcwd()
     name = basename(argv[1]).replace('.mrb36', "")
     chdir('C:/Windows/TEMP')
     system(f'tar -xf {argv[1]}')
     chdir(ogpath)
     system(f'C:\\Windows\\TEMP\\{name}\\{name}.exe')
     rmtree(f'C:\\Windows\\TEMP\\{name}')
    else: print('Not a mrb36 file') 