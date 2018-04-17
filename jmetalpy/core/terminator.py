from jmetalpy.core.algorithm.observable import Observer, DefaultObservable
from jmetalpy.core.population import Population


class Terminator(DefaultObservable, Observer):

    def __init__(self):
        super(Terminator, self).__init__()

    def update(self, *args, **kwargs):
        pass

    def apply(self, population: Population) -> float:
        pass

