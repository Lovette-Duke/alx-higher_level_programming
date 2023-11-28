#!/usr/bin/python3
def print_last_digit(number):
    last_int = abs(number) % 10
    print(f'{last_int}', end='')
    return last_int
