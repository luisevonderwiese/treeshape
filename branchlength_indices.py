import numpy as np

import util

from tree_index import TreeIndex

class Treeness(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.treeness
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("treeness", 0)
            else:
                all_brlens = 0
                internal_brlens = 0
                for node in tree.traverse("postorder"):
                    brlen = node.dist
                    all_brlens += brlen
                    if not node.is_leaf():
                        internal_brlens += brlen
                tree.add_feature("treeness", internal_brlens / all_brlens)
            return tree.treeness

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
        try:
            return tree.stemminess
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("stemminess", 0)
            else:
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
                tree.add_feature("stemminess", sum(values) / len(values))
            return tree.stemminess

    def maximum(self, n, m, mode):
        if n == 1:
            return 0
        return 1 #pseudo bound

    def minimum(self, n, m, mode):
        return 0

    def imbalance(self):
        return 0


class PhylogeneticDiversity(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.phylogenetic_diversity
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("phylogenetic_diversity", 0)
            else:
                all_brlens = 0
                for node in tree.traverse("postorder"):
                    all_brlens += node.dist
                tree.add_feature("phylogenetic_diversity", all_brlens)
            return tree.phylogenetic_diversity

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0


class MeanBranchLength(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.mean_branch_length
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("mean_branch_length", 0)
            else:      
                all_brlens = []
                for node in tree.traverse("postorder"):
                    all_brlens.append(node.dist)
                tree.add_feature("mean_branch_length", sum(all_brlens) / len(all_brlens))
            return tree.mean_branch_length

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0


class BranchLengthVariance(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.branch_length_variance
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("branch_length_variance", 0)
            else:
                all_brlens = []
                for node in tree.traverse("postorder"):
                    all_brlens.append(node.dist)
                tree.add_feature("branch_length_variance", np.var(all_brlens))
            return tree.branch_length_variance

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0


class MeanInternalBranchLength(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.mean_internal_branch_length
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("mean_internal_branch_length", 0)
            else:
                internal_brlens = []
                for node in tree.traverse("postorder"):
                    if not node.is_leaf():
                        internal_brlens.append(node.dist)
                tree.add_feature("mean_internal_branch_length", sum(internal_brlens) / len(internal_brlens))
            return tree.mean_internal_branch_length

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0


class InternalBranchLengthVariance(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.internal_branch_length_variance
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("internal_branch_length_variance", 0)
            else:
                internal_brlens = []
                for node in tree.traverse("postorder"):
                    if not node.is_leaf():
                        internal_brlens.append(node.dist)
                tree.add_feature("internal_branch_length_variance", np.var(internal_brlens))
            return tree.internal_branch_length_variance

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0


class MeanExternalBranchLength(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.mean_external_branch_length
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("mean_external_branch_length", 0)
            else:
                external_brlens = []
                for node in tree.traverse("postorder"):
                    if node.is_leaf():
                        external_brlens.append(node.dist)
                tree.add_feature("mean_external_branch_length", sum(external_brlens) / len(external_brlens))
            return tree.mean_external_branch_length

    def maximum(self, n, m, mode):
        return float("nan")

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0


class ExternalBranchLengthVariance(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.external_branch_length_variance
        except AttributeError:
            if tree.is_leaf():
                tree.add_feature("external_branch_length_variance", 0)
            else:
                external_brlens = []
                for node in tree.traverse("postorder"):
                    if not node.is_leaf():
                        external_brlens.append(node.dist)
                tree.add_feature("external_branch_length_variance", np.var(external_brlens))
            return tree.external_branch_length_variance

    def maximum(self, n, m, mode):
        return float("nan") 

    def minimum(self, n, m, mode):
        return float("nan")

    def imbalance(self):
        return 0

