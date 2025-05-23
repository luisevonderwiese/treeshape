import util
import math

from tree_index import TreeIndex

class CherryIndex(TreeIndex):
    def evaluate_only(self, tree, mode):
        cnt = 0
        for node in tree.traverse("postorder"):
            if node.is_leaf():
                continue
            direct_leaves = len([child for child in node.children if child.is_leaf()])
            if direct_leaves >= 2:
                cnt += math.comb(direct_leaves, 2)
        return  cnt

    def evaluate(self, tree, mode):
        try:
            return tree.cherry_index
        except AttributeError:
            cnt = 0
            for node in tree.traverse("postorder"):
                if node.is_leaf():
                    continue
                direct_leaves = len([child for child in node.children if child.is_leaf()])
                if direct_leaves >= 2:
                    cnt += math.comb(direct_leaves, 2)
            tree.add_feature("cherry_index", cnt)
            return tree.cherry_index

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            return math.floor(n / 2)
        if mode == "ARBITRARY":
            return math.comb(n, 2)

    def minimum(self, n, m, mode):
        if n == 1:
            return 0
        return 1

    def imbalance(self):
        return 0


class ModifiedCherryIndex(TreeIndex):
    def evaluate(self, tree, mode):
        if mode == "ARBITRARY":
            raise ValueError("modified_cherry_index is not defined for arbitrary trees")
        try:
            return tree.modified_cherry_index
        except AttributeError:
            tree.add_feature("modified_cherry_index", util.clade_size(tree, tree) - 2 * CherryIndex().evaluate_only(tree, mode))
            return tree.modified_cherry_index

    def maximum(self, n, m, mode):
        if mode == "BINARY":
            if n == 1:
                return 1
            return n - 2
        if mode == "ARBITRARY":
            return float("nan")

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return n % 2
        if mode == "ARBITRARY":
            return float("nan")

    def imbalance(self):
        return 0


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

