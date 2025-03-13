import util
import math
from collections import Counter

from tree_index import TreeIndex

class B1Index(TreeIndex):
    def evaluate(self, tree, mode):
        s = 0
        try: #check if heights already precomputed
            tree.height
        except AttributeError:
            util.precompute_heights(tree)
        for node in tree.iter_descendants("postorder"):
            if node.is_leaf():
                continue
            s += 1/ node.height
        return s

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return -1


class B2Index(TreeIndex):
    def evaluate(self, tree, mode):
        s = 0
        try: #check if probs are already precomputed
            tree.prob
        except AttributeError:
            util.precompute_probs(tree)
        for leaf in tree.iter_leaves():
            p_leaf = leaf.prob
            s += p_leaf * math.log2(p_leaf)
        return - s

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            x  = math.floor(math.log2(n))
            pow_x = math.pow(2, x)
            return x + ((n - pow_x) / pow_x)
        if mode == "ARBITRARY":
            return math.log2(n)

    def minimum(self, n, m, mode):
        return 2 - math.pow(2, 2 - n)

    def imbalance(self):
        return -1


class SShape(TreeIndex):
    def evaluate(self, tree, mode):
        s = 0
        for node in tree.traverse("postorder"):
            if not node.is_leaf():
                s += math.log2(clade_size(tree, node) - 1)
        return s

    def maximum(self, n, m, mode):
        return math.log2(math.factorial(n - 1))

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            if n == 1:
                return 0
            return math.log2(n - 1)

    def imbalance(self):
        return 1

class DIndex(TreeIndex):
    def evaluate(self, tree, mode):
        n = util.clade_size(tree, tree)
        if n == 1:
            return 0
        f_n = Counter([util.clade_size(tree, node) for node in tree.traverse()])
        num_inner_nodes = len([_ for _ in tree.traverse()]) - n
        s = 0
        for z in range(2, n):
            p_n = (n / (n - 1)) * (2 / (z * (z + 1)))
            s += z * abs(f_n[z] / num_inner_nodes - p_n)
        s += n * abs(f_n[n] / num_inner_nodes - (1 / (n - 1)))
        return s

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0
