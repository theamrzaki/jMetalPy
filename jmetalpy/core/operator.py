from typing import TypeVar

from jmetalpy.core.algorithm.observable import DefaultObservable, Observer, Observable

S = TypeVar('S')
R = TypeVar('R')


class Operator(DefaultObservable, Observer):

    def __init__(self):
        super(Operator, self).__init__()
        self.observable: Observable = DefaultObservable()

    def execute(self, source: S) -> R:
        pass

    def update(self, *args, **kwargs):
        pass

    def get_name(self):
        pass


class Mutation:

    def __init__(self, probability: float):
        super(Mutation, self).__init__()
        if probability > 1.0:
            raise Exception("The probability is greater than one: " + str(probability))
        elif probability < 0.0:
            raise Exception("The probability is lower than zero: " + str(probability))

        self.probability = probability

    def execute(self, source: S) -> S:
        pass


class Crossover:

    def __init__(self, probability: float):
        super(Crossover, self).__init__()
        if probability > 1.0:
            raise Exception("The probability is greater than one: " + str(probability))
        elif probability < 0.0:
            raise Exception("The probability is lower than zero: " + str(probability))

        self.probability = probability

    def execute(self, source: S) -> R:
        pass

    def get_number_of_parents(self) -> int:
        pass


class Selection(Operator):

    def __init__(self):
        super(Selection, self).__init__()

    def execute(self, source: S) -> R:
        pass


class Replacement(Operator):

    def __init__(self):
        super(Replacement, self).__init__()

    def execute(self, source: S) -> R:
        pass
