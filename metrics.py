from ete3 import Tree
import math
import numpy as np
absolute_metrics =[
    "average_leaf_depth",
    "variance_of_leaves_depths",
    "sackin_index",
    "B_1_index",
    "B_2_index",
    "height",
    "maximum_width",
    "s_roof_shape",
    "cherry_index",
    "cophenetic_index",
    "diameter",
    "root_imbalance",
    "I_root",
    "colless_index",
    "corrected_colless_index",
    "quadratic_colless_index",
    "I_2_index",
    "stairs",
    "rogers_j_index",
    "symmetry_nodes_index",
    "mean_I",
    "total_I",
    "mean_I_prime",
    "total_I_prime",
    "mean_I_w",
    "total_I_w",
    "colijn_plazotta_rank"]


relative_metrics = [
    "average_leaf_depth",
    "sackin_index",
    "B_2_index",
    "height",
    "cherry_index",
    "cophenetic_index",
    "root_imbalance",
    "I_root",
    "colless_index",
    "quadratic_colless_index",
    "rogers_j_index",
    "symmetry_nodes_index"]
#============ GENERAL ============

def height(tree):
    return max(leaf_depths(tree))

def width(tree, i):
    leaf_depths(tree).count(i)

def depths_in_subtree(node, depth):
    depths_below = []
    for child in node.children:
        if child.is_leaf():
            depths_below.append(depth + 1)
        else:
            depths_below += depths_in_subtree(child, depth + 1)
    return depths_below

def leaf_depths(tree):
    return depths_in_subtree(tree, 0)

def clade_size(v):
    return len(v)


def lca(tree, v1, v2):
    if tree == v1 or tree == v2:
        return tree
    if tree.is_leaf():
        return None
    c = tree.children
    assert(len(c) == 2)
    left_lca = lca(c[0], v1, v2)
    right_lca = lca(c[1], v1, v2)
    if left_lca and right_lca:
        return tree
    return left_lca if left_lca is not None else right_lca

def connecting_path_length(tree, v1, v2):
    ancestor = lca(tree, v1, v2)
    length = 0
    while(v1 != ancestor):
        v1 = v1.up
        length += 1
    while(v2 != ancestor):
        v2 = v2.up
        length += 1
    return length

def node_depth(tree, v):
    depth = 0
    while(v != tree):
        v = v.up
        depth += 1
    return depth

def inner_nodes(tree):
    inner_nodes = []
    for v in tree.traverse("postorder"):
        if not v.is_leaf():
            inner_nodes.append(v)
    return inner_nodes


def cophenetic_value(tree, v1, v2):
    return node_depth(tree, lca(tree, v1, v2))

def balance_index(tree, v):
    if v.is_leaf():
        return 0
    else:
        c = v.children
        assert(len(c) == 2)
        return abs(clade_size(c[0]) - clade_size(c[1]))

def prob(tree, v):
    if tree.is_leaf():
        if tree == v:
            return 1
        else:
            return 0
    c = tree.children
    assert(len(c) == 2)
    return 0.5 * prob(c[0], v) + 0.5 * prob(c[1], v)


def isomorphic(v1, v2):
    if v1.is_leaf():
        return v2.is_leaf()
    if v2.is_leaf():
        return False
    c1 = v1.children
    c2 = v2.children
    return (isomorphic(c1[0], c2[0]) and isomorphic(c1[1], c2[1])) or (isomorphic(c1[0], c2[1]) and isomorphic(c1[1], c2[0]))


def depth_counts(tree):
    counts = []
    if tree.is_leaf():
        return [1]
    else:
        counts.append(0)
        c = tree.children
        counts_l = depth_counts(c[0])
        for (i, l_count) in enumerate(counts_l):
            while len(counts) < i+2:
                counts.append(0)
            counts[i+1] += l_count
        counts_r = depth_counts(c[1])
        for (i, r_count) in enumerate(counts_r):
            while len(counts) < i+2:
                counts.append(0)
            counts[i+1] += r_count
    return counts


