from jmetalpy.component.comparator import Dominance
from jmetalpy.core.population import Population
from jmetalpy.core.ranking import Ranking


class FastNonDominated(Ranking):

    def __init__(self):
        super(FastNonDominated, self).__init__()

    def compute_ranking(self, solution_list: Population):
        # number of solutions dominating solution ith
        dominate_me = [0 for _ in range(len(solution_list))]

        # list of solutions dominated by solution ith
        i_dominate = [[] for _ in range(len(solution_list))]

        # front[i] contains the list of solutions belonging to front i
        front = [[] for _ in range(len(solution_list) + 1)]

        for p in range(len(solution_list) - 1):
            for q in range(p + 1, len(solution_list)):
                dominance_test_result = Dominance().compare(solution_list[p], solution_list[q])
                self.number_of_comparions += 1
                if dominance_test_result is -1:
                    i_dominate[p].append(q)
                    dominate_me[q] += 1
                elif dominance_test_result is 1:
                    i_dominate[q].append(p)
                    dominate_me[p] += 1

        for i in range(len(solution_list)):
            if dominate_me[i] is 0:
                front[0].append(i)
                solution_list[i].attributes["dominance_ranking"] = 0

        i = 0
        while len(front[i]) != 0:
            i += 1
            for p in front[i - 1]:
                if p <= len(i_dominate):
                    for q in i_dominate[p]:
                        index = q
                        dominate_me[index] -= 1
                        if dominate_me[index] is 0:
                            front[i].append(index)
                            solution_list[index].attributes["dominance_ranking"] = i

        self.ranked_sublists = [[]] * i
        for j in range(i):
            Q = [0] * len(front[j])
            for k in range(len(front[j])):
                Q[k] = solution_list[front[j][k]]
            self.ranked_sublists[j] = Q

        return self.ranked_sublists