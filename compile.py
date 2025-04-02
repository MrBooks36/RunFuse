def compile(argv):
 if len(argv) >= 3:
    from shutil import which
    from os import getlogin, system
    if which('Python') == None:
        print('Python is not installed or is not on path')
        input('Press enter to exit')
        return
    if which('Python') == f'C:\\Users\\{getlogin()}\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe':
        print('Compile is not compatible With the Microsoft Store Python version. Please install Python from the official website to use compile')
        input('Press enter to exit')
    if not which('PyInstaller') == None: PyIstaller = True
    else: PyIstaller = False
    if not which('nuitka') == None: nuitka = True
    else: nuitka = False
    if not which('py2exe') == None: py2exe = True
    else: py2exe = False
    if not len(argv) == 4:
     print('Select Python compiler:')
     if PyIstaller: print('PyInstaller')
     if nuitka: print('Nuitka')
     if py2exe: print('Py2exe')
     pram = input()
    else: pram = argv[3]
    if pram.lower() == 'nuitka' and nuitka: system(f'python -m nuitka --follow-imports --standalone --remove-output --mingw64  {argv[2]}')
    elif pram.lower() == 'pyinstaller' and PyIstaller: system(f'python -m PyInstaller --onedir {argv[2]}')
    elif pram.lower() == 'py2exe' and py2exe: system(f'python -m py2exe -d {argv[2]}')
    else: print(f'Invalid Input: {pram}')

    
def wrap(argv):
    from tarfile import open as opentar
    from pathlib import Path

    dir_path = Path(argv[2])
    folder_path = Path(dir_path)
    folder_name = folder_path.name
    tar_file_path = Path(f'{folder_name}.mrb36')

    if not dir_path.is_dir():
        print(f"Error: {argv[2]} is not a valid directory.")
        input('Press enter to exit')
        return

    runtime_path = dir_path / 'runtime.json'
    if not runtime_path.exists():
        print(f"Error: runtime.json not found in {dir_path}.")
        input('Press enter to exit')
        return

    try:
        with opentar(tar_file_path, 'w:gz') as tar:
            tar.add(dir_path, arcname=dir_path.name)
        print(f"{tar_file_path} created successfully.")
    except Exception as e:
        print(f"Error: Unable to create mrb36 file {tar_file_path}: {e}")
        input('Press enter to exit')