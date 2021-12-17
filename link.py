class Link:
    def __init__(self, neuro_in, neuro_out, w = 0):
        self.__in = neuro_in
        self.__out = neuro_out
        self.__w = w

    @property
    def neuro_in(self):
        return self.__in

    @property
    def neuro_out(self):
        return self.__in

    @property
    def w(self):
        return self.__w
