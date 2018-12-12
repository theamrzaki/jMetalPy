from jmetal.algorithm.multiobjective.nsgaii import NSGAII, DynamicNSGAII
from jmetal.component import ProgressBarObserver, RankingAndCrowdingDistanceComparator
from jmetal.component.observervable import TimeCounter
from jmetal.core.problem import DynamicProblem
from jmetal.operator import BinaryTournamentSelection, BitFlip, SPX, Polynomial, SBX
from jmetal.problem.multiobjective.fda import FDA2
from jmetal.util.termination_criteria import Endless

if __name__ == '__main__':
    problem: DynamicProblem = FDA2()
    time_counter = TimeCounter(problem.observable, 1)
    time_counter.start()

    algorithm = DynamicNSGAII(
        problem=problem,
        population_size=100,
        offspring_size=100,
        mating_pool_size=100,
        mutation=Polynomial(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBX(probability=1.0, distribution_index=20),
        selection=BinaryTournamentSelection(comparator=RankingAndCrowdingDistanceComparator()),
        termination_criteria=Endless()
    )

    progress_bar = ProgressBarObserver(max=25000)
    algorithm.observable.register(observer=progress_bar)

    algorithm.run()

