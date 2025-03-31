def compile(argv):
    from shutil import which
    from os import getlogin, system
    if which('Python') == None:
        print('Python is not installed or is not on path')
        return
    if which('Python') == f'C:\\Users\\{getlogin()}\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe':
        print('Not compatible With the Microsoft Store Python version. Please install Python from the official website')
    if not which('PyInstaller') == None: PyIstaller = True
    else: PyIstaller = False
    if not which('nuitka') == None: nuitka = True
    else: nuitka = False
    if not which('py2exe') == None: py2exe = True
    else: py2exe = False
    print('Select Python compiler:')
    if PyIstaller: print('PyInstaller')
    if nuitka: print('Nuitka')
    if py2exe: print('Py2exe')
    pram = input()
    if pram.lower() == 'nuitka': system(f'python -m nuitka --follow-imports --standalone --remove-output --mingw64  {argv[2]}')
    elif pram.lower() == 'pyinstaller': system(f'python -m PyInstaller --onedir {argv[2]}')
    elif pram.lower() == 'py2exe': system(f'python {argv[2]} py2exe')

    
def wrap(argv):
    from tarfile import open as opentar
    from pathlib import Path

    dir_path = Path(argv[2])
    folder_path = Path(dir_path)
    folder_name = folder_path.name
    tar_file_path = Path(f'{folder_name}.mrb36')

    if not dir_path.is_dir():
        print(f"Error: {argv[2]} is not a valid directory.")
        return

    runtime_path = dir_path / 'runtime.json'
    if not runtime_path.exists():
        print(f"Error: runtime.json not found in {dir_path}.")
        return

    try:
        with opentar(tar_file_path, 'w:gz') as tar:
            tar.add(dir_path, arcname=dir_path.name)
        print(f"{tar_file_path} created successfully.")
    except Exception as e:
        print(f"Error: Unable to create mrb36 file {tar_file_path}: {e}")