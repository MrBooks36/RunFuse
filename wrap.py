def wrap(argv):
    from tarfile import open as opentar
    from pathlib import Path

    dir_path = Path(argv[2])
    folder_path = Path(dir_path)
    folder_name = folder_path.name
    tar_file_path = Path(f'{folder_name}.runfuse')

    if not dir_path.is_dir():
        print(f"Error: {argv[2]} is not a valid directory.")
        input('Press enter to exit')
        return

    runtime_path = dir_path / 'runtime.json'
    if not runtime_path.exists():
        print(f"Error: runtime.json not found in {dir_path}.")
        input('Press enter to exit')
        return

    try:
        with opentar(tar_file_path, 'w:gz') as tar:
            tar.add(dir_path, arcname=dir_path.name)
        print(f"{tar_file_path} created successfully.")
    except Exception as e:
        print(f"Error: Unable to create runfuse file {tar_file_path}: {e}")
        input('Press enter to exit')