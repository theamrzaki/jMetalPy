import random
from typing import TypeVar


import jmetalpy
from jmetalpy.core.solution import BinarySolution, FloatSolution, IntegerSolution, Solution

S = TypeVar('S')


class Problem:

    def __init__(self):
        self.objectives: [jmetalpy.core.problem.Objective] = None
        self.number_of_variables: int = None
        self.number_of_objectives: int = None
        self.number_of_constraints: int = None

    def evaluate(self, solution: S) -> None:
        if self.objectives is None:
            raise Exception("Not a single objective have been indicated")

        for i in range(self.number_of_objectives):
            if self.objectives[i].is_a_minimization_objective():
                solution.objectives[i] = self.objectives[i].compute(solution, self)
            else:
                solution.objectives[i] = -1.0 * self.objectives[i].compute(solution, self)

    def evaluate_constraints(self, solution: S):
        pass

    def create_solution(self) -> S:
        pass

    def get_name(self) -> str:
        pass


class BinaryProblem(Problem):

    def evaluate(self, solution: BinarySolution) -> None:
        pass

    def create_solution(self) -> BinarySolution:
        pass


class FloatProblem(Problem):

    def __init__(self):
        super().__init__()
        self.lower_bound: [] = None
        self.upper_bound: [] = None

    def create_solution(self) -> FloatSolution:
        new_solution = FloatSolution(self.number_of_variables, self.number_of_objectives, self.number_of_constraints,
                                     self.lower_bound, self.upper_bound)
        new_solution.variables = \
            [random.uniform(self.lower_bound[i]*1.0, self.upper_bound[i]*1.0) for i in range(self.number_of_variables)]

        return new_solution


class IntegerProblem(Problem):

    def __init__(self):
        super().__init__()
        self.lower_bound: [] = None
        self.upper_bound: [] = None

    def create_solution(self) -> IntegerSolution:
        new_solution = IntegerSolution(
            self.number_of_variables,
            self.number_of_objectives,
            self.number_of_constraints,
            self.lower_bound, self.upper_bound)

        new_solution.variables = \
            [int(random.uniform(self.lower_bound[i]*1.0, self.upper_bound[i]*1.0)) for i in range(self.number_of_variables)]

        return new_solution


class Objective:

    def compute(self, solution: Solution, problem: Problem) -> float:
        pass

    def is_a_minimization_objective(self) -> bool:
        return True
