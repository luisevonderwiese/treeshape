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

class MinimumBCent(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.minimum_bcent
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("minimum_bcent", 0)
            else:
                try:
                    tree.bcent
                except AttributeError:
                    util.precompute_bcent(tree)
                tree.add_feature("minimum_bcent", min([node.bcent for node in tree.traverse() if not node.is_leaf()]))
            return tree.minimum_bcent

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class MaximumBCent(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.maximum_bcent
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("maximum_bcent", 0)
            else:
                try:  
                    tree.bcent
                except AttributeError:
                    util.precompute_bcent(tree)
                tree.add_feature("maximum_bcent", max([node.bcent for node in tree.traverse() if not node.is_leaf()]))
            return tree.maximum_bcent

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class MeanBCent(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.mean_bcent
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("mean_bcent", 0)
            else:
                try:
                    tree.bcent
                except AttributeError:
                    util.precompute_bcent(tree)
                bcents = [node.bcent for node in tree.traverse() if not node.is_leaf()]
                tree.add_feature("mean_bcent", sum(bcents) / len(bcents))
            return tree.mean_bcent

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class BCentVariance(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.bcent_variance
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("bcent_variance", 0)
            else:
                try:
                    tree.bcent
                except AttributeError:
                    util.precompute_bcent(tree)
                bcents = [node.bcent for node in tree.traverse() if not node.is_leaf()]
                tree.add_feature("bcent_variance", np.var(bcents))
            return tree.bcent_variance

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class BCentRoot(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            tree.bcent
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("bcent", 0)
            else:
                util.precompute_bcent(tree)
        return tree.bcent

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0


