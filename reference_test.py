from ete3 import Tree
import os
import metrics
import math
import unittest
import pandas as pd




class TestMetrics(unittest.TestCase):
    ref_dir = "reference_results"
    tree_names = ["covid_edited"]
    expected = {}
    for tree_name in tree_names:
        df = pd.read_csv(os.path.join(ref_dir, tree_name + ".csv"))
        results = {}
        for i, row in df.iterrows():
            results[row["names"]] = float(row["results"])
        expected[tree_name] = results

    def test(self):
        test_trees = {}
        for test_tree_name in self.tree_names:
            tree = Tree(os.path.join("data/virus/trees/rooted", test_tree_name + ".rooted.tree"))
            for metric_name in metrics.R_metrics:
                print(metric_name)
                try:
                    self.assertAlmostEqual(metrics.absolute(metric_name, tree, "BINARY"), self.expected[test_tree_name][metric_name])
                except ValueError as e:
                    print(e)
                    self.assertAlmostEqual(metrics.absolute(metric_name, tree, "ARBITRARY"), self.expected[test_tree_name][metric_name])


if __name__ == '__main__':
    unittest.main()
