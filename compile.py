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
        print('runtime args not found!')
        return

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
  name = input('File name: ')
  name = name.replace('.py', "")
  content = f'''
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['{name}.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={'{}'},
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
'''
  with open(name+'.spec', 'w') as file:
    file.write(content)

def wrap():
  from os import system
  from sys import argv
  system(f'tar -rzf wrap.mrb36 {argv[2]}')
