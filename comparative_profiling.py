from ete3 import Tree
import time
import os

from treebalance import TreeBalance
import indexlists
import util

treename = "covid_edited.rooted.tree"
treepath = os.path.join("data/virus/trees/rooted/", treename)

times = []
for index_name in indexlists.treebalance_indices:
    print(index_name)
    tree =  Tree(treepath)
    tb = TreeBalance(tree, "BINARY")
    start = time.time()
    tb.absolute(index_name)
    end = time.time()
    times.append(end - start)
if not os.path.isdir("data/comp_treebalance_profiling/"):
    os.makedirs("data/comp_treebalance_profiling/")
with open("data/comp_treebalance_profiling/" + treename + ".csv", "w+") as outfile:
    outfile.write(",".join(indexlists.treebalance_indices) + "\n")
    outfile.write(",".join([str(time) for time in times]) + "\n")

times = []
for index_name in indexlists.treestats_indices:
    print(index_name)
    tree =  Tree(treepath)
    tb = TreeBalance(tree, "BINARY")
    start = time.time()
    tb.absolute(index_name)
    end = time.time()
    times.append(end - start)
if not os.path.isdir("data/comp_treestats_profiling/"):
    os.makedirs("data/comp_treestats_profiling/")
with open("data/comp_treestats_profiling/" + treename + ".csv", "w+") as outfile:
    outfile.write(",".join(indexlists.treestats_indices) + "\n")
    outfile.write(",".join([str(time) for time in times]) + "\n")


tree =  Tree(treepath)
util.precompute_clade_sizes(tree)
util.precompute_depths(tree)
util.precompute_pw_distances_efficient(tree)
tb = TreeBalance(tree, "BINARY")


times = []
for index_name in indexlists.treebalance_indices:
    print(index_name)
    start = time.time()
    tb.absolute(index_name)
    end = time.time()
    times.append(end - start)
if not os.path.isdir("data/comp_treebalance_profiling_precompute/"):
    os.makedirs("data/comp_treebalance_profiling_precompute/")
with open("data/comp_treebalance_profiling_precompute/" + treename + ".csv", "w+") as outfile:
    outfile.write(",".join(indexlists.treebalance_indices) + "\n")
    outfile.write(",".join([str(time) for time in times]) + "\n")

times = []
for index_name in indexlists.treestats_indices:
    print(index_name)
    start = time.time()
    tb.absolute(index_name)
    end = time.time()
    times.append(end - start)
if not os.path.isdir("data/comp_treestats_profiling_precompute/"):
    os.makedirs("data/comp_treestats_profiling_precompute/")
with open("data/comp_treestats_profiling_precompute/" + treename + ".csv", "w+") as outfile:
    outfile.write(",".join(indexlists.treestats_indices) + "\n")
    outfile.write(",".join([str(time) for time in times]) + "\n")

