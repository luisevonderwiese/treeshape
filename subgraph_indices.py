import util
import math

from tree_index import TreeIndex

class CherryIndex(TreeIndex):
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
            tree.add_feature("modified_cherry_index", util.clade_size(tree, tree) - 2 * CherryIndex().evaluate(tree, mode))
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
