from ete3 import Tree
import metrics

tree =  Tree("data/virus/trees/rooted/covid_edited.rooted.tree")
for metric_name in metrics.absolute_metrics:
    print(metric_name)
    metrics.absolute(metric_name, tree, "BINARY")
