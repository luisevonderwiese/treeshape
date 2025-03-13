import util

from tree_index import TreeIndex

class MeanI(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        values = util.I_values(tree, "I")
        return sum(values) / len(values)

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1


class TotalI(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        return sum(util.I_values(tree, "I"))

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1


class MeanIPrime(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        values = util.I_values(tree, "I_prime")
        return sum(values) / len(values)

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1


class TotalIPrime(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        return sum(util.I_values(tree, "I_prime"))

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1


class MeanIW(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        sw = util.I_weight_sum(tree)
        values = util.I_values(tree, "I_w", sw)
        return sum(values) / len(values)

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1


class TotalIW(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError(metric_name + " is not defined for arbitrary trees")
        if tree.is_leaf():
            return 0
        sw = util.I_weight_sum(tree)
        return sum(util.I_values(tree, "I_w", sw))

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 1
