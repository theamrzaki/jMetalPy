from typing import TypeVar

from jmetalpy.component.evaluator import Sequential
from jmetalpy.component.population import RandomInitialCreation
from jmetalpy.component.termination import ByEvaluations
from jmetalpy.core.algorithm import Algorithm
from jmetalpy.core.evaluator import Evaluator
from jmetalpy.core.operator import Mutation, Crossover, Selection
from jmetalpy.core.problem import Problem
from jmetalpy.core.terminator import Terminator
from jmetalpy.core.population import Population

S = TypeVar('S')
R = TypeVar(Population)


class NSGAII(Algorithm):

    def __init__(self, problem: Problem, initial_population: RandomInitialCreation, mutation: Mutation,
                 crossover: Crossover, selection: Selection, evaluator: Evaluator = Sequential(),
                 terminator: Terminator = ByEvaluations(1500)):
        super().__init__()
        self.initial_population = initial_population
        self.problem = problem
        self.mutation = mutation
        self.crossover = crossover
        self.selection = selection
        self.evaluator = evaluator
        self.terminator = terminator

    def run(self):
        # register components
        print("ADDING COMPONENTS")
        self.initial_population.register(self.evaluator)
        self.evaluator.register(self.terminator)

        print("MAIN LOOP")
        self.terminator.register(self.selection)
        self.selection.register(self.crossover)
        self.crossover.register(self.mutation)
        self.mutation.register(self.evaluator)
        self.evaluator.register(self.terminator)
        #self.evaluator.register(self.replacement)
        #self.replacement.register(self.terminator)

        print("STARTING THREADS")
        self.initial_population.start()
        self.evaluator.start()
        self.terminator.start()
        self.selection.start()
        self.crossover.start()
        self.mutation.start()

        # start the algorithm
        print("RUNNING ALGORITHM")
        self.initial_population.apply(self.problem)

