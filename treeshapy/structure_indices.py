import math
from collections import Counter

import treeshapy.util as util
from treeshapy.tree_index import TreeIndex


class RootedQuartetIndex(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.rooted_quartet_index #check if rqis already precomputed
        except AttributeError:
            util.precompute_rqi(tree)
            return tree.rooted_quartet_index

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            return 4 * math.comb(n, 4)

    def minimum(self, n, m, mode):
        return 0

    def imbalance(self):
        return -1

class SShape(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.s_shape
        except AttributeError:
            s = 0
            for node in tree.traverse("postorder"):
                if not node.is_leaf():
                    s += math.log2(util.clade_size(tree, node) - 1)
            tree.add_feature("s_shape", s)
            return tree.s_shape

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
        try:
            return tree.d_index
        except AttributeError:
            n = util.clade_size(tree, tree)
            if n == 1:
                tree.add_feature("d_index", 0)
            else:
                f_n = Counter([util.clade_size(tree, node) for node in tree.traverse()])
                num_inner_nodes = len([_ for _ in tree.traverse()]) - n
                s = 0
                for z in range(2, n):
                    p_n = (n / (n - 1)) * (2 / (z * (z + 1)))
                    s += z * abs(f_n[z] / num_inner_nodes - p_n)
                s += n * abs(f_n[n] / num_inner_nodes - (1 / (n - 1)))
                tree.add_feature("d_index", s)
            return tree.d_index

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class LadderLength(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError("ladder_length is not defined for arbitrary trees")
        try:
            return tree.ladder_length
        except AttributeError:
            for node in tree.traverse("postorder"):
                if node.is_leaf():
                    node.add_feature("ladder_length", -1)
                    continue
                c = node.children
                if c[0].is_leaf():
                    node.add_feature("ladder_length", c[1].ladder_length + 1)
                elif c[1].is_leaf():
                    node.add_feature("ladder_length", c[0].ladder_length + 1)
                else: #not part of a ladder
                    node.add_feature("ladder_length", 0)
            max_ladder = 0
            for node in tree.traverse("postorder"):
                max_ladder = max(max_ladder, node.ladder_length)
            tree.add_feature("ladder_length", max_ladder)
            return tree.ladder_length

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

class ILNumber(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.IL_number
        except AttributeError:
            cnt = 0
            for node in tree.traverse("postorder"):
                if len([c for c in node.children if c.is_leaf()]) == 1:
                    cnt += 1
            tree.add_feature("IL_number", cnt)
            return tree.IL_number

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0
