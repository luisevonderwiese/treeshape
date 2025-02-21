from ete3 import Tree
import metrics

tree =  Tree("data/virus/trees/rooted/covid_edited.rooted.tree")
metrics.precompute(tree)
for metric_name in metrics.relative_metrics:
    print(metric_name)
    metrics.relative_normalized(metric_name, tree)