def I(v):
    assert(not v.is_leaf())
    c = v.children
    assert(len(c) == 2)
    n_v1 = max(clade_size(c[0]), clade_size(c[1]))
    n_v = clade_size(v)
    half = math.ceil(n_v / 2.0)
    if (n_v - 1 - half) == 0:
        return 0
    return (n_v1 - half) / (n_v - 1 - half)

def I_prime(v):
    I_value = I(v)
    n_v = clade_size(v)
    if n_v > 0 and n_v % 2 == 0:
        I_value *= (n_v - 1) / n_v
    return I_value


def I_weight(v):
    n_v = clade_size(v)
    if n_v % 2 == 1:
        return 1
    if n_v == 0:
        return 0
    I_v = I(v)
    if I_v == 0:
        return (2 * (n_v - 1)) / n_v
    else:
        return (n_v - 1) / n_v

def I_weight_sum(tree):
    weights = []
    for node in tree.traverse("postorder"):
        if clade_size(node) >= 4:
            weights.append(I_weight(node))
    return sum(weights) / len(weights)

def I_w(v, sw):
    return (I_weight(v) * I(v)) / sw


def I_values(tree, mode, sw = 0):
    assert(mode in ["I", "I_prime", "I_w"])
    values = []
    for node in tree.traverse("postorder"):
        if clade_size(node) >= 4:
            if mode == "I":
                values.append(I(node))
            elif mode == "I_prime":
                values.append(I_prime(node))
            elif mode == "I_w":
                values.append(I_w(node, sw))
    return values

#============ ABSOLUTE METRICS ============

def absolute(metric_name, tree):
    if not metric_name in absolute_metrics:
        print(metric_name, " is not an implemented absolute metric!")
        return
    match metric_name:
        case "average_leaf_depth":
            depths = leaf_depths(tree)
            return sum(depths) / len(depths)

        case "variance_of_leaves_depths":
            return np.var(leaf_depths(tree))

        case "sackin_index":
            return sum(leaf_depths(tree))

        case "B_1_index":
            s = 0
            for node in tree.iter_descendants("postorder"):
                if not node.is_leaf():
                    s += 1 / height(node)
            return s

        case "B_2_index":
            s = 0
            for leaf in tree.iter_leaves():
                p_leaf = prob(tree, leaf)
                s += p_leaf * math.log2(p_leaf)
            return - s

        case "height":
            return height(tree)

        case "maximum_width":
            return max(depth_counts(tree))

        case "s_roof_shape":
            s = 0
            for node in tree.traverse("postorder"):
                if not node.is_leaf():
                    s += math.log2(clade_size(node) - 1)
            return s

        case "cherry_index":
            cnt = 0
            for node in tree.traverse("postorder"):
                if node.is_leaf():
                    continue
                c = node.children
                if c[0].is_leaf() and c[1].is_leaf():
                    cnt += 1
            return cnt

        case "cophenetic_index":
            leaves = [l for l in tree.iter_leaves()]
            s = 0
            for i, node1 in enumerate(leaves):
                for j in range(i):
                    node2 = leaves[j]
                    s += cophenetic_value(tree, node1, node2)
            return s

        case "diameter":
            leaves = [l for l in tree.iter_leaves()]
            m = 0
            for i, node1 in enumerate(leaves):
                for j in range(i):
                    node2 = leaves[j]
                    m = max(m, connecting_path_length(tree, node1, node2))
            return m

        case "root_imbalance":
            c = tree.children
            return max(clade_size(c[0]), clade_size(c[1])) / clade_size(tree)

        case "I_root":
            return I(tree)

        case "colless_index":
            s = 0
            for node in tree.traverse("postorder"):
                if not node.is_leaf():
                    s += balance_index(tree, node)
            return s

        case "corrected_colless_index":
            n = len(tree)
            return (2 * absolute("colless_index", tree)) / ((n-1) * (n-2))

        case "quadratic_colless_index":
            s = 0
            for node in tree.traverse("postorder"):
                if not node.is_leaf():
                    b = balance_index(tree, node)
                    s += b * b
            return s

        case "I_2_index":
            n = clade_size(tree)
            s = 0
            for node in tree.traverse("postorder"):
                n_v = clade_size(node)
                if n_v > 2:
                    b = balance_index(tree, node)
                    s += b / (n_v - 2)
            return s / (n - 2)

        case "stairs":
            s = 0
            for node in tree.traverse("postorder"):
                if node.is_leaf():
                    continue
                c = node.children
                n0 = clade_size(c[0])
                n1 = clade_size(c[1])
                s += min(n0, n1) / max(n0, n1)
            return s / (clade_size(tree) - 1)

        case "rogers_j_index":
            s = 0
            for node in tree.traverse("postorder"):
                if not node.is_leaf():
                    if balance_index(tree, node) != 0:
                        s += 1
            return s

        case "symmetry_nodes_index":
            cnt = 0
            for node in tree.traverse("postorder"):
                if not node.is_leaf():
                    c = node.children
                    if not isomorphic(c[0], c[1]):
                        cnt += 1
            return cnt

        case "mean_I":
            values = I_values(tree, "I")
            return sum(values) / len(values)

        case "total_I":
            return sum(I_values(tree, "I"))

        case "mean_I_prime":
            values = I_values(tree, "I_prime")
            return sum(values) / len(values)

        case "total_I_prime":
            return sum(I_values(tree, "I_prime"))

        case "mean_I_w":
            sw = I_weight_sum(tree)
            values = I_values(tree, "I_w", sw)
            return sum(values) / len(values)

        case "total_I_w":
            sw = I_weight_sum(tree)
            return sum(I_values(tree, "I_w", sw))

        case "colijn_plazotta_rank":
            if clade_size(tree) == 1:
                return 1
            c = tree.children
            assert(len(c) == 2)
            cp1 = absolute("colijn_plazotta_rank", c[0])
            cp2 = absolute("colijn_plazotta_rank", c[1])
            if cp1 >= cp2:
                return 0.5 * cp1 * (cp1 - 1) + cp2 + 1
            else:
                return 0.5 * cp2 * (cp2 - 1) + cp1 + 1



