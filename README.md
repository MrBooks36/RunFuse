# Packaging and Running Python Scripts in a Temporary Folder

## Command Line Usage:
./Packager.exe [compile] [filepath]

Parameters:

[path]: The path of the Python script you wish to package.

[compile]: A flag to indicate whether the script should be compiled (set to compile to compile, else leave empty).

filepath: The path to the directory where the script is located.

Instructions:

Run the command in your terminal:

./Packager.execompile /path/to/your/script/my_script.py

This command will package and compile your_script.py if the compile? flag is compile.

The script will produce a file with the extension .mrb36.

## To execute the packaged file:

Open the generated .mrb36 file with the application. This action will extract the contents to a temporary folder and run the .exe file automatically.

### Example:

./Packager.exe compile /path/to/your/script/my_script.py

This command takes /path/to/my/script/my_script.py, compiles it, packages the compiled script, and creates a my_script.mr file.

By opening the my_script.mr file, the application will unpackage its contents and run the executable in a temporary folder.
