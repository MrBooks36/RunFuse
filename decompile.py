def decompile(argv):
    try:
        from tarfile import open as opentar
        from wrap import wrap
        from tkinter import Tk, Label, messagebox
        from pathlib import Path
        from shutil import rmtree
        from json import load
        from subprocess import run
        from os import getlogin, rename, getcwd, makedirs, chdir
        from os.path import getctime
        from threading import Thread
        from time import sleep

        cwd = getcwd()

        def logerror(arg):
            with open(cwd + '\\ERROR.txt', "w") as file:
                file.write(str(arg))
            messagebox.showerror("ERROR!", str(arg))

        isload = 0

        if '.runfuse' not in argv[1]:
            logerror('Not a runfuse file')
            return

        input_path = Path(argv[1])
        if not input_path.is_absolute():
            input_path = input_path.resolve()
        if not input_path.exists():
            logerror(f'File not found: {input_path}')
            return

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
            while not isload:
                for dots in range(1, 4):
                    label.config(text=f"Loading{'.' * dots}")
                    root.update()
                    sleep(0.5)
            root.destroy()

        def list_folder_in_tar(tar_path):
            folders = []
            with opentar(tar_path, 'r') as tar:
                for member in tar.getmembers():
                    if member.isdir():
                        folders.append(member.name)
            return folders[0] if folders else None

        temp_dir = Path(f'C:/Users/{getlogin()}/AppData/Local/RunFuse')
        name = list_folder_in_tar(input_path)
        if not name:
            logerror('Unable to determine folder inside tar archive')
            return
        extracted_dir = temp_dir / name
        folder_name = str(extracted_dir) + str(getctime(str(input_path)))

        if not temp_dir.exists():
            makedirs(temp_dir)

        # Start the loading animation
        thr = Thread(target=loading)
        thr.start()

        if not Path(folder_name).exists():
            tar_result = run(f'tar -xf "{input_path}" -C "{temp_dir}"', shell=True, capture_output=True, text=True)
            if tar_result.returncode != 0:
                logerror(tar_result.stderr)
                isload = 1
                return
            rename(extracted_dir, folder_name)

        extracted_dir = Path(folder_name)
        runtime_file = extracted_dir / 'runtime.json'

        if not runtime_file.exists():
            logerror('runtime.json not found in the extracted files')
            isload = 1
            return

        with open(runtime_file, 'r') as file:
            data = load(file)
            exe = data.get('exe', '')
            exe_name = Path(exe).stem if exe else name
            keep = data.get('keep', '')
            rewrap = data.get('rewrap', '')

        exe_args = argv[2:]  # Collect additional arguments

        exe_path = extracted_dir / exe
        if exe_path.exists():
            isload = 1
            thr.join()
            try:
                run([str(exe_path)] + exe_args, check=True)
            except Exception as e:
                logerror(e)
        else:
            logerror(f'Executable {exe_name}.exe not found in the extracted files')
            isload = 1
            return

        # Re-wrap if necessary
        if rewrap:
            args = ["name", "wrap", str(extracted_dir), str(input_path)]
            wrap(args)
            chdir(cwd)
            rmtree(extracted_dir)

        if not keep and not rewrap:
            rmtree(extracted_dir)

    except Exception as e:
        logerror(str(e))
        isload = 1