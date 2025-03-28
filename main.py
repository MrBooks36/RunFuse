from sys import argv
from compile import make_mrb36, prep, wrap
from decompile import decompile
try:
 if len(argv) > 1:
  if len(argv) > 2:
   if argv[1] == 'compile': make_mrb36(argv)
   elif argv[1] == 'wrap': wrap(argv)
   else: decompile(argv)
  elif argv[1] == 'prep': prep()
  else: decompile(argv)
except KeyboardInterrupt:
 exit()
