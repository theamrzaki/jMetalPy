from typing import TypeVar

from jmetalpy.component.density_estimator import DensityCrowdingDistance
from jmetalpy.core.operator import Selection
from jmetalpy.core.population import Population
from jmetalpy.component.ranking import FastNonDominated

S = TypeVar('S')


class RankingAndCrowdingDistance(Selection):

    def __init__(self, max_population_size: int):
        super().__init__()
        self.max_population_size = max_population_size

    def execute(self, population: Population) -> Population:
        ranking = FastNonDominated()
        crowding_distance = DensityCrowdingDistance()
        ranking.compute_ranking(population)

        ranking_index = 0
        new_solution_list = []

        while len(new_solution_list) < self.max_population_size:
            if len(ranking.get_subfront(ranking_index)) < self.max_population_size - len(new_solution_list):
                new_solution_list = new_solution_list + ranking.get_subfront(ranking_index)
                ranking_index += 1
            else:
                subfront = ranking.get_subfront(ranking_index)
                crowding_distance.compute_density_estimator(subfront)
                sorted_subfront = sorted(subfront, key=lambda x: x.attributes["crowding_distance"], reverse=True)
                for i in range((self.max_population_size - len(new_solution_list))):
                    new_solution_list.append(sorted_subfront[i])

        return new_solution_list
