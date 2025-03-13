import util
import math
import numpy as np

from tree_index import TreeIndex

class AverageLeafDepth(TreeIndex):
    def evaluate(self, tree, mode):
        depths = util.leaf_depths(tree)
        return sum(depths) / len(depths)

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
        return np.var(util.leaf_depths(tree))

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
        return sum(util.leaf_depths(tree))

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
        return sum([util.depth(tree, node) for node in tree.traverse("postorder")])

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
        s = 0
        for node in tree.iter_descendants("postorder"):
            if not node.is_leaf():
                s += util.depth(tree, node)
        return s

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
        depths = [util.depth(tree, node) for node in tree.traverse("postorder")]
        return sum(depths) / len(depths)

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
        return max(util.leaf_depths(tree))

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
