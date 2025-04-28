import numpy as np

import util

from tree_index import TreeIndex
from depth_indices import SackinIndex
from cophenetic_indices import TotalCopheneticIndex


class Diameter(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.diameter
        except AttributeError:
            if tree.is_leaf(): #single-node-tree
                tree.add_feature("diameter", 0)
            else:
                max_d = 0
                deepest_leaf = None
                for leaf in tree.iter_leaves():
                    if util.depth(tree, leaf) > max_d:
                        max_d = util.depth(tree, leaf)
                        deepest_leaf = leaf
                max_d = 0
                for leaf in tree.iter_leaves():
                    max_d = max(max_d, util.connecting_path_length(tree, deepest_leaf, leaf))
                tree.add_feature("diameter", max_d)
            return tree.diameter

    def maximum(self, n, m, mode):
        return n

    def minimum(self, n, m, mode):
        if mode == "BINARY":
            return float("nan")
        if mode == "ARBITRARY":
            if n == 1:
                return 0
            return 2

    def imbalance(self):
        return 0


class AreaPerPairIndex(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.area_per_pair_index
        except AttributeError:
            n = util.clade_size(tree, tree)
            if n == 1:
                tree.add_feature("area_per_pair_index", 0)
            else:
                s = SackinIndex().evaluate(tree, mode)
                c = TotalCopheneticIndex().evaluate(tree, mode)
                tree.add_feature("area_per_pair_index", 2 / n * s - 4 / (n * (n - 1)) * c)
            return tree.area_per_pair_index

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 0

class MeanPairwiseDistance(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.mean_pairwise_distance
        except AttributeError:
            try:
                tree.all_pw_distances
            except AttributeError:
                util.precompute_pw_distances_efficient(tree)
            tree.add_feature("mean_pairwise_distance", sum(tree.all_pw_distances) / len(tree.all_pw_distances))
            return tree.mean_pairwise_distance

    def maximum(self, n, m, mode):
        return float('nan') 

    def minimum(self, n, m, mode):
        return float('nan') 

    def imbalance(self):
        return 1

class PairwiseDistanceVariance(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.pairwise_distance_variance
        except AttributeError:
            try:
               tree.all_pw_distances 
            except AttributeError:
                util.precompute_pw_distances_efficient(tree)
            tree.add_feature("pairwise_distance_variance", np.var(tree.all_pw_distances))
            return tree.pairwise_distance_variance

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 1

class MeanMinimumPairwiseDistance(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.mean_minimum_pairwise_distance
        except AttributeError:
            try:
                tree.all_pw_distances
            except AttributeError:
                util.precompute_pw_distances_efficient(tree)
            minimum_distances = []
            for leaf in tree.get_leaves():
                minimum_distances.append(min(leaf.pw_distances.values()))
            tree.add_feature("mean_minimum_pairwise_distance", sum(minimum_distances) / len(minimum_distances))
            return tree.mean_minimum_pairwise_distance

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 1

class JStatistic(TreeIndex):
    def evaluate(self, tree, mode):
        try:
            return tree.j_statistic
        except AttributeError:
            try:
                tree.all_pw_distances
            except AttributeError:
                util.precompute_pw_distances_efficient(tree)
            s = len(tree.get_leaves())
            print(s)
            d = ((s+1) * (s-1) * s) / 4 
            tree.add_feature("j_statistic", sum(tree.all_pw_distances) / d)
            return tree.j_statistic

    def maximum(self, n, m, mode):
        return float('nan')

    def minimum(self, n, m, mode):
        return float('nan')

    def imbalance(self):
        return 1

