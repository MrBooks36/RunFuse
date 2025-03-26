from sys import argv
from compile import make_mrb36
from decompile import decompile

if len(argv) > 1:
 if len(argv) > 2:
  if argv[1] == 'compile':
   make_mrb36(argv)
 else:
  decompile(argv)