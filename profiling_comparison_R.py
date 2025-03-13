from ete3 import Tree
import time

from treebalance import TreeBalance
import indexlists

tree =  Tree("data/virus/trees/rooted/covid_edited.rooted.tree")
tb = TreeBalance(tree, "BINARY")
start = time.time()
for index_name in indexlists.R_implemented_indices:
    print(index_name)
    tb.absolute(index_name)
end = time.time()
print("Index Evaluation:", str(end - start))
