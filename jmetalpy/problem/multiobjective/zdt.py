from math import sqrt, exp, pow, sin, pi, cos

from jmetalpy.core.problem import Objective
from jmetalpy.core.problem import FloatProblem
from jmetalpy.core.solution import FloatSolution


class ZDT1(FloatProblem):

    def __init__(self, number_of_variables: int = 30):
        super().__init__()
        self.objectives = [self.Objective1(), self.Objective2()]

        self.number_of_variables = number_of_variables
        self.number_of_objectives = len(self.objectives)
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    class Objective1(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            return solution.variables[0]

    class Objective2(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            g = self.__eval_g(solution)
            h = self.__eval_h(solution.variables[0], g)

            return h * g

        @staticmethod
        def __eval_g(solution: FloatSolution):
            g = sum(solution.variables) - solution.variables[0]

            constant = 9.0 / (solution.number_of_variables - 1)
            g = constant * g
            g = g + 1.0
            return g

        @staticmethod
        def __eval_h(f: float, g: float) -> float:
            return 1.0 - sqrt(f/g)

    def get_name(self):
        return "ZDT1"


class ZDT2(FloatProblem):

    def __init__(self, number_of_variables: int = 30):
        super().__init__()
        self.objectives = [self.Objective1(), self.Objective2()]

        self.number_of_variables = number_of_variables
        self.number_of_objectives = len(self.objectives)
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    class Objective1(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            return solution.variables[0]

    class Objective2(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            g = self.__eval_g(solution)
            h = self.__eval_h(solution.variables[0], g)

            return h * g

        def __eval_g(self, solution: FloatSolution):
            g = sum(solution.variables) - solution.variables[0]

            constant = 9.0 / (solution.number_of_variables - 1)
            g = constant * g
            g = g + 1.0
            return g

        def __eval_h(self, f: float, g: float) -> float:
            return 1.0 - pow(f / g, 2.0)

    def get_name(self):
        return "ZDT2"


class ZDT3(FloatProblem):

    def __init__(self, number_of_variables: int = 30):
        super().__init__()
        self.objectives = [self.Objective1(), self.Objective2()]

        self.number_of_variables = number_of_variables
        self.number_of_objectives = len(self.objectives)
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    class Objective1(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            return solution.variables[0]

    class Objective2(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            g = self.__eval_g(solution)
            h = self.__eval_h(solution.variables[0], g)

            return h * g

        def __eval_g(self, solution: FloatSolution):
            g = sum(solution.variables) - solution.variables[0]

            constant = 9.0 / (solution.number_of_variables - 1)
            g = constant * g
            g = g + 1.0
            return g

        def __eval_h(self, f: float, g: float) -> float:
            return 1.0 - sqrt(f / g) - (f / g) * sin(10.0 * f * pi)

    def get_name(self):
        return "ZDT3"


class ZDT4(FloatProblem):

    def __init__(self, number_of_variables: int = 10):
        super().__init__()
        self.objectives = [self.Objective1(), self.Objective2()]

        self.number_of_variables = number_of_variables
        self.number_of_objectives = len(self.objectives)
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [-5.0]
        self.upper_bound = self.number_of_variables * [5.0]
        self.lower_bound[0] = 0.0
        self.upper_bound[0] = 1.0

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    class Objective1(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            return solution.variables[0]

    class Objective2(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            g = self.__eval_g(solution)
            h = self.__eval_h(solution.variables[0], g)

            return h * g

        def __eval_g(self, solution: FloatSolution):
            g = 0.0

            for i in range(1, solution.number_of_variables):
                g += pow(solution.variables[i], 2.0) - 10.0 * cos(4.0 * pi * solution.variables[i])

            g += 1.0 + 10.0 * (solution.number_of_variables - 1)

            return g

        def __eval_h(self, f: float, g: float) -> float:
            return 1.0 - sqrt(f / g)

    def get_name(self):
        return "ZDT4"


class ZDT6(FloatProblem):

    def __init__(self, number_of_variables: int = 10):
        super().__init__()
        self.objectives = [self.Objective1(), self.Objective2()]

        self.number_of_variables = number_of_variables
        self.number_of_objectives = len(self.objectives)
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    class Objective1(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            return 1.0 - exp((-4.0) * solution.variables[0]) \
                   * pow(sin(6.0 * pi * solution.variables[0]), 6.0)

    class Objective2(Objective):
        def compute(self, solution: FloatSolution, problem: FloatProblem):
            g = self.__eval_g(solution)
            h = self.__eval_h(solution.objectives[0], g)

            return h * g

        def __eval_g(self, solution: FloatSolution):
            g = sum(solution.variables) - solution.variables[0]
            g = g / (solution.number_of_variables - 1)
            g = pow(g, 0.25)
            g = 9.0 * g
            g = 1.0 + g

            return g

        def __eval_h(self, f: float, g: float) -> float:
            return 1.0 - pow(f / g, 2.0)

    def get_name(self):
        return "ZDT6"
