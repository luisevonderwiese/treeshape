import util
import math

from tree_index import TreeIndex

class RootImbalance(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf(): #single-node-tree
            return 0
        c = tree.children
        assert (len(c) == 2)
        return max(util.clade_size(tree, c[0]), util.clade_size(tree, c[1])) / util.clade_size(tree, tree)

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return (n - 1) / n
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            if n == 1:
                return 0
            return math.ceil(n / 2) / n
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 0

class IRoot(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf(): #single-node-tree
            return 0
        return util.I_value(tree, tree)

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            if n == 1:
                return 0
            return 1
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return 0
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 0
