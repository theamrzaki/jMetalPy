import threading
from typing import TypeVar

from jmetalpy.core.algorithm.observable import DefaultObservable, Observer, Observable

__author__ = "Antonio J. Nebro"

S = TypeVar('S')
R = TypeVar('R')


class Operator(DefaultObservable, Observer, threading.Thread):

    def __init__(self):
        super(Operator, self).__init__()
        self.observable: Observable = DefaultObservable()

    def update(self, *args, **kwargs):
        pass

    def execute(self, source: S) -> R:
        pass

    def get_name(self):
        pass


class Mutation(Operator):

    def __init__(self, probability: float):
        super().__init__()
        if probability > 1.0:
            raise Exception("The probability is greater than one: " + str(probability))
        elif probability < 0.0:
            raise Exception("The probability is lower than zero: " + str(probability))

        self.probability = probability

    def execute(self, source: S) -> S:
        pass


class Crossover(Operator):

    def __init__(self, probability: float):
        super().__init__()
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

    def execute(self, source: S) -> R:
        pass
