import logging
from _random import Random
from copy import copy
from queue import Queue

import numpy

from jmetalpy.core.operator import Operator
from jmetalpy.core.population import Population
from jmetalpy.core.problem import FloatProblem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VelocityAndPosition(Operator):

    def __init__(self, problem: FloatProblem, swarm_size: int, speed):
        super(VelocityAndPosition, self).__init__()
        self.buffer = Queue()
        self.problem = problem
        self.speed = speed
        self.swarm_size = swarm_size

        self.c1_min = 1.5
        self.c1_max = 2.5
        self.c2_min = 1.5
        self.c2_max = 2.5

        self.min_weight = 0.1
        self.max_weight = 0.1

        self.change_velocity1 = -1
        self.change_velocity2 = -1

        self.delta_max = numpy.empty(problem.number_of_variables)
        self.delta_min = numpy.empty(problem.number_of_variables)
        for i in range(problem.number_of_variables):
            self.delta_max[i] = (self.problem.upper_bound[i] - self.problem.lower_bound[i]) / 2.0

        self.delta_min = -1.0 * self.delta_max

    def update(self, *args, **kwargs):
        logger.info("VARIATION update invoked")
        swarm = kwargs["POPULATION"]

        try:
            self.buffer.put(swarm)
        except Exception as ex:
            raise Exception("VARIATION buffer ex: " + str(ex))

    def apply(self, swarm: Population):
        if not swarm.is_terminated:
            logger.info("VARIATION: APPLY invoked")

            # Update velocity
            for i in range(self.swarm_size):
                particle = copy(swarm[i])
                best_particle = copy(swarm[i].attributes["local_best"])
                best_global = self.__select_global_best(swarm)

                r1 = Random.random
                r2 = Random.random

                c1 = Random.uniform(self.c1_min, self.c1_max)
                c2 = Random.uniform(self.c2_min, self.c2_max)

                wmin = self.min_weight
                wmax = self.max_weight

                for var in range(self.problem.number_of_variables):
                    self.speed[i][var] = \
                        self.__velocity_constriction(self.__constriction_coefficient(c1, c2) * \
                                                     (wmax * self.speed[i][var] +
                                                      c1 * r1 * (best_particle.variables[var] - particle.variables[
                                                                 var]) +
                                                      c2 * r2 * (best_global.variables[var] - particle.variables[var])),
                                                      var)

            # Update position
            for i in range(self.swarm_size):
                particle = swarm[i]

                for j in particle.variables:
                    particle.variables[j] += self.speed[i][j]

                    if particle.variables[j] < self.problem.lower_bound[j]:
                        particle.variables[j] = self.problem.lower_bound[j]
                        self.speed[i][j] *= self.change_velocity1

                    if particle.variables[j] > self.problem.upper_bound[j]:
                        particle.variables[j] = self.problem.upper_bound[j]
                        self.speed[i][j] *= self.change_velocity2

        observable_data = {'POPULATION': swarm}
        self.notify_all(**observable_data)

    def __select_global_best(self, swarm: Population):
        particles = Random.sample(swarm.leaders.solution_list, 2)
        if swarm.leaders.get_comparator().compare(particles[0], particles[1]) < 1:
            best_global = copy(particles[0])
        else:
            best_global = copy(particles[1])

        return best_global

    def __velocity_constriction(self, value: float, variable_index: int) -> float:
        result = None
        if value > self.delta_max[variable_index]:
            result = self.delta_max[variable_index]

        if value < self.delta_min[variable_index]:
            result = self.delta_min[variable_index]

        return result

    def __constriction_coefficient(self, c1: float, c2: float) -> float:
        rho = c1 + c2
        if rho <= 4:
            result = 1.0
        else:
            result = 2.0 / (2.0 - rho - numpy.sqrt(pow(rho, 2.0) - 4.0 * rho))

        return result

    def run(self):
        logger.info("VARIATION OBSERVER: RUN")

        try:
            while True:
                swarm = self.buffer.get()
                logger.info("VARIATION OBSERVER: GET READY")
                self.apply(swarm)

                if swarm.is_terminated:
                    break
        except Exception as ex:
            raise Exception("VARIATION ex: " + str(ex))

        logger.info("VARIATION OBSERVER: END RUN")
