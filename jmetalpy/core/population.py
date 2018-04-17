from typing import TypeVar

S = TypeVar('S')


class Population(list):

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            list.__init__(self, args[0])
        else:
            list.__init__(self, args)
        self.__dict__.update(kwargs)

    def __new__(cls, *args, **kwargs):
        return super(Population, cls).__new__(cls)

    def __call__(self, **kwargs):
        self.__dict__.update(kwargs)
        return self
