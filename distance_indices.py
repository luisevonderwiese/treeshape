import util

from tree_index import TreeIndex
from depth_indices import SackinIndex
from cophenetic_indices import TotalCopheneticIndex


class Diameter(TreeIndex):
    def evaluate(self, tree, mode):
        if tree.is_leaf(): #single-node-tree
            return 0
        max_d = 0
        deepest_leaf = None
        for leaf in tree.iter_leaves():
            if util.depth(tree, leaf) > max_d:
                max_d = util.depth(tree, leaf)
                deepest_leaf = leaf
        max_d = 0
        for leaf in tree.iter_leaves():
            max_d = max(max_d, util.connecting_path_length(tree, deepest_leaf, leaf))
        return max_d

    def maximum(self, n, m, mode):
        return n

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            if n == 1:
                return 0
            return 2

    def imbalance(self):
        return 0


class AreaPerPairIndex(TreeIndex):
    def evaluate(self, tree, mode):
        n = util.clade_size(tree, tree)
        if n == 1:
            return 0
        s = SackinIndex().evaluate(tree, mode)
        c = TotalCopheneticIndex().evaluate(tree, mode)
        return  2 / n * s - 4 / (n * (n - 1)) * c

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 0
