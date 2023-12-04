#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        _max = my_list[0]
        for i, d in enumerate(my_list):
            if d > _max:
                _max = d
        return _max
