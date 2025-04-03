def clean():
    from shutil import rmtree
    from os import getlogin
    rmtree(f'C:/Users/{getlogin()}/AppData/Local/Packager')