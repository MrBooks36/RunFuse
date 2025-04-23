def decompile(argv):
 try:   
    from tarfile import open as opentar
    from tkinter import Tk, Label
    from pathlib import Path
    from shutil import rmtree
    from json import load
    from subprocess import call
    from os import getlogin, rename, remove, system
    from os.path import getctime
    from threading import Thread
    from time import sleep
    def logerror(arg):
       with open('ERROR.txt', "w") as file:
          file.write(arg)
    isload = 0
    if '.runfuse' not in argv[1]:
        logerror('Not a runfuse file')
        return
    input_path = Path(argv[1])
    if not input_path.is_absolute():
        input_path = input_path.resolve()
    if not Path.exists(input_path):
        logerror(f'File not found: {input_path}')
        return
    
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
        return

    temp_dir = Path(f'C:/Users/{getlogin()}/AppData/Local/RunFuse')
    name = input_path.stem
    extracted_dir = temp_dir / name
    runtime_file = extracted_dir / 'runtime.json'
    folder_name = str(extracted_dir) + str(getctime(str(input_path)))


    thr = Thread(target=loading)
    thr.start()


    # Extract tar file
    if not Path(folder_name).exists():
     system(f"tar -vxf {input_path} -C {temp_dir}")
     rename(extracted_dir, folder_name)
    else:
     with opentar(input_path, 'r:gz') as tar:
      tar.extract(name+'/runtime.json',path=temp_dir)
      tar.close
      remove(folder_name+'/runtime.json')
      rename(extracted_dir / 'runtime.json', folder_name+'/runtime.json') 
      rmtree(extracted_dir)
    
    extracted_dir = Path(folder_name)
    runtime_file = extracted_dir / 'runtime.json'


    if not runtime_file.exists():
        logerror('runtime.json not found in the extracted files')
        isload = 1
        return

    # Read the runtime.json file
    with open(runtime_file, 'r') as file:
        data = load(file)
        exe = data.get('exe', '')
        exe_name = Path(exe).stem if exe else name
        keep = data.get('keep', '')
    
    # Collect additional arguments to pass to the executable
    exe_args = argv[2:]  # Skip the script name and the first argument which is the path to the file

    # Run the executable with additional arguments
    exe_path = extracted_dir / exe
    if exe_path.exists():
        isload = 1
        thr.join()
        system('cls')
        try:
         call([str(exe_path)] + exe_args)
        except Exception as e:
           logerror(e) 
    else:
        logerror(f'Executable {exe_name}.exe not found in the extracted files')
        isload = 1
        return

    # Clean up
    if not keep:
     rmtree(extracted_dir)

 except Exception as e:
    logerror(str(e))
    isload = 1 