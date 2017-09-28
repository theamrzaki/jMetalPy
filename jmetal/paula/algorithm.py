import logging
import threading
import time
from typing import TypeVar, Generic, List

from jmetal.core.algorithm import Algorithm
from jmetal.core.problem import Problem
from jmetal.core.solution import FloatSolution
from jmetal.component.evaluator import Evaluator, SequentialEvaluator
from jmetal.paula.populationcreation import PopulationCreation
from jmetal.paula.population import Population

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

S = TypeVar('S')
R = TypeVar('R')

class EvolutionaryAlgorithm(Generic[S, R]):
    def __init__(self,
                 problem: Problem[S],
                 population_creation : PopulationCreation,
                 evaluation,
                 mating_pool,
                 variation,
                 replacement):
        super(EvolutionaryAlgorithm,self).__init__()
        self.problem = problem
        self.population_creation = population_creation
        self.mating_pool = mating_pool
        self.variation = variation
        self.replacement = replacement
        self.evaluation = evaluation

        self.population : Population[S]
        self.number_of_evaluations : int
        self.start_computing_time = 0

    def init_progress(self) -> None:
        self.number_of_evaluations = 0

    def is_stopping_condition_reached(self) -> bool:
        pass

    def update_progress(self):
        pass

    def get_result(self) -> R:
        pass

    def run(self):
        """
        Step One: Generate the initial population of individuals randomly. (First generation)
        Step Two: Evaluate the fitness of each individual in that population (time limit, sufficient fitness achieved, etc.)
        Step Three: Repeat the following regenerational steps until termination:
            1. Select the best-fit individuals for reproduction. (Parents)
            2. Breed new individuals through crossover and mutation operations to give birth to offspring.
            3. Evaluate the individual fitness of new individuals.
            4. Replace least-fit population with new individuals.
        """

        self.start_computing_time = time.time()

        self.population = self.population_creation.create() # Step One
        self.population = self.evaluation.evaluate(self.population) # Step Two
        self.init_progress()

        while not self.is_stopping_condition_reached(): # Step Three
            mating_population = self.mating_pool.apply(self.population) # Step Three.1
            offspring_population = self.variation.apply(mating_population) # Step Three.2
            offspring_population = self.evaluation.evaluate(offspring_population) # Step Three.3
            self.population = self.replacement.apply(self.population, offspring_population) # Step Three.4
            self.update_progress()

        self.total_computing_time = self.get_current_computing_time()

