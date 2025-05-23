import numpy as np

import util

from tree_index import TreeIndex


class MinimumFarness(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.minimum_farness
        except AttributeError:
            try:
                tree.farness
            except AttributeError:
                util.precompute_distances(tree)
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
                util.precompute_distances(tree)
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
                util.precompute_distances(tree)
            tree.add_feature("total_farness", sum([node.farness for node in tree.traverse()]))
            return tree.total_farness

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

