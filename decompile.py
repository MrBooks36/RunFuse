def decompile(argv):
    import tarfile
    from pathlib import Path
    from shutil import rmtree
    from json import load
    from subprocess import call
    if '.mrb36' not in argv[1]:
        print('Not a mrb36 file')
        return
    input_path = Path(argv[1])
    if not input_path.is_absolute():
        input_path = input_path.resolve()
    if not Path.exists(input_path):
        print(f'File not found: {input_path}')
        return
    temp_dir = Path('C:/Windows/TEMP')

    name = input_path.stem
    extracted_dir = temp_dir / name

    # Extract tar file
    with tarfile.open(input_path, 'r') as tar:
        tar.extractall(path=temp_dir)

    runtime_file = extracted_dir / 'runtime.json'

    if not runtime_file.exists():
        print('runtime.json not found in the extracted files')
        return

    # Read the runtime.json file
    with open(runtime_file, 'r') as file:
        exe = load(file).get('exe', '')
        exe_name = Path(exe).stem if exe else name
    
    # Collect additional arguments to pass to the executable
    exe_args = argv[2:]  # Skip the script name and the first argument which is the path to the tar file

    # Run the executable with additional arguments
    exe_path = extracted_dir / f'{exe_name}.exe'
    if exe_path.exists():
        call([str(exe_path)] + exe_args)
    else:
        print(f'Executable {exe_name}.exe not found in the extracted files')

    # Clean up
    rmtree(extracted_dir)
