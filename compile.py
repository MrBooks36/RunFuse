def make_mrb36(argv):
    from PyInstaller.__main__ import run
    from pathlib import Path
    from shutil import rmtree, copy2, move
    from tarfile import open as opentar

    current_dir = Path.cwd()
    script_path = Path(argv[2])
    name = script_path.stem
    runtime_path = script_path.parent / 'runtime.json'

    print(runtime_path)

    if not runtime_path.exists():
        print('Runtime args not found! Generating now...')
        with open(runtime_path, 'w') as file:
            file.write({
                "exe":f"{name}.exe"
            })

    if script_path.suffix != '.py':
        print('Expected a Python script file (.py)')
        return

    output_dir = current_dir / name

    if output_dir.exists():
        rmtree(output_dir)

    # Determine if we need to run pyinstaller with spec or not
    spec_file = current_dir / f'{name}.spec'
    if not spec_file.exists():
        run([str(script_path), '--noconfirm'])
        remove_spec = True
    else:
        run([str(spec_file), '--noconfirm'])
        remove_spec = False

    # Move the generated directory
    dist_dir = current_dir / 'dist' / name
    move(str(dist_dir), str(output_dir))

    # Cleanup
    rmtree(current_dir / 'dist')
    rmtree(current_dir / 'build')
    
    if remove_spec and spec_file.exists():
        spec_file.unlink()

    # Copy runtime file
    copy2(runtime_path, output_dir)

    # Create tar archive
    with opentar(f'{name}.mrb36', 'w') as tar:
        tar.add(output_dir, arcname=name)

    rmtree(output_dir)


def prep():
    from pathlib import Path
    # Get the file name from the user input
    filename = input('File name (with .py extension): ').strip()
    
    # Validate the input to ensure it ends with .py extension
    if not filename.endswith('.py'):
        print("Error: The file name should end with .py")
        return

    # Create the name without the .py extension
    name = Path(filename).stem
    
    # Create the content for the spec file using a template string
    content = f"""
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['{name}.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='{name}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='{name}',
)
"""
    # Define the path for the .spec file
    spec_file_path = Path(f"{name}.spec")
    
    try:
        # Write the content to the .spec file
        with spec_file_path.open('w') as file:
            file.write(content)
        print(f"Spec file '{spec_file_path}' created successfully.")
    except IOError as e:
        print(f"Error: Unable to write to file {spec_file_path}: {e}")

def wrap(argv):
    from tarfile import open as opentar
    from pathlib import Path

    dir_path = Path(argv[2])
    folder_path = Path(dir_path)
    folder_name = folder_path.name
    tar_file_path = Path(f'{folder_name}.mrb36')

    if not dir_path.is_dir():
        print(f"Error: {argv[2]} is not a valid directory.")
        return

    runtime_path = dir_path / 'runtime.json'
    if not runtime_path.exists():
        print(f"Error: runtime.json not found in {dir_path}.")
        return

    try:
        with opentar(tar_file_path, 'w:gz') as tar:
            tar.add(dir_path, arcname=dir_path.name)
        print(f"{tar_file_path} created successfully.")
    except Exception as e:
        print(f"Error: Unable to create mrb36 file {tar_file_path}: {e}")