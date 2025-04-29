import tkinter as tk
from tkinter import ttk
import threading
from tarfile import open as opentar
from os import getlogin, system
from sys import argv
if len(argv) == 2:
    system('python -m nuitka --standalone --onefile --remove-output --windows-console-mode=disable --enable-plugin=tk-inter --include-data-files=runfuse.tar=runfuse.tar --windows-icon-from-ico=logo.ico --mingw64  installer.py')
    exit()
class LoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading Screen")
        self.root.geometry("300x150")
        self.root.configure(bg="#282c34")

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(expand=True, fill="both")

        self.label = ttk.Label(self.frame, text="Installing RunFuse", foreground="#61dafb", background="#282c34", font=("Helvetica", 16))
        self.label.pack(pady=(0, 10))

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=200, mode="indeterminate")
        self.progress.pack(pady=10)

        self.loading = False

    def start_loading(self):
        self.loading = True
        # Start the indeterminate mode of the progress bar, showing continuous animation
        self.progress.start(10)  # Speed up progress bar animation
        self.thread = threading.Thread(target=self.installtask)
        self.thread.start()
        self.root.after(100, self.check_thread)  # Checking status of the thread periodically

    def installtask(self):
     with opentar("runfuse.tar", 'r') as tar:
            tar.extractall(path=f"C:/Users/{getlogin()}/AppData/Local/Programs", filter='fully_trusted')
     
     self.loading = False

    def check_thread(self):
        if self.thread.is_alive():
            self.root.after(100, self.check_thread)
        else:
            self.progress.stop()  # Stop the progress bar
            self.label.config(text="Installed Runfuse", foreground="#34eb43")
            self.root.after(1000, self.root.destroy)  # Delay and then destroy the window

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.configure("TFrame", background="#282c34")
    style.configure("TLabel", background="#282c34")

    loading_screen = LoadingScreen(root)

    # Start the loading screen
    loading_screen.start_loading()

    root.mainloop()

if __name__ == "__main__":
    main()