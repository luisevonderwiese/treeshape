import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

dfs = {"lang" : pd.read_csv(os.path.join('data', 'lang', 'metrics.csv')), "bio" : pd.read_csv(os.path.join('data', 'bio', 'metrics.csv'))}
plots_dir = "data/plots/"
if not os.path.isdir(plots_dir):
    os.makedirs(plots_dir)

for metric_name in dfs["lang"].columns:
    if metric_name == "tree_name" or metric_name.startswith("Unnamed"):
        continue
    plt.xlim(0, 1)
    plt.hist([dfs["lang"][metric_name], dfs["bio"][metric_name]], weights=[np.ones(len(dfs["lang"])) / len(dfs["lang"]), np.ones(len(dfs["bio"])) / len(dfs["bio"])], label = ["lang", "bio"])
    plt.xlabel(metric_name)
    plt.ylabel("Percentage of trees")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.legend()
    plt.savefig(os.path.join(plots_dir, "hist_" + metric_name + ".png"))
    plt.clf()
