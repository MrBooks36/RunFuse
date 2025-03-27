def make_mrb36(argv):
    from os import system
    from os.path import basename, splitext
    name = basename(argv[2])
    system(f'tar -czf {name}.mrb36 {argv[2]}')