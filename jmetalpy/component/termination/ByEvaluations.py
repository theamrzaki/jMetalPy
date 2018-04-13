from jmetalpy.core.terminator import Terminator
from jmetalpy.core.population import Population


class ByEvaluations(Terminator):

    def __init__(self, max_evaluations: int = 1500):
        super(ByEvaluations, self).__init__()
        self.max_evaluations = max_evaluations

    def update(self, *args, **kwargs):
        population = kwargs["population"]

        if population.__getattribute__("evaluations") > self.max_evaluations:
            population.__setattr__("is_terminated", True)
            print("ALGORITHM TERMINATED!!")

        observable_data = {'population': population}
        self.notify_all(**observable_data)

    def apply(self, population: Population) -> float:
        pass
