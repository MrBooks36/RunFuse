# RunFuse

**RunFuse** is a Python-based toolset for wrapping and managing Python projects on Windows. It allows you to package scripts into standalone executables, decompile them when needed, and keep your environment clean by auto-removing old builds.

---

## 🔧 Features

- 📦 **Wrap**  
  Package a Python project into a single distributable archive with optional icon support.

- 🔍 **Decompile**  
  Extracts files from a wrapped executable into a temporary folder and runs the application from there.

- 🧹 **Manage**  
  Automatically removes old packages and clears the temporary folder used during execution or decompilation.

- 🪟 **Windows-only**  
  Designed to run on Windows systems.

---

## 🖥️ Requirements

- Windows OS (required)
- Python 3.10+
- `pip` for managing dependencies
- Admin privileges (for install/uninstall, optional)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MrBooks36/RunFuse.git
cd RunFuse
```

Or [download it as a ZIP](https://github.com/MrBooks36/RunFuse/archive/refs/heads/main.zip) and extract it.

---

## 📚 Usage

### 🔧 Main Entry Point

Run the main script with a command:

```bash
python main.py [command]
```

Available commands:

| Command        | Description                                                |
|----------------|------------------------------------------------------------|
| `wrap <folder>`| Wrap a Python project folder into a single archive         |
| `clean`        | Clean up temporary and old files                           |
| *(filename)*   | Decompile a `.runfuse` file into a temp folder and run it  |

### 📦 Wrap

```bash
python main.py wrap <project_folder>
```

This compresses the folder into a distributable `.runfuse` file. Uses `wrap.py`.

### 🔍 Decompile & Run

```bash
python main.py <yourfile.runfuse>
```

- Extracts the contents to a temporary folder.
- Automatically executes the main script inside.

### 🧹 Clean Up

```bash
python main.py clean
```

- Deletes temporary folders and removes stale packages from previous runs.

---

## 🛠️ Installer/Uninstaller (Optional)

### 📥 Install

```bash
python installer.py <yourfile.runfuse>
```

- Copies the `.runfuse` file into a system location and sets up an environment to run it.

### ❌ Uninstall

```bash
python uninstall.py
```

- Removes the installed `.runfuse` application and its files.

---

## 📁 Project Structure

```
RunFuse/
├── main.py           # Main entry point
├── wrap.py           # Wrap logic
├── decompile.py      # Decompile logic
├── manage.py         # Cleaning and environment management
├── installer.py      # Installer for .runfuse files
├── uninstall.py      # Uninstaller
├── compile.bat       # Batch helper for builds
├── logo.ico          # Optional icon for wrapped apps
├── licence.md        # License
└── .gitignore
```

---

## 📄 License

See `licence.md` for licensing information. This tool is provided as-is, with no guarantees or warranties.

---

## 👤 Author

[MrBooks36](https://github.com/MrBooks36)

---

## 📬 Feedback

Issues and pull requests are welcome. Feel free to suggest improvements or report bugs on the [GitHub Issues page](https://github.com/MrBooks36/RunFuse/issues).
