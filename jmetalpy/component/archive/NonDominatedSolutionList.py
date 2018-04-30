import logging
from queue import Queue
from typing import TypeVar

from jmetalpy.core.archive import Archive
from jmetalpy.component.comparator import Dominance, EqualSolutions
from jmetalpy.core.population import Population

S = TypeVar('S')
R = TypeVar('R')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NonDominatedSolutionList(Archive):

    def __init__(self):
        super(NonDominatedSolutionList, self).__init__()
        self.buffer = Queue()
        self.comparator = Dominance()

    def update(self, *args, **kwargs):
        logger.info("ARCHIVE update invoked")
        population = kwargs["POPULATION"]

        try:
            self.buffer.put(population)
        except Exception as ex:
            print("ARCHIVE buffer ex: " + str(ex))

    def apply(self, population: Population):
        for solution in population:
            self.add(solution)

        observable_data = {'POPULATION': population}
        self.notify_all(**observable_data)

    def add(self, solution: S) -> bool:
        is_dominated = False
        is_contained = False

        if len(self.solution_list) == 0:
            self.solution_list.append(solution)
            return True
        else:
            number_of_deleted_solutions = 0

            # New copy of list and enumerate
            for index, current_solution in enumerate(list(self.solution_list)):
                is_dominated_flag = self.comparator.compare(solution, current_solution)
                if is_dominated_flag == -1:
                    del self.solution_list[index-number_of_deleted_solutions]
                    number_of_deleted_solutions += 1
                elif is_dominated_flag == 1:
                    is_dominated = True
                    break
                elif is_dominated_flag == 0:
                    if EqualSolutions().compare(solution, current_solution) == 0:
                        is_contained = True
                        break

        if not is_dominated and not is_contained:
            self.solution_list.append(solution)
            return True

        return False

    def get_comparator(self):
        return self.comparator

    def run(self):
        logger.info("ARCHIVE OBSERVER: RUN")

        try:
            while True:
                population = self.buffer.get()
                logger.info("ARCHIVE OBSERVER: GET READY")
                self.apply(population)

                if population.is_terminated:
                    break
        except Exception as ex:
            print("ARCHIVE ex: " + str(ex))

        logger.info("ARCHIVE OBSERVER: END RUN")
