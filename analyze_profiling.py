import os

from tabulate import tabulate
import util


def analyze(tree_name, python_dir, R_dir):

    d = {}
    with open(os.path.join(python_dir, "no_precompute", tree_name + ".csv"), "r") as infile:
        lines = infile.readlines()
    names = lines[0][:-1].split(",")
    times = [float(s) for s in lines[1].split(",")]
    d["precomputation"] = [0]
    for i, name in enumerate(names):
        d[name] = [times[i]]

    with open(os.path.join(python_dir, "precompute", tree_name + ".csv"), "r") as infile:
        lines = infile.readlines()
    names = lines[0][:-1].split(",")
    times = [float(s) for s in lines[1].split(",")]
    for i, name in enumerate(names):
        d[name].append(times[i])

    with open(os.path.join(R_dir, tree_name + ".csv"), "r") as infile:
        lines = infile.readlines()
    d["precomputation"].append(0)
    for line in lines[1:]:
        parts = line.split(",")
        name = parts[1].strip("\"")
        time = float(parts[2])
        d[name].append(time)

    res = [[name] + d[name] for name in names]
    print(tabulate(res, headers = ["metric", "my time", "my time precompute", "ref time"], tablefmt="pipe", floatfmt=".6f"))

tree_dir = "data/virus/trees/rooted/"
python_dir = "results/python/benchmark/virus"
R_dir = "results/treestats/benchmark/virus"

for tree_name in os.listdir(tree_dir):
    analyze(tree_name, python_dir, R_dir)
