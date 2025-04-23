def clean():
    from shutil import rmtree
    from os import getlogin
    rmtree(f'C:/Users/{getlogin()}/AppData/Local/RunFuse')

def rmold():
    import os
    import shutil
    import time
    if not os.path.exists(f'C:/Users/{os.getlogin()}/AppData/Local/RunFuse'):
        return
    current_time = time.time()
    duration_seconds = 30 * 86400  # Convert days to seconds

    for folder_name in os.listdir(f'C:/Users/{os.getlogin()}/AppData/Local/RunFuse'):
        folder_path = os.path.join(f'C:/Users/{os.getlogin()}/AppData/Local/RunFuse', folder_name)

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
    from os import system
    from os.path import dirname, abspath, exists
    from sys import argv
    from shutil import rmtree, copytree

    script_directory = dirname(abspath(argv[0]))
    if exists("C:\\Windows\\TEMP\\RunFuse"): rmtree("C:\\Windows\\TEMP\\RunFuse")
    copytree(script_directory, "C:\\Windows\\TEMP\\RunFuse")
    file = open("C:\\Windows\\TEMP\\temp.asdf", "w")
    file.write(script_directory)
    system('start cmd /c C:\\Windows\\TEMP\\RunFuse\\Runfuse.exe uninstall2')

def uninstall2():
        from shutil import rmtree
        from time import sleep
        file = open("C:\\Windows\\TEMP\\temp.asdf", "r")
        path = file.read()
        sleep(3)
        rmtree(path)
        return

#setup 
rmold()