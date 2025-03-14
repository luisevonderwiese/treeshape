import os
import pandas as pd
from ete3 import Tree

from treebalance import TreeBalance
import indexlists

dfs = {}
trees_dir = "data/virus/trees/rooted"
tree_names = []
for tree_name in os.listdir(trees_dir):
    tree_file_name = os.path.join(trees_dir, tree_name)
    if os.path.isfile(tree_file_name):
        tree_names.append(tree_name)
df = pd.DataFrame(tree_names, columns=["tree_name"])

for i, row in df.iterrows():
    tree =  Tree(os.path.join(trees_dir, row["tree_name"]))
    tb = TreeBalance(tree, "ARBITRARY")
    print(row["tree_name"])
    for index_name in indexlists.all_indices:
        print(index_name)
        try:
            df.at[i, index_name] = round(tb.relative(index_name), 3)
        except ValueError as e:
            print(e)
            continue
print(df)
df.to_csv("data/virus/metrics.csv")
