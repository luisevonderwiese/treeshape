from tabulate import tabulate
import util

tree_name = "covid_edited.rooted.tree"
d = {}
with open("data/comp_treestats_profiling/" + tree_name + ".csv", "r") as infile:
    lines = infile.readlines()
names = lines[0][:-1].split(",")
times = [float(s) for s in lines[1].split(",")]
for i, name in enumerate(names):
    d[name] = [times[i]]

with open("data/comp_treestats_profiling_precompute/" + tree_name + ".csv", "r") as infile:
    lines = infile.readlines()
names = lines[0][:-1].split(",")
times = [float(s) for s in lines[1].split(",")]
for i, name in enumerate(names):
    d[name].append(times[i])

with open("data/treestats_profiling/" + tree_name + ".csv", "r") as infile:
    lines = infile.readlines()
for line in lines[1:]:
    parts = line.split(",")
    name = parts[1].strip("\"")
    time = float(parts[2])
    d[name].append(time)

res = [[name] + d[name] for name in names]
print(tabulate(res, headers = ["metric", "my time", "my time precompute", "ref time"], tablefmt="pipe", floatfmt=".6f"))
