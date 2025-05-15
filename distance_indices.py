import numpy as np

import util

from tree_index import TreeIndex
from depth_indices import SackinIndex
from cophenetic_indices import TotalCopheneticIndex


class Diameter(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.diameter
        except AttributeError:
            if tree.is_leaf(): #single-node-tree
                tree.add_feature("diameter", 0)
            else:
                max_d = 0
                deepest_leaf = None
                for leaf in tree.iter_leaves():
                    if util.depth(tree, leaf) > max_d:
                        max_d = util.depth(tree, leaf)
                        deepest_leaf = leaf
                max_d = 0
                for leaf in tree.iter_leaves():
                    max_d = max(max_d, util.connecting_path_length(tree, deepest_leaf, leaf))
                tree.add_feature("diameter", max_d)
            return tree.diameter

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
        try:
            return tree.area_per_pair_index
        except AttributeError:
            n = util.clade_size(tree, tree)
            if n == 1:
                tree.add_feature("area_per_pair_index", 0)
            else:
                s = SackinIndex().evaluate_only(tree, mode)
                c = TotalCopheneticIndex().evaluate_only(tree, mode)
                tree.add_feature("area_per_pair_index", 2 / n * s - 4 / (n * (n - 1)) * c)
            return tree.area_per_pair_index

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 0

