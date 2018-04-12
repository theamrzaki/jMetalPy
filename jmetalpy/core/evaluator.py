from jmetalpy.core.problem import Problem

from typing import TypeVar, List, Generic

S = TypeVar('S')


class Evaluator(Generic[S]):
    def evaluate(self, solution_list: List[S], problem: Problem) -> List[S]:
        pass

    @staticmethod
    def evaluate_solution(solution: S, problem: Problem) -> None:
        problem.evaluate(solution)
        if problem.number_of_constraints > 0:
            problem.evaluate_constraints(solution)
