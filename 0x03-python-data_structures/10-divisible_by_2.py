#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    by_2 = []
    for item in my_list:
        if item % 2 == 0:
            by_2.append(True)
        else:
            by_2.append(False)
    return by_2
