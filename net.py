from random import random
from neuro import Neuro
from link import Link

class Network:
    def __init__(self, *args):
        self.__nlayers = len(args)
        self.__neuros = args
        self.__layers = []

        for i in range(self.__nlayers):
            self.__layers.append( [Neuro([], []) for n in range(self.__neuros[i])] )
        
        for i in range(self.__nlayers):
            for neuro in self.__layers[i]:
                list_in = 0 if i == 0 else [ Link(n_in, neuro, random()) for n_in in self.__layers[i-1] ]
                list_out = 0 if i == self.__nlayers-1 else [ Link(neuro, n_out, random()) for n_out in self.__layers[i+1] ]
                neuro.list_in = list_in
                neuro.list_out = list_out

    def run(self, signal_list):

        for neuro, inp in zip(self.__layers[0], signal_list):
            neuro.__value = neuro.list_in = inp
        
        for i in range(1, self.__nlayers):
            for neuro in self.__layers[i]:
                signal_list = [ (link.neuro_in.__value*link.w) for link in neuro.list_in ]
                neuro.__value = neuro.calculate(sum(signal_list))

    def output(self):
        return [ neuro.__value for neuro in self.__layers[-1] ]