def relative(metric_name, tree):
    if not metric_name in relative_metrics:
        print(metric_name, " is not an implemented absolute metric!")
        return
    v = absolute(metric_name, tree)
    n = clade_size(tree)
    min_v = minimum(metric_name, n)
    max_v = maximum(metric_name, n)
    if max_v == min_v:
        return float('nan')
    if max_v - v < -0.00001:
        print("Value above max for", metric_name)
        print("max_v:", str(max_v))
        print("v:", str(v))
        assert(False)
    if v - min_v < -0.00001:
        print("Value below min for", metric_name)
        print("min_v:", str(min_v))
        print("v:", str(v))
        assert(False)
    return (v - min_v) / (max_v - min_v)


def maximum(metric_name, n):
    match metric_name:
        case "average_leaf_depth":
            m = n-1
            return m - (((m - 1) * m) / (2 * n))

        case "variance_of_leaves_depths":
            return float('nan') #no tight minimum for binary trees
            #return ((n - 1) * (n - 2) * (n*n + 3*n -6)) / (12 * n * n)

        case "sackin_index":
            m = n - 1
            return (n * m) - (((m - 1) * m) / 2)

        case "B_1_index":
            return float('nan')

        case "B_2_index":
            x  = math.floor(math.log2(n))
            pow_x = math.pow(2, x)
            return x + ((n - pow_x) / pow_x)

        case "height":
            return n - 1

        case "maximum_width":
            return float('nan')

        case "s_roof_shape":
            return float('nan')
            #return math.log2(math.factorial(n - 1)) # problem with minimum

        case "cherry_index":
            return math.floor(n / 2)

        case "cophenetic_index":
            return math.comb(n, 3)

        case "diameter":
            return float('nan')
            #return n #problem with min

        case "root_imbalance":
            return (n - 1) / n

        case "I_root":
            return 1

        case "colless_index":
            return ((n - 1) * (n - 2)) / 2

        case "corrected_colless_index":
            return float('nan')
            #return 1 #use colleess instead

        case "quadratic_colless_index":
            return math.comb(n, 3) + math.comb(n - 1, 3)

        case "I_2_index":
            return float('nan')
            #return 1 problem with miimum

        case "stairs":
            return float('nan')
            #return sum([1 / i for i in range(1, n)]) / (n - 1) (holds for caterpillar but is not the maximum)

        case "rogers_j_index":
            return max(0, n - 2)

        case "symmetry_nodes_index":
            return n - 2

        case "mean_I":
            return float('nan')

        case "total_I":
            return float('nan')

        case "mean_I_prime":
            return float('nan')

        case "total_I_prime":
            return float('nan')

        case "mean_I_w":
            return float('nan')

        case "total_I_w":
            return float('nan')

        case "colijn_plazotta_rank":
            return float('nan')


