def decompile(argv):
    from tarfile import open as opentar
    import ctypes
    from pathlib import Path
    from shutil import rmtree
    from json import load
    from subprocess import call
    from os import getlogin, rename, remove, system
    from os.path import getctime
    from threading import Thread
    from time import sleep
    isload = 0
    if '.mrb36' not in argv[1]:
        print('Not a mrb36 file')
        input('Press enter to exit')
        return
    input_path = Path(argv[1])
    if not input_path.is_absolute():
        input_path = input_path.resolve()
    if not Path.exists(input_path):
        print(f'File not found: {input_path}')
        input('Press enter to exit')
        return
    
    def loading():
       while not isload:
        if not isload: 
         print('Loading.')
         sleep(0.5)
        if not isload:  
         system('cls')
         print('Loading..')
         sleep(0.5)
         system('cls')
        if not isload: 
         print('Loading...')
         sleep(0.5)
         system('cls')
       return    


    temp_dir = Path(f'C:/Users/{getlogin()}/AppData/Local/Packager')
    name = input_path.stem
    extracted_dir = temp_dir / name
    runtime_file = extracted_dir / 'runtime.json'
    folder_name = str(extracted_dir) + str(getctime(str(input_path)))


    thr = Thread(target=loading)
    thr.start()


    # Extract tar file
    with opentar(input_path, 'r') as tar:
     if not Path(folder_name).exists():
      tar.extractall(path=temp_dir)
      tar.close
      rename(extracted_dir, folder_name)
     else:
        tar.extract(name+'/runtime.json',path=temp_dir)
        tar.close
        remove(folder_name+'/runtime.json')
        rename(extracted_dir / 'runtime.json', folder_name+'/runtime.json') 
        rmtree(extracted_dir)
    
    extracted_dir = Path(folder_name)
    runtime_file = extracted_dir / 'runtime.json'


    if not runtime_file.exists():
        print('runtime.json not found in the extracted files')
        input('Press enter to exit')
        isload = 1
        return

    # Read the runtime.json file
    with open(runtime_file, 'r') as file:
        data = load(file)
        exe = data.get('exe', '')
        exe_name = Path(exe).stem if exe else name  # Replace 'name' with an appropriate default name or variable
        keep = data.get('keep', '')
        hide = data.get('hide', '')
    
    # Collect additional arguments to pass to the executable
    exe_args = argv[2:]  # Skip the script name and the first argument which is the path to the tar file

    # Run the executable with additional arguments
    exe_path = extracted_dir / exe
    if hide:
       hwnd = ctypes.windll.kernel32.GetConsoleWindow()
       ctypes.windll.user32.ShowWindow(hwnd, 0)
       system(f'taskkill /f /im cmd.exe')
    if exe_path.exists():
        isload = 1
        thr.join()
        system('cls')
        call([str(exe_path)] + exe_args)
    else:
        print(f'Executable {exe_name}.exe not found in the extracted files')
        input('Press enter to exit')
        isload = 1
        return

    # Clean up
    if not keep:
     rmtree(extracted_dir)

def uninstall():
    from os import chdir, getlogin
    from os.path import dirname, exists
    from sys import exit
    from subprocess import Popen
    current_script_path = dirname(__file__)
    if not exists(current_script_path+'/python312.dll'):
       print("cannnot uninstall in portable mode")
       input('Press enter to exit')
       return
    chdir(f'C:\\Users\\{getlogin()}\\AppData\\Local')
    with open('del.bat', 'w') as file:
      file.write('''
@echo off
powershell sleep 1
echo ..
echo This script will now delete itself.
echo Done! Press Enter to exit. The error below is ok.
rmdir /s /Q %*
del "%~f0"
                 ''')
      file.close()
      Popen(["del.bat", current_script_path])
      exit()
