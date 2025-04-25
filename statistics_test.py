from ete3 import Tree
import os
import math
import unittest
import pandas as pd

from treebalance import TreeBalance
import indexlists




class TestMetrics(unittest.TestCase):
    tree_dir = "test_data/"

    def test(self):
        test_trees = {}
        for test_tree_name in os.listdir(self.tree_dir):
            tree = Tree(os.path.join(self.tree_dir, test_tree_name))
            tb_b = TreeBalance(tree, "BINARY")
            tb_a = TreeBalance(tree, "ARBITRARY")
            for index_name in indexlists.statistics_indices:
                tb_b.absolute(index_name)

if __name__ == '__main__':
    unittest.main()
