#!/usr/bin/python3
""" This is module 7-base_geometry.py """


class BaseGeometry():
    """ This class has two methods: area() and interger_validator() """
    def area(self):
        """ area methon; not implemented """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ valitated the 'value' variable to be integer """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
