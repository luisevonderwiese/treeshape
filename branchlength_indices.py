import util

from tree_index import TreeIndex

class Treeness(TreeIndex):
    def evaluate(self, tree, mode):
        if tree.is_leaf():
            return 0
        all_brlens = 0
        internal_brlens = 0
        for node in tree.traverse("postorder"):
            brlen = node.dist
            all_brlens += brlen
            if not node.is_leaf():
                internal_brlens += brlen
        return internal_brlens / all_brlens


    def maximum(self, n, m, mode):
        if n == 1:
            return 0
        return 1 #pseudo bound

    def minimum(self, n, m, mode):
        return 0

    def imbalance(self):
        return 0


class Stemminess(TreeIndex):
    def evaluate(self, tree, mode):
        if tree.is_leaf():
            return 0
        values = []
        for node in tree.iter_descendants("postorder"):
            d = node.dist
            if node.is_leaf():
                node.add_feature("sum_below", d)
            else:
                c = node.children
                s = d + sum([child.sum_below for child in c])
                node.add_feature("sum_below", s)
                if s == 0:
                    continue
                values.append(d / s)
        return sum(values) / len(values)


    def maximum(self, n, m, mode):
        if n == 1:
            return 0
        return 1 #pseudo bound

    def minimum(self, n, m, mode):
        return 0

    def imbalance(self):
        return 0
