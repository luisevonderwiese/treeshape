import util
import math

from tree_index import TreeIndex

class CollessIndex(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        s = 0
        for node in tree.traverse("postorder"):
            if not node.is_leaf():
                s += util.balance_index(tree, node)
        return s

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return ((n - 1) * (n - 2)) / 2
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            sum_bound = math.ceil(math.log2(n))
            s = 0
            for j in range(1, sum_bound):
                x = math.pow(2, -j) * n
                triangle_wave = min(math.ceil(x) - x, x - math.floor(x))
                s += math.pow(2, j) * triangle_wave
            return s
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 1


class CorrectedCollessIndex(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        n = util.clade_size(tree, tree)
        return (2 * CollessIndex().evaluate(tree, mode)) / ((n-1) * (n-2))

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            if n <= 2:
                return 0
            return 1
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            if n <= 2:
                return 0
            return (2 / ((n - 1) * (n - 2))) * minimum("colless_index", n, m, mode)
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 1


class QuadraticCollessIndex(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        s = 0
        for node in tree.traverse("postorder"):
            if not node.is_leaf():
                b = balance_index(tree, node)
                s += b * b
        return s

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return math.comb(n, 3) + math.comb(n - 1, 3)
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            sum_bound = math.ceil(math.log2(n))
            s = 0
            for j in range(1, sum_bound):
                x = math.pow(2, -j) * n
                triangle_wave = min(math.ceil(x) - x, x - math.floor(x))
                s += math.pow(2, j) * triangle_wave
            return s
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 1


class I2Index(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        n = util.clade_size(tree, tree)
        s = 0
        for node in tree.traverse("postorder"):
            n_v = util.clade_size(tree, node)
            if n_v > 2:
                b = util.balance_index(tree, node)
                s += b / (n_v - 2)
        return s / (n - 2)

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            if n <= 2:
                return 0
            return 1
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1


class Stairs1(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        return RogersJIndex().evaluate(tree, mode) /  (util.clade_size(tree, tree)- 1)

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            if n == 1:
                return 0
            return (n - 2) / (n - 1)
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            if n == 1:
                return 0
            return (bin(n).count("1") - 1) / (n - 1)
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        raise 1


class Stairs2(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        s = 0
        for node in tree.traverse("postorder"):
            if node.is_leaf():
                continue
            c = node.children
            assert (len(c) == 2)
            n0 = util.clade_size(tree, c[0])
            n1 = util.clade_size(tree, c[1])
            s += min(n0, n1) / max(n0, n1)
        return s / (util.clade_size(tree, tree) - 1)

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 1


class RogersJIndex(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        s = 0
        for node in tree.traverse("postorder"):
            if not node.is_leaf():
                if util.balance_index(tree, node) != 0:
                    s += 1
        return s

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            if n == 1:
                return 0
            return n - 2
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return bin(n).count("1") - 1
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 1


class SymmetryNodesIndex(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        cnt = 0
        for node in tree.traverse("postorder"):
            if not node.is_leaf():
                c = node.children
                assert (len(c) == 2)
                if not util.isomorphic(c[0], c[1]):
                    cnt += 1
        return cnt

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            if n == 1:
                return 0
            return n - 2
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return bin(n).count("1") - 1
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 1
