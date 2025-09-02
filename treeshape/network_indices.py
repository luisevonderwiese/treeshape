import numpy as np

import treeshape.util as util
from treeshape.tree_index import TreeIndex
from treeshape.depth_indices import SackinIndex
from treeshape.distance_indices import TotalCopheneticIndex

class WienerIndex(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.wiener_index
        except AttributeError:
            n = util.clade_size(tree, tree)
            if n == 1:
                tree.add_feature("wiener_index", 0)
            else:
                s = SackinIndex().evaluate_only(tree, mode)
                c = TotalCopheneticIndex().evaluate_only(tree, mode)
                tree.add_feature("wiener_index", (n - 1) * s - 2 * c)
            return tree.wiener_index

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class MinimumFarness(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.minimum_farness
        except AttributeError:
            try:
                tree.farness
            except AttributeError:
                util.precompute_farness(tree)
            tree.add_feature("minimum_farness", min([node.farness for node in tree.traverse()]))
            return tree.minimum_farness

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class MaximumFarness(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.maximum_farness
        except AttributeError:
            try:
                tree.farness
            except AttributeError:
                util.precompute_farness(tree)
            tree.add_feature("maximum_farness", max([node.farness for node in tree.traverse()]))
            return tree.maximum_farness

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class TotalFarness(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.total_farness
        except AttributeError:
            try:
                tree.farness
            except AttributeError:
                util.precompute_farness(tree)
            tree.add_feature("total_farness", sum([node.farness for node in tree.traverse()]))
            return tree.total_farness

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

