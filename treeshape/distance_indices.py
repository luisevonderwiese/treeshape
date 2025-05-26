import numpy as np
import math

import treeshape.util as util
from treeshape.tree_index import TreeIndex
from treeshape.depth_indices import SackinIndex

class TotalCopheneticIndex(TreeIndex):
    def evaluate_only(self, tree, mode):
        s = 0
        for node in tree.iter_descendants("postorder"):
            if not node.is_leaf():
                s += math.comb(util.clade_size(tree, node), 2)
        return s

    def evaluate(self, tree, mode):
        try:
            return tree.total_cophenetic_index
        except AttributeError:
            s = 0
            for node in tree.iter_descendants("postorder"):
                if not node.is_leaf():
                    s += math.comb(util.clade_size(tree, node), 2)
            tree.add_feature("total_cophenetic_index", s)
            return tree.total_cophenetic_index

    def maximum(self, n, m, mode):
        return math.comb(n, 3)

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            factorial = 1
            s = 0
            for i in range(n):
                a = 1
                j = 0
                if i != 0:
                    factorial *= i
                while (a * 2) <= factorial and factorial % (a * 2) == 0:
                    a *= 2
                    j += 1
                s += j
            return s
        if mode == "ARBITRARY":
            return 0

    def imbalance(self):
        return 1

class Diameter(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.diameter
        except AttributeError:
            if mode == "BINARY":
                util.diameter_recursive(tree, tree)
            if mode == "ARBITRARY":
                try:
                    distances = tree.all_distances
                except AttributeError:
                    util.precompute_distances(tree)
                    distances = tree.all_distances
                tree.diameter = max(distances)
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
                tree.add_feature("area_per_pair_index", (2 / n) * s - (4 / (n * (n - 1))) * c)
            return tree.area_per_pair_index

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 0



