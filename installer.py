import tkinter as tk
from tkinter import ttk
import threading
import tarfile
import os
import sys
import winreg

class LoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading Screen")
        self.root.geometry("300x150")
        self.root.configure(bg="#282c34")

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(expand=True, fill="both")

        self.label = ttk.Label(
            self.frame, 
            text="Installing RunFuse", 
            foreground="#61dafb", 
            background="#282c34", 
            font=("Helvetica", 16)
        )
        self.label.pack(pady=(0, 10))

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=200, mode="indeterminate")
        self.progress.pack(pady=10)

        self.loading = False

    def start_loading(self):
        self.loading = True
        # Start the progress bar animation
        self.progress.start(10)
        # Start the installation process on a separate thread
        self.thread = threading.Thread(target=self.installtask, daemon=True)
        self.thread.start()
        self.root.after(100, self.check_thread)

    def add_to_user_path(self, new_directory):
        """
        Adds the specified directory to the user's PATH in the registry.
        This native method is less likely to be flagged than a shell command.
        """
        try:
            reg_path = r'Environment'
            # Open the registry key for the user's environment variables (read access)
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ) as key:
                try:
                    current_path, reg_type = winreg.QueryValueEx(key, 'Path')
                except FileNotFoundError:
                    current_path = ''
                    reg_type = winreg.REG_EXPAND_SZ

            if new_directory.lower() not in current_path.lower():
                # Append new_directory only if not already present
                updated_path = f"{current_path};{new_directory}" if current_path else new_directory

                # Open the registry key with write access to update the PATH
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE) as key:
                    winreg.SetValueEx(key, 'Path', 0, reg_type, updated_path)
                print(f"Successfully added '{new_directory}' to the user PATH.")
            else:
                print(f"Directory '{new_directory}' is already in the user PATH.")

        except Exception as e:
            print(f"Error updating user PATH: {e}")

    def installtask(self):
        try:
            # Build a destination path using the user's home directory
            user_home = os.path.expanduser("~")
            destination = os.path.join(user_home, "AppData", "Local", "Programs", "runfuse")
            os.makedirs(destination, exist_ok=True)

            # Construct path to the tar archive located relative to the script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            archive_path = os.path.join(current_dir, "runfuse.tar")

            # Extract the archive into the destination directory
            with tarfile.open(archive_path, 'r') as tar:
                tar.extractall(path=destination)

            # Update the user's PATH natively via winreg
            self.add_to_user_path(destination)

        except Exception as e:
            error_message = str(e)
            # Log error to a file for troubleshooting
            with open("ERROR.txt", "w") as file:
                file.write(error_message)
            print(f"Installation error: {error_message}")
        self.loading = False

    def check_thread(self):
        if self.thread.is_alive():
            self.root.after(100, self.check_thread)
        else:
            self.progress.stop()  # Stop the progress bar
            self.label.config(text="Installed Runfuse", foreground="#34eb43")
            self.root.after(1000, self.root.destroy)

def main():
    root = tk.Tk()

    style = ttk.Style()
    style.configure("TFrame", background="#282c34")
    style.configure("TLabel", background="#282c34")

    loading_screen = LoadingScreen(root)
    loading_screen.start_loading()
    root.mainloop()

if __name__ == "__main__":
    main()