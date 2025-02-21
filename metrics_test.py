from ete3 import Tree
import os
import metrics
import math
import unittest




class TestMetrics(unittest.TestCase):
    test_tree_dir = "test_data"
    #test_tree_names = ["fischer2"]
    test_tree_names = ["fischer1", "fischer2", "fischer3", "fischer4", "fischer5", "fischer6"]

    expected = {}
    expected["fischer1"] = {
        "average_leaf_depth" : 10 / 3,
        "variance_of_leaves_depths" : 20 / 9,
        "sackin_index" : 20,
        "total_path_length" : 30,
        "total_internal_path_length" : 10,
        "average_vertex_depth" : 30 / 11,
        "B_1_index" : 25 / 12,
        "B_2_index" : 31 /16,
        "height" : 5,
        "maximum_width" : 2,
        "s_roof_shape" : math.log2(120),
        "cherry_index" : 1,
        "cophenetic_index" : 20,
        "diameter" : 6,
        "root_imbalance" : 5 / 6,
        "I_root" : 1,
        "colless_index" : 10,
        "corrected_colless_index" : 1,
        "quadratic_colless_index" : 30,
        "I_2_index" : 1,
        "stairs1" : 4 / 5,
        "stairs2" : 137 /300,
        "rogers_j_index" : 4,
        "symmetry_nodes_index" : 4,
        "mean_I" : 1,
        "total_I" : 3,
        "mean_I_prime" : 31 / 36,
        "total_I_prime" : 31 / 12,
        "mean_I_w" : 1,
        "total_I_w" : 3,
        "colijn_plazotta_rank" : 68,
        "treeness" : 0.4,
        "stemminess" : 62 / 315}

    expected["fischer2"] = {
        "average_leaf_depth" :  19 / 6,
        "variance_of_leaves_depths" : 1.472222222222,
        "sackin_index" : 19,
        "total_path_length" : 28,
        "total_internal_path_length" : 9,
        "average_vertex_depth" : 28 / 11,
        "B_1_index" : 17 / 6,
        "B_2_index" : 2,
        "height" : 4,
        "maximum_width" : 4,
        "s_roof_shape" : math.log2(60),
        "cherry_index" : 2,
        "cophenetic_index" : 18,
        "diameter" : 5,
        "root_imbalance" : 5 / 6,
        "I_root" : 1,
        "colless_index" : 7,
        "corrected_colless_index" : 0.7,
        "quadratic_colless_index" : 25,
        "I_2_index" : 0.5,
        "stairs1" : 2 / 5, 
        "stairs2" : 69 /  100,
        "rogers_j_index" : 2,
        "symmetry_nodes_index" : 2,
        "mean_I" : 2 / 3,
        "total_I" : 2,
        "mean_I_prime" : 11 / 18,
        "total_I_prime" : 11 / 6,
        "mean_I_w" : 0.55,
        "total_I_w" : 1.65,
        "colijn_plazotta_rank" : 30,
        "treeness" : 0.4,
        "stemminess" : 29/126}

    expected["fischer3"] = {
        "average_leaf_depth" : 3,
        "variance_of_leaves_depths" : 1,
        "sackin_index" : 18,
        "total_path_length" : 26,
        "total_internal_path_length" : 8,
        "average_vertex_depth" : 26 / 11,
        "B_1_index" : 17 / 6,
        "B_2_index" : 17 / 8,
        "height" : 4,
        "maximum_width" : 3,
        "s_roof_shape" : math.log2(40),
        "cherry_index" : 2,
        "cophenetic_index" : 15,
        "diameter" : 5,
        "root_imbalance" : 5 / 6,
        "I_root": 1,
        "colless_index" : 6,
        "corrected_colless_index" : 0.6,
        "quadratic_colless_index" : 18,
        "I_2_index" : 0.5833333,
        "stairs1" : 3 / 5,
        "stairs2" : 101 / 150,
        "rogers_j_index" : 3,
        "symmetry_nodes_index" : 3,
        "mean_I" : 0.5,
        "total_I" : 1,
        "mean_I_prime" : 5 / 12,
        "total_I_prime" : 5 / 6,
        "mean_I_w" : 5 / 11,
        "total_I_w" : 10 / 11,
        "colijn_plazotta_rank" : 17,
        "treeness" : 0.4,
        "stemminess" : 44/180}

    expected["fischer4"] = {
        "average_leaf_depth" : 17 /  6,
        "variance_of_leaves_depths" : 0.80555555555555555,
        "sackin_index" : 17,
        "total_path_length" : 24,
        "total_internal_path_length" : 7,
        "average_vertex_depth" : 24 / 11,
        "B_1_index" : 17 / 6,
        "B_2_index" : 19 / 8,
        "height" : 4,
        "maximum_width" : 3,
        "s_roof_shape" : math.log2(30),
        "cherry_index" :  2,
        "cophenetic_index" : 11,
        "diameter" : 6,
        "root_imbalance" : 4 / 6,
        "I_root" : 1 / 2,
        "colless_index" : 5,
        "corrected_colless_index" : 0.5,
        "quadratic_colless_index" : 9,
        "I_2_index" :  0.625,
        "stairs1" : 3 / 5,
        "stairs2" : 10 / 15,
        "rogers_j_index" :  3,
        "symmetry_nodes_index" : 3,
        "mean_I" :  0.75,
        "total_I" : 3 / 2,
        "mean_I_prime" : 7 / 12,
        "total_I_prime" :  7 / 6,
        "mean_I_w" : 14 / 19,
        "total_I_w" : 28 / 19,
        "colijn_plazotta_rank" :  13,
        "treeness" : 0.4,
        "stemminess" : 106/420}

    expected["fischer5"] = {
        "average_leaf_depth" : 16 / 6,
        "variance_of_leaves_depths" : 2 / 9,
        "sackin_index" : 16,
        "total_path_length" : 22,
        "total_internal_path_length" : 6,
        "average_vertex_depth" : 2,
        "B_1_index" :  3.5,
        "B_2_index" : 2.5,
        "height" : 3,
        "maximum_width" : 4,
        "s_roof_shape" : math.log2(15),
        "cherry_index" :  3,
        "cophenetic_index" : 9,
        "diameter" : 5,
        "root_imbalance" : 4 / 6,
        "I_root" :  1 / 2,
        "colless_index" : 2,
        "corrected_colless_index" : 0.2,
        "quadratic_colless_index" : 4,
        "I_2_index" : 0.125,
        "stairs1" : 1 / 5,
        "stairs2" : 9 / 10,
        "rogers_j_index" :  1,
        "symmetry_nodes_index" : 1,
        "mean_I" : 0.25,
        "total_I" : 0.5,
        "mean_I_prime" : 5 / 24,
        "total_I_prime" : 5 / 12,
        "mean_I_w" : 5 / 28,
        "total_I_w" : 5 / 14,
        "colijn_plazotta_rank" : 9,
        "treeness" : 0.4,
        "stemminess" : 8 / 28}

    expected["fischer6"] = {
        "average_leaf_depth" : 16 / 6,
        "variance_of_leaves_depths" : 2 / 9,
        "sackin_index" : 16,
        "total_path_length" : 22,
        "total_internal_path_length" : 6,
        "average_vertex_depth" : 2,
        "B_1_index" : 3,
        "B_2_index" : 2.5,
        "height" : 3,
        "maximum_width" : 4,
        "s_roof_shape" : math.log2(20),
        "cherry_index" : 2,
        "cophenetic_index" : 8,
        "diameter" : 6,
        "root_imbalance" : 3 / 6,
        "I_root" : 0,
        "colless_index" : 2,
        "corrected_colless_index" : 0.2,
        "quadratic_colless_index" : 2,
        "I_2_index" : 0.5,
        "stairs1" : 2 / 5,
        "stairs2" : 4 / 5,
        "rogers_j_index" : 2,
        "symmetry_nodes_index" : 2,
        "mean_I" : 0,
        "total_I" : 0,
        "mean_I_prime" : 0,
        "total_I_prime" : 0,
        "mean_I_w" : 0,
        "total_I_w" : 0,
        "colijn_plazotta_rank" : 7,
        "treeness" : 0.4,
        "stemminess" : 16 / 60}


    def test_absolute(self):
        test_trees = {}
        for test_tree_name in self.test_tree_names:
            tree = Tree(os.path.join(self.test_tree_dir, test_tree_name  +".tree"))
            metrics.precompute(tree)
            for metric_name in metrics.absolute_metrics:
                self.assertAlmostEqual(metrics.absolute(metric_name, tree), self.expected[test_tree_name][metric_name])

    def test_relative(self):
        test_trees = {}
        for test_tree_name in self.test_tree_names:
            tree = Tree(os.path.join(self.test_tree_dir, test_tree_name  +".tree"))
            metrics.precompute(tree)
            for metric_name in metrics.relative_metrics:
                metrics.relative(metric_name, tree)


if __name__ == '__main__':
    unittest.main()
