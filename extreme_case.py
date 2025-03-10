from ete3 import Tree
import metrics

tree =  Tree("A;")
for metric_name in metrics.absolute_metrics:
    print(metric_name)
    try:
        print(metrics.absolute(metric_name, tree, "BINARY"))
    except ValueError as e:
        print(e)
    try:
        print(metrics.relative(metric_name, tree, "BINARY"))
    except ValueError as e:
        print(e)
    try:
        print(metrics.relative(metric_name, tree, "ARBITRARY"))
    except ValueError as e:
        print(e)
