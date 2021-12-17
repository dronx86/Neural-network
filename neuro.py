from math import exp

class NeuroMovement:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

class Neuro:
    list_in = NeuroMovement()
    list_out = NeuroMovement()

    def __init__(self, list_in, list_out):
        self.list_in = list_in
        self.list_out = list_out
        self.__value = 0

    def calculate(self, x):
        return 1/(1+exp(-x))
