import util
import math

from tree_index import TreeIndex

class TotalCopheneticIndex(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.total_cophenetic_index
        except AttributeError:
            s = 0
            for node in tree.iter_descendants("postorder"):
                if not node.is_leaf():
                    s += math.comb(util.clade_size(tree, node), 2)
            tree.add_feature("total_cophenetic_index", s)
            return tree.total_cophenetic_index

    def maximum(self, n, m, mode):
        return math.comb(n, 3)

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            factorial = 1
            s = 0
            for i in range(n):
                a = 1
                j = 0
                if i != 0:
                    factorial *= i
                while (a * 2) <= factorial and factorial % (a * 2) == 0:
                    a *= 2
                    j += 1
                s += j
            return s
        if mode == "ARBITRARY":
            return 0

    def imbalance(self):
        return 1
