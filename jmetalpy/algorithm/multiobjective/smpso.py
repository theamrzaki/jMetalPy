import logging

import numpy
from jmetalpy.component.archive import Bounded

from jmetalpy.component.comparator import Dominance
from jmetalpy.component.population import RandomInitialPopulation
from jmetalpy.component.variation.VelocityAndPosition import VelocityAndPosition
from jmetalpy.core.algorithm import Algorithm
from jmetalpy.core.evaluator import Evaluator
from jmetalpy.core.operator import Mutation
from jmetalpy.core.problem import FloatProblem
from jmetalpy.core.terminator import Terminator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SMPSO(Algorithm):

    def __init__(self,
                 problem: FloatProblem,
                 initial_swarm: RandomInitialPopulation,
                 mutation: Mutation,
                 evaluator: Evaluator,
                 terminator: Terminator):
        super().__init__()
        self.problem = problem
        self.initial_swarm = initial_swarm
        self.terminator = terminator
        self.perturbation = mutation
        self.evaluator = evaluator
        self.swarm_evaluator = evaluator

        self.speed = numpy.zeros((self.initial_swarm.population_size, self.problem.number_of_variables), dtype=float)
        self.update_velocity_and_position = \
            VelocityAndPosition(self.problem, self.initial_swarm.population_size, self.speed)

        self.dominance_comparator = Dominance()

    def run(self):
        """
            while not self.is_stopping_condition_reached():
                self.update_velocity(self.swarm)
                self.update_position(self.swarm)
                self.perturbation(self.swarm)
                self.swarm = self.evaluate_swarm(self.swarm)
                self.update_global_best(self.swarm)
                self.update_particle_best(self.swarm)
        """
        logger.info("ADDING COMPONENTS...")
        self.initial_swarm.register(self.evaluator)
        self.evaluator.register(self.terminator)

        """
        self.initialize_velocity(self.swarm)
        self.initialize_particle_best(self.swarm)
        self.initialize_global_best(self.swarm)
        """

        logger.info("CREATING MAIN LOOP...")
        self.update_velocity_and_position.register(self.perturbation)
        self.perturbation.register(self.swarm_evaluator)
        self.swarm_evaluator.register()
        """
        self.update_global_best(self.swarm)
        self.update_particle_best(self.swarm)
        """

        logger.info("STARTING THREADS...")
        self.initial_swarm.start()
        self.evaluator.start()
        self.update_velocity_and_position.start()
        self.perturbation.start()
        self.swarm_evaluator.start()

        # start the algorithm
        logger.info("...OK! RUNNING SMPSO")
        self.initial_swarm.apply(self.problem)

