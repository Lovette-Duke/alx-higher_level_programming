#!/usr/bin/python3
for value in range(122, 96, -1):
    c = value
    if (value % 2) == 1:
        c -= 32
    print('{:s}'.format(chr(c)), end='')
