import util
import math

from tree_index import TreeIndex

class AverageLadder(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError("average ladder is not defined for arbitrary trees")
        try:
            return tree.average_ladder
        except AttributeError:
            try:
                tree.ladders
            except:
                util.precompute_ladder_lengths(tree)
            if len(tree.ladders) == 0:
                tree.add_feature("average_ladder", 0)
            else:
                tree.add_feature("average_ladder", sum(tree.ladders) / len(tree.ladders))
            return tree.average_ladder

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1


class MaximumLadder(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError("maximum ladder is not defined for arbitrary trees")
        try:
            return tree.maximum_ladder
        except AttributeError:
            try:
                tree.ladders
            except:
                util.precompute_ladder_lengths(tree)
            if len(tree.ladders) == 0:
                tree.add_feature("maximum_ladder", 0)
            else:
                tree.add_feature("maximum_ladder", max(tree.ladders))
            return tree.maximum_ladder

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1