def minimum(metric_name, n):
    match metric_name:
        case "average_leaf_depth":
            x = math.floor(math.log2(n / 2))
            return  x + 3 - (2 / n) * math.pow(2, x + 1)

        case "variance_of_leaves_depths":
            return float('nan')
            #return 0 #bound only tight for general trees

        case "sackin_index":
            x = math.floor(math.log2(n / 2))
            return (x + 3) * n - math.pow(2, x + 2)

        case "B_1_index":
            return float('nan')

        case "B_2_index":
            return 2 - math.pow(2, 2 - n)

        case "height":
            return math.floor(math.log2(n)) + 1

        case "maximum_width":
            return float('nan')
            #return 2 #problem with maximum

        case "s_roof_shape":
            return float('nan')

        case "cherry_index":
            return 1

        case "cophenetic_index":
            factorial = 1
            a = 1
            s = 0
            for i in range(n):
                if i != 0:
                    factorial += i
                while factorial % (a * 2) == 0:
                    a *= 2
                s += a
            return 0

        case "diameter":
            return float('nan')
            #highest_1_bit = math.floor(math.log2(n))
            #lowest_1_bit = math.log2(n & -n) + 1
            #if highest_1_bit == lowest_1_bit or bin(n).count('1'):
            #    inbetween = 0
            #else:
            #    inbetween = minimum("diameter", n1)
            #return highest_1_bit + inbetween + lowest_1_bit

        case "root_imbalance":
            return math.ceil(n / 2) / n

        case "I_root":
            return 0

        case "colless_index":
            sum_bound = math.ceil(math.log2(n))
            s = 0
            for j in range(1, sum_bound):
                x = math.pow(2, -j) * n
                triangle_wave = min(math.ceil(x) - x, x - math.floor(x))
                s += math.pow(2, j) * triangle_wave
            return s

        case "corrected_colless_index":
            return float('nan')
            #return (2 / ((n - 1) * (n - 2))) * minimum("colless_index", n) #noramlize colless instead

        case "quadratic_colless_index":
            sum_bound = math.ceil(math.log2(n))
            s = 0
            for j in range(1, sum_bound):
                x = math.pow(2, -j) * n
                triangle_wave = min(math.ceil(x) - x, x - math.floor(x))
                s += math.pow(2, j) * triangle_wave
            return s

        case "I_2_index":
            return float("nan")

        case "stairs":
            return float('nan')
            return 0 #problem with maximum

        case "rogers_j_index":
            return bin(n).count("1") - 1

        case "symmetry_nodes_index":
            return  bin(n).count("1") - 1

        case "mean_I":
            return float('nan')

        case "total_I":
            return float('nan')

        case "mean_I_prime":
            return float('nan')

        case "total_I_prime":
            return float('nan')

        case "mean_I_w":
            return float('nan')

        case "total_I_w":
            return float('nan')

        case "colijn_plazotta_rank":
            return float('nan')
