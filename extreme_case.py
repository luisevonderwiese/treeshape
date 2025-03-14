from ete3 import Tree
from treebalance import TreeBalance
import indexlists

tree =  Tree("A;")
tb_b = TreeBalance(tree, "BINARY")
tb_a = TreeBalance(tree, "ARBITRARY")

for index_name in indexlists.all_indices:
    print(index_name)
    try:
        print(tb_b.absolute(index_name))
    except ValueError as e:
        print(e)
    try:
        print(tb_a.absolute(index_name))
    except ValueError as e:
        print(e)
    try:
        print(tb_b.relative(index_name))
    except ValueError as e:
        print(e)
    try:
        print(tb_a.relative(index_name))
    except ValueError as e:
        print(e)
