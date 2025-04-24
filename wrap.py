def wrap(argv):
 try:
    from os import chdir, getcwd, system
    from pathlib import Path
    from time import sleep
    from threading import Thread
    from tkinter import Tk, Label, messagebox
    def logerror(arg):
       with open('ERROR.txt', "w") as file:
          file.write(arg)
    isload = 0
    def loading():
        root = Tk()
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.title("Infinite Parkour - Pack Manager")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
    
        # Calculate position x and y coordinates
        x = (screen_width // 2) - (90 // 2)
        y = (screen_height // 2) - (30 // 2)
    
        # Set the dimensions and position of the window
        root.geometry(f'90x30+{x}+{y}')
        root.resizable(False, False)
        label = Label(root, text="Loading.")
        label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        root.update()
        while not isload:
           label.config(text="Loading.")
           root.update()
           sleep(0.5)
           label.config(text="Loading..")
           root.update()
           sleep(0.5)
           label.config(text="Loading...")
           root.update()
           sleep(0.5)
        if not isload == 2:
         messagebox.showinfo("Done!",f"{tar_file_path} created successfully.")
        return

    dir_path = Path(argv[2])
    folder_path = Path(dir_path)
    folder_name = folder_path.name
    tar_file_path = Path(f'{getcwd()}\\{folder_name}.runfuse')

    if not dir_path.is_dir():
        logerror(f"Error: {argv[2]} is not a valid directory.")
        return

    runtime_path = dir_path / 'runtime.json'
    if not runtime_path.exists():
        logerror(f"Error: runtime.json not found in {dir_path}.")
        return

    try:
        thr = Thread(target=loading)
        thr.start()
        chdir(folder_path.parent) 
        tar = system(f'tar -vczf {tar_file_path} {folder_name}')
        if tar != 0:
           logerror("Tar Error")
           isload = 2
           return
        print(f"{tar_file_path} created successfully.")
        isload = 1
        thr.join()
    except Exception as e:
        logerror(f"Error: Unable to create runfuse file {tar_file_path}: {e}")
 except Exception as e:
    logerror(str(e))
    isload = 2