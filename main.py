from sys import argv
from compile import compile, wrap
from decompile import decompile
try:
 if len(argv) > 1:
  if len(argv) > 2:
   if argv[1] == 'compile': compile(argv)
   elif argv[1] == 'wrap': wrap(argv)
   else: decompile(argv)
  else: decompile(argv)
except KeyboardInterrupt:
 exit()
