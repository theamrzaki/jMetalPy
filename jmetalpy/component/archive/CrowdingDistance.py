from typing import TypeVar, List

from jmetalpy.component.archive import Bounded, NonDominatedSolutionList
from jmetalpy.component.density_estimator import DensityCrowdingDistance
from jmetalpy.component.comparator import SolutionAttribute

S = TypeVar('S')


class CrowdingDistance(Bounded):
    def __init__(self, maximum_size: int):
        super(CrowdingDistance, self).__init__(maximum_size)
        self.__non_dominated_solution_archive = NonDominatedSolutionList()
        self.__comparator = SolutionAttribute("crowding_distance", lowest_is_best=False)
        self.__crowding_distance = DensityCrowdingDistance()
        self.solution_list = self.__non_dominated_solution_archive.get_solution_list()

    def add(self, solution: S) -> bool:
        success = self.__non_dominated_solution_archive.add(solution)
        if success:
            if self.size() > self.get_max_size():
                self.compute_density_estimator()
                worst_solution = self.__find_worst_solution(self.get_solution_list())
                self.get_solution_list().remove(worst_solution)

        return success

    def compute_density_estimator(self):
        self.__crowding_distance.compute_density_estimator(self.get_solution_list())

    def __find_worst_solution(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is None")
        elif len(solution_list) is 0:
            raise Exception("The solution list is empty")

        worst_solution = solution_list[0]
        for solution in solution_list[1:]:
            if self.__comparator.compare(worst_solution, solution) < 0:
                worst_solution = solution

        return worst_solution

    def get_comparator(self):
        return self.__comparator
