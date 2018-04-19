from jmetalpy.core.population import Population


class Ranking:

    def __init__(self):
        self.number_of_comparisons = None
        self.number_of_comparions = 0
        self.ranked_sublists = []

    def compute_ranking(self, solution_list: Population):
        pass

    def get_subfront(self, rank: int):
        if rank >= len(self.ranked_sublists):
            raise Exception("Invalid rank: " + str(rank) + ". Max rank = " + str(len(self.ranked_sublists) -1))
        return self.ranked_sublists[rank]

    def get_number_of_subfronts(self):
        return len(self.ranked_sublists)

    def get_number_of_comparions(self) -> int:
        return self.number_of_comparisons
