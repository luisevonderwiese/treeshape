from ete3 import Tree
import metrics
import time

tree =  Tree("data/virus/trees/rooted/covid_edited.rooted.tree")
start = time.time()
for metric_name in metrics.R_metrics:
    print(metric_name)
    metrics.absolute(metric_name, tree)
end = time.time()
print("Metric Evaluation:", str(end - start))
