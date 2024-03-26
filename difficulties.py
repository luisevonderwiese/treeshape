import os
import pythia
import pandas as pd
import metrics
from tabulate import tabulate
from scipy import stats



def run_pythia():
    msa_dir = "data/bio/msa"
    output_dir = "data/bio/pythia"
    results = {}
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    for msa_name in os.listdir(msa_dir):
        msa_path = os.path.join(msa_dir, msa_name)
        name = ".".join(msa_name.split(".")[:-1])
        prefix = os.path.join(output_dir, name)
        pythia.run_with_padding(msa_path, prefix)
        results[name + ".rooted.tree"] = pythia.get_difficulty(prefix)
    df = pd.DataFrame(results.items(), columns=['name', 'difficulty'])
    df.to_csv('data/bio/difficulties.csv', index = False)


    msa_dir = "data/lang/lingdata/generated/msa"
    output_dir = "data/lang/pythia"
    results = {}
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    for msa_subdir in os.listdir(msa_dir):
        msa_path = os.path.join(msa_dir, msa_subdir, "bin.phy")
        ds_id = msa_subdir.split("_")[0]
        prefix = os.path.join(output_dir, ds_id)
        #pythia.run_with_padding(msa_path, prefix)
        results[ds_id + ".rooted.tree"] = pythia.get_difficulty(prefix)
    df = pd.DataFrame(results.items(), columns=['name', 'difficulty'])
    df.to_csv('data/lang/difficulties.csv', index = False)


def correlations():
    for type in ["lang", "bio"]:
        metrics_df = pd.read_csv(os.path.join("data", type, "metrics.csv"))
        difficulties_df = pd.read_csv(os.path.join("data", type, "difficulties.csv"))
        df = metrics_df.merge(difficulties_df, left_on = 'tree_name', right_on='name', how='inner', suffixes=(False, False))
        result = []
        for metric_name in metrics.relative_metrics:
            part_r = [metric_name]
            mini_df = df[["difficulty", metric_name]]
            mini_df = mini_df.dropna()
            pearson = stats.pearsonr(mini_df['difficulty'], mini_df[metric_name])
            part_r.append(pearson[0])
            part_r.append(pearson[1])
            result.append(part_r)
        print("Correlation of tree metrics with difficulty in", type, "data")
        print(tabulate(result, tablefmt="pipe", floatfmt=".3f", headers = ["column", "pearson correlation", "p-value"]))



#run_pythia()
correlations()
