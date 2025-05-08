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

#setup 
rmold()