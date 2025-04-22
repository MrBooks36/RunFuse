def clean():
    from shutil import rmtree
    from os import getlogin
    rmtree(f'C:/Users/{getlogin()}/AppData/Local/Packager')

def rmold():
    import os
    import shutil
    import time
    if not os.path.exists(f'C:/Users/{os.getlogin()}/AppData/Local/Packager'):
        return
    current_time = time.time()
    duration_seconds = 30 * 86400  # Convert days to seconds

    for folder_name in os.listdir(f'C:/Users/{os.getlogin()}/AppData/Local/Packager'):
        folder_path = os.path.join(f'C:/Users/{os.getlogin()}/AppData/Local/Packager', folder_name)

        if os.path.isdir(folder_path):
            folder_time = os.path.getmtime(folder_path)
            folder_age = current_time - folder_time

            if folder_age > duration_seconds:
                try:
                    shutil.rmtree(folder_path)
                    print(f"Deleted folder: {folder_path}")
                except Exception as e:
                    print(f"Error deleting folder {folder_path}: {e}")


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



#setup 
rmold()