from ete3 import Tree
import metrics

tree =  Tree("data/virus/trees/rooted/covid_edited.rooted.tree")
tree = metrics.precompute_clade_sizes(tree)
for metric_name in metrics.relative_metrics:
    #if metric_name == "cophenetic_index":
    #    continue
    print(metric_name)
    metrics.relative_normalized(metric_name, tree)
