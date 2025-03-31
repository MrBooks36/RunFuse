from platform import system
if not system() == 'Windows':
 print('At the current point in time this is only available on Windows')
 input('Press enter to exit')
 exit()
from sys import argv
from compile import compile, wrap
from decompile import decompile
def uninstall():
    import os
    current_script_path = os.path.abspath(__file__)
    print('Delete This Folder:'+os.path.dirname(current_script_path))
try:
 if len(argv) > 1:
  if len(argv) > 2:
   if argv[1] == 'compile': compile(argv)
   elif argv[1] == 'wrap': wrap(argv)
   else: decompile(argv)
  elif argv[1] == 'uninstall': uninstall()
  else: decompile(argv)
except KeyboardInterrupt:
 exit()
