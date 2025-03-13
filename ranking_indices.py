import util

from tree_index import TreeIndex

class ColijnPlazottaRank(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        try:
            return tree.colijn_plazotta_rank
        except AttributeError:
            util.colijn_plazotta_recursive(tree)
            return tree.colijn_plazotta_rank

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 1


class FurnasRank(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        try:
            return tree.furnas_rank #check if furnas ranks already precomputed
        except AttributeError:
            util.furnas_ranks(tree)
            return tree.furnas_rank

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            try:
                return util.we(n)
            except NotImplementedError:
                return float("nan")
        if mode == "ABITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return 1
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return -1
