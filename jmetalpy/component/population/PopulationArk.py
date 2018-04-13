from typing import List, TypeVar

from jmetalpy.core.population import Population
from jmetalpy.core.solution import Solution

S = TypeVar('S')


class PopulationArk(Population):

    def __init__(self, population_size: int):
        super().__init__()
        self.evaluations: int = 0
        self.population_size = population_size
        self.population_list: List[S] = []

    def add(self, individual: Solution):
        if len(self.population_list) < self.population_size:
            self.population_list.append(individual)

    def get_evaluations(self) -> int:
        return self.evaluations
