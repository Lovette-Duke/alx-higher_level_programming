#!/usr/bin/python3
from sys import argv

n_args = len(argv[1:])

if n_args == 1:
    print('1 argument:')
else:
    print('{:d} arguments{:s}'.format(n_args, '.' if n_args == 0 else ':'))

for arg in range(1, n_args + 1):
    print('{:d}: {}'.format(arg, argv[arg]))
