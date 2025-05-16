import os
import matplotlib.pyplot as plt
from tabulate import tabulate
import util


def analyze(tree_name, python_dir, R_dir):
    d = {}
    with open(os.path.join(python_dir, "no_precompute", tree_name + ".csv"), "r") as infile:
        lines = infile.readlines()
    names = lines[0][:-1].split(",")
    times = [float(s) for s in lines[1].split(",")]
    d["precomputation"] = {}
    d["precomputation"]["no_precompute"] = 0
    for i, name in enumerate(names):
        d[name] = {}
        d[name]["no_precompute"] = times[i]

    with open(os.path.join(python_dir, "precompute", tree_name + ".csv"), "r") as infile:
        lines = infile.readlines()
    names = lines[0][:-1].split(",")
    times = [float(s) for s in lines[1].split(",")]
    for i, name in enumerate(names):
        d[name]["precompute"] = times[i]

    with open(os.path.join(R_dir, tree_name + ".csv"), "r") as infile:
        lines = infile.readlines()
    d["precomputation"]["R"] = 0
    for line in lines[1:]:
        parts = line.split(",")
        name = parts[1].strip("\"")
        time = float(parts[2])
        d[name]["R"] = time
    return d

def boxplots(all_times, plots_dir):
    if not os.path.isdir(plots_dir):
        os.makedirs(plots_dir)
    for index, times in all_times.items():
        fig, ax = plt.subplots()
        ax.boxplot(times.values())
        ax.set_xticklabels(times.keys())
        plt.savefig(os.path.join(plots_dir, index + ".png"))

tree_dir = "data/virus/trees/rooted/"
python_dir = "results/python/benchmark/virus"
R_dir = "results/treestats/benchmark/virus"

all_times = {}
for tree_name in os.listdir(tree_dir):
    times = analyze(tree_name, python_dir, R_dir)
    if len(all_times) == 0:
        for index, subtimes in times.items():
            all_times[index] = {}
            for mode, time in subtimes.items():
                all_times[index][mode] = [time]
    else:
        for index, sub_times in times.items():
            for mode, time in subtimes.items():
                all_times[index][mode].append(time)
boxplots(all_times, "results/plots/benchmark/virus")

        
