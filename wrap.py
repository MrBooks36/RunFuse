def wrap(argv):
    try:
        #Setup
        from subprocess import run
        from os import chdir, getcwd
        from pathlib import Path
        from time import sleep
        from threading import Thread
        from tkinter import Tk, Label, messagebox
        cwd = getcwd()
        isload = 0

        # Function setup
        def logerror(arg):
            with open(cwd+'\\ERROR.txt', "w") as file:
                file.write(arg)
            messagebox.showerror("ERROR!", str(arg))
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

            if isload != 2:
                messagebox.showinfo("Done!", f"{tar_file_path} created successfully.")
            root.destroy()
        
        #File Checks
        try:
            dir_path = Path(argv[2])
            if not dir_path.is_dir():
                logerror(f"Error: {argv[2]} is not a valid directory.")
                return
            runtime_path = dir_path / 'runtime.json'
            if not runtime_path.exists():
                logerror(f"Error: runtime.json not found in {dir_path}.")
                return
        except IndexError:
            logerror("Error: Missing directory argument.")
            return
        #Path setup
        folder_name = dir_path.name
        output_tar_path = argv[3] if len(argv) >= 4 else f"{folder_name}.runfuse"
        tar_file_path = Path(cwd) / output_tar_path

        try:
            thr = None
            if len(argv) < 4:
                thr = Thread(target=loading)
                thr.start()

            chdir(dir_path.parent)
            tar_command = ['tar', '-vczf', str(tar_file_path), folder_name]

            # Use subprocess to handle the tar command
            result = run(tar_command, shell=True)
            chdir(cwd)
            if result.returncode != 0:
                logerror(f"Tar command failed: {result.stderr}")
                isload = 2
                return

            if thr:
                isload = 1
                thr.join()
            if len(argv) >= 4:
                print(f"{tar_file_path} created successfully.")

        except Exception as e:
            logerror(f"Error: Unable to create runfuse file {tar_file_path}: {e}")
            isload = 2
    except Exception as e:
        logerror(str(e))