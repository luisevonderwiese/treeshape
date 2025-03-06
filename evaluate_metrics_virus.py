import os
import pandas as pd
from ete3 import Tree
import metrics

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
    print(row["tree_name"])
    for metric_name in metrics.relative_metrics:
        print(metric_name)
        df.at[i, metric_name] = round(metrics.relative_normalized(metric_name, tree), 3)
print(df)
df.to_csv("data/virus/metrics.csv")
