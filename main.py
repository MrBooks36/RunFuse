from sys import argv, exit
from platform import system
from wrap import *
from decompile import *
from manage import *

def main():
    if system() != 'Windows':
        print('At the current point in time, this is only available on Windows.')
        exit()

    if len(argv) > 1:
        command = argv[1].lower()
        if command == 'wrap': wrap(argv)
        elif command == 'uninstall': uninstall()
        elif command == 'uninstall2': uninstall2()
        elif command == 'clean': clean()
        else: decompile(argv)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()