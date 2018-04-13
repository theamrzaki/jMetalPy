from typing import TypeVar
from jmetalpy.core.population import Population
from jmetalpy.core.problem import Problem
from jmetalpy.core.evaluator import Evaluator

S = TypeVar('S')


class Sequential(Evaluator):

    def update(self, *args, **kwargs):
        print(">RECIEVED: EVALUATOR")
        population = kwargs["population"]

        self.evaluate(population, population.__getattribute__("problem"))

    def evaluate(self, population: Population, problem: Problem):
        if not population.__getattribute__("is_terminated"):
            pass

        observable_data = {'population': population, 'problem': problem}
        self.notify_all(**observable_data)
