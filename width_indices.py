import util

from tree_index import TreeIndex
from depth_indices import MaximumDepth

class MaximumWidth(TreeIndex):
    def evaluate(self, tree, mode):
        return max(util.widths(tree).values())

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            return n

    def minimum(self, n, m, mode):
        if n == 1:
            return 1
        return 2

    def imbalance(self):
        return -1


class MaxdiffWidths(TreeIndex):
    def evaluate(self, tree, mode):
        w = util.widths(tree)
        res = 0
        for i in range(len(w) - 1):
            diff = abs(w[i + 1] - w[i])
            res = max(res, diff)
        return res

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            return n - 1

    def minimum(self, n, m, mode):
        if n == 1:
            return 0
        return 1

    def imbalance(self):
        return -1


class ModifiedMaxdiffWidths(TreeIndex):
    def evaluate(self, tree, mode):
        w = util.widths(tree)
        res = 0
        for i in range(len(w) - 1):
            diff = w[i + 1] - w[i]
            res = max(res, diff)
        return res

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            return n - 1

    def minimum(self, n, m, mode):
        if n == 1:
            return 0
        return 1

    def imbalance(self):
        return -1


class MaxWidthOverMaxDepth(TreeIndex):
    def evaluate(self, tree, mode):
        h = MaximumDepth().evaluate(tree, mode)
        if h == 0:
            return 0
        return MaximumWidth().evaluate(tree, mode) / h

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        if n == 1:
            return 0
        return 2 / (n - 1)

    def imbalance(self):
        return -1
