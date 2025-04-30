def decompile(argv):
    try:
        # Setup
        from tarfile import open as opentar
        from wrap import wrap
        from tkinter import Tk, Label, messagebox
        from pathlib import Path
        from shutil import rmtree
        from json import load
        from subprocess import run, call
        from os import getlogin, rename, getcwd, makedirs, chdir
        from os.path import getctime
        from threading import Thread
        from time import sleep
        cwd = getcwd()
        global isload
        isload = 0
        print("Started")

        # Function setup
        def logerror(arg):
            with open(cwd + '\\ERROR.txt', "a") as file:
                file.write(str(arg))
            messagebox.showerror("ERROR!", str(arg))
        print("logerror def")
        def loading():
            root = Tk()
            root.overrideredirect(True)
            root.attributes("-topmost", True)
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width // 2) - (90 // 2)
            y = (screen_height // 2) - (30 // 2)
            root.geometry(f'90x30+{x}+{y}')
            root.resizable(False, False)
            label = Label(root, text="Loading.")
            label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
            def update_label():
                while not isload:
                    for dots in range(1, 4):
                        label.config(text=f"Loading{'.' * dots}")
                        root.update()
                        sleep(0.5)
                root.destroy()
            root.after(0, update_label)
            root.mainloop()
        print("loading def")
        def list_folder_in_tar(tar_file_path):
         # Open the tar file in read mode
         with opentar(tar_file_path, 'r:*') as tar:
          for member in tar:
            # Split the member name into parts to determine its hierarchy
            parts = member.name.split('/')
            
            # Check if the member is effectively a folder without extensions
            if len(parts) > 1 and member.isdir():
                first_folder_name = parts[0]
                return first_folder_name
         # If no folder found, return None
         return None
        print("list_folder_in_tar def")
        # Path setup
        print("Path setup start")
        input_path = Path(argv[1])
        if not input_path.suffix == '.runfuse':
            logerror('Not a runfuse file')
            return
        print('runfuse check')
        if not input_path.is_absolute():
            input_path = input_path.resolve()
        print('full path check')    
        if not input_path.exists():
            logerror(f'File not found: {input_path}')
            return
        print('exists check')        
        temp_dir = Path(f'C:/Users/{getlogin()}/AppData/Local/RunFuse')
        name = list_folder_in_tar(input_path)
        print('tar folder check')
        if not name:
            logerror('Unable to determine folder inside tar archive')
            return
        extracted_dir = temp_dir / name
        folder_name = f"{extracted_dir}{getctime(str(input_path))}"
        if not temp_dir.exists():
            makedirs(temp_dir)
        print("Path setup end")
        # Start the loading animation
        thr = Thread(target=loading)
        thr.setDaemon(True)
        thr.start()
        print('thread started')

        # Extract folder
        print('Extract folder start')
        if not Path(folder_name).exists():
            tar_result = run(f'tar -vxf "{input_path}" -C "{temp_dir}"', shell=True)
            print(tar_result)
            if tar_result.returncode != 0:
                logerror(tar_result.stderr.decode())
                isload = 1
                thr.join()
                return
            rename(extracted_dir, folder_name)
        extracted_dir = Path(folder_name)
        print('Extract folder end')

        # Get config
        print('get config start')
        runtime_file = extracted_dir / 'runtime.json'
        if not runtime_file.exists():
            logerror('runtime.json not found in the extracted files')
            isload = 1
            thr.join()
            return
        with open(runtime_file, 'r') as file:
            data = load(file)
            exe = data.get('exe', '')
            keep = data.get('keep', '')
            rewrap = data.get('rewrap', '')
        print('get config end')
        exe_args = argv[2:]

        # Start EXE
        print('start exe')
        exe_path = extracted_dir / exe
        if exe_path.exists():
            isload = 1
            thr.join()
            try:
                call([str(exe_path)] + exe_args)
            except Exception as e:
                logerror(e)
        else:
            logerror(f'Executable {exe}.exe not found in the extracted files')
            isload = 1
            thr.join()
            return

        # Re-wrap if necessary
        if rewrap:
            args = ["name", "wrap", str(extracted_dir), str(input_path)]
            wrap(args)
            chdir(cwd)
            rmtree(extracted_dir)
        # Clean up
        if not keep and not rewrap:
            rmtree(extracted_dir)

    except Exception as e:
        logerror(str(e))
        isload = 1
        thr.join()