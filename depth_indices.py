import util
import math
import numpy as np

from tree_index import TreeIndex

class AverageLeafDepth(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.average_leaf_depth
        except AttributeError:
            depths = util.leaf_depths(tree)
            tree.add_feature("average_leaf_depth", sum(depths) / len(depths))
            return tree.average_leaf_depth

    def maximum(self, n, m, mode):
        return m - (((m - 1) * m) / (2 * n))

    def minimum(self, n, m, mode):
        k = n - m + 1
        x = math.floor(math.log2(n / k))
        return  x + 3 - (k / n) * math.pow(2, x + 1)

    def imbalance(self):
        return 1


class VarianceOfLeavesDepths(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.variance_of_leaves_depths
        except AttributeError:
            tree.add_feature("variance_of_leaves_depths", float(np.var(util.leaf_depths(tree))))
            return tree.variance_of_leaves_depths

    def maximum(self, n, m, mode):
        return ((n - 1) * (n - 2) * (n*n + 3*n -6)) / (12 * n * n)

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            return 0

    def imbalance(self):
        return 1


class SackinIndex(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.sackin_index
        except AttributeError:
            tree.add_feature("sackin_index", sum(util.leaf_depths(tree)))
            return tree.sackin_index

    def maximum(self, n, m, mode):
        return (n * m) - (((m - 1) * m) / 2)

    def minimum(self, n, m, mode):
        k = n - m + 1
        x = math.floor(math.log2(n / k))
        return (x + 3) * n - k * math.pow(2, x + 1)

    def imbalance(self):
        return 1


class TotalPathLength(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.total_path_length
        except AttributeError:
            tree.add_feature("total_path_length", sum([util.depth(tree, node) for node in tree.traverse("postorder")]))
            return tree.total_path_length

    def maximum(self, n, m, mode):
        return (n * n) - n

    def minimum(self, n, m, mode):
        if n == 1:
            return 0
        if mode == "BINARY":
            log_val = math.floor(math.log2(n))
            return 2 * log_val * n - math.pow(2, log_val + 2) + 2 * n + 2
        if mode == "ARBITRARY":
            return n

    def imbalance(self):
        return 1


class TotalInternalPathLength(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.total_internal_path_length
        except AttributeError:
            s = 0
            for node in tree.iter_descendants("postorder"):
                if not node.is_leaf():
                    s += util.depth(tree, node)
            tree.add_feature("total_internal_path_length", s)
            return tree.total_internal_path_length

    def maximum(self, n, m, mode):
        return ((n - 1) * (n - 2)) / 2

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            log_val = math.floor(math.log2(n))
            return log_val * n - math.pow(2, log_val + 1) + 2
        if mode == "ARBITRARY":
            return 0

    def imbalance(self):
        return 1


class AverageVertexDepth(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.average_vertex_depth
        except AttributeError:
            depths = [util.depth(tree, node) for node in tree.traverse("postorder")]
            tree.add_feature("average_vertex_depth", sum(depths) / len(depths))
            return tree.average_vertex_depth

    def maximum(self, n, m, mode):
        return ((n * n) - n) / (2 * n - 1)

    def minimum(self, n, m, mode):
        if n == 1:
            return 0
        if mode == "BINARY":
            log_val = math.floor(math.log2(n))
            return (2 * log_val * n - math.pow(2, log_val + 2) + 2 * n + 2) / (2 * n - 1)
        if mode == "ARBITRARY":
            return n / (n + 1)

    def imbalance(self):
        return 1


class MaximumDepth(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.maximum_depth
        except AttributeError:
            tree.add_feature("maximum_depth", max(util.leaf_depths(tree)))
            return tree.maximum_depth

    def maximum(self, n, m, mode):
        return n - 1

    def minimum(self, n, m, mode):
        if n == 1:
            return 0
        if mode == "BINARY":
            return math.floor(math.log2(n)) + 1
        if mode == "ARBITRARY":
            return 1

    def imbalance(self):
        return 1
