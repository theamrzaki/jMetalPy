from jmetalpy.core.algorithm.observable import Observer, DefaultObservable
from jmetalpy.core.population import Population
from jmetalpy.core.problem import Problem

from typing import TypeVar

S = TypeVar('S')


class Evaluator(DefaultObservable, Observer):

    def __init__(self):
        super(Evaluator, self).__init__()

    def update(self, *args, **kwargs):
        pass

    def apply(self, population: Population):
        pass

    def run(self):
        pass

    @staticmethod
    def evaluate_solution(solution: S, problem: Problem) -> None:
        problem.evaluate(solution)
        if problem.number_of_constraints > 0:
            problem.evaluate_constraints(solution)
