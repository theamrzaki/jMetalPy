import logging
from typing import TypeVar, List

S = TypeVar('S')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DensityEstimator:

    def compute_density_estimator(self, solution_list: List[S]) -> float:
        pass


class DensityCrowdingDistance(DensityEstimator):

    def compute_density_estimator(self, solution_list: List[S]):
        size = len(solution_list)

        if size is 0:
            return
        elif size is 1:
            solution_list[0].attributes["crowding_distance"] = float("inf")
            return
        elif size is 2:
            solution_list[0].attributes["crowding_distance"] = float("inf")
            solution_list[1].attributes["crowding_distance"] = float("inf")
            return

        for i in range(len(solution_list)):
            solution_list[i].attributes["crowding_distance"] = 0.0

        number_of_objectives = solution_list[0].number_of_objectives

        for i in range(number_of_objectives):
            # Sort the population by Obj n
            solution_list = sorted(solution_list, key=lambda x: x.objectives[i])
            objective_minn = solution_list[0].objectives[i]
            objective_maxn = solution_list[len(solution_list) - 1].objectives[i]

            # Set de crowding distance
            solution_list[0].attributes["crowding_distance"] = float("inf")
            solution_list[size - 1].attributes["crowding_distance"] = float("inf")

            for j in range(1, size - 1):
                distance = solution_list[j + 1].objectives[i] - solution_list[j - 1].objectives[i]

                # Check if minimum and maximum are the same (in which case do nothing)
                if objective_maxn - objective_minn == 0:
                    logger.info("Minimum and maximum are the same!")
                else:
                    distance = distance / (objective_maxn - objective_minn)

                distance += solution_list[j].attributes["crowding_distance"]
                solution_list[j].attributes["crowding_distance"] = distance
