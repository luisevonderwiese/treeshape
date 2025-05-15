import math
import numpy as np
from collections import Counter

def leaf_depths(tree):
    return [depth(tree, leaf) for leaf in tree.iter_leaves()]

def clade_size(tree, v):
    try:
        return v.clade_size
    except AttributeError:
        precompute_clade_sizes(tree)
        return v.clade_size

def depth(tree, v):
    try:
        return v.depth
    except AttributeError:
        precompute_depths(tree)
        return v.depth

def precompute_clade_sizes(tree):
    for node in tree.traverse("postorder"):
        if node.is_leaf():
            node.add_feature("clade_size", 1)
            continue
        c = node.children
        node.add_feature("clade_size", sum([child.clade_size for child in c]))


def precompute_depths(tree):
    tree.add_feature("depth", 0)
    depths_recursive(tree)

def depths_recursive(tree):
    c = tree.children
    d = tree.depth + 1
    for child in c:
        child.add_feature("depth", d)
        if not child.is_leaf():
            depths_recursive(child)


def widths(tree):
    return Counter([depth(tree, v) for v in tree.traverse("postorder")])

def connecting_path_length(tree, v1, v2):
    ancestor = tree.get_common_ancestor(v1, v2)
    return depth(tree, v1) + depth(tree, v2) - 2 * depth(tree, ancestor)

def inner_nodes(tree):
    inner_nodes = []
    for v in tree.traverse("postorder"):
        if not v.is_leaf():
            inner_nodes.append(v)
    return inner_nodes


def balance_index(tree, v):
    if v.is_leaf():
        return 0
    c = v.children
    assert (len(c) == 2)
    return abs(clade_size(tree, c[0]) - clade_size(tree, c[1]))

def precompute_probs(tree):
    tree.add_feature("prob", 1)
    probs_recursive(tree)

def probs_recursive(tree):
    if tree.is_leaf():
        return
    c = tree.children
    p = tree.prob / len(c)
    for child in c:
        child.add_feature("prob", p)
        if not child.is_leaf():
            probs_recursive(child)

def precompute_heights(tree):
    for node in tree.iter_descendants("postorder"):
        if node.is_leaf():
            node.add_feature("height", 0)
            continue
        c = node.children
        h = 1 + max([child.height for child in c])
        node.add_feature("height", h)

def we(x):
    lookup = [0, 1, 1, 1, 2, 3, 6, 11, 23, 46, 98, 207, 451, \
            983, 2179, 4850, 10905, 24631, 56011, 127912, \
            293547, 676157, 1563372, 3626149, 8436379, \
            19680277, 46026618, 107890609, 253450711, \
            596572387, 1406818759, 3323236238, 7862958391, \
            18632325319, 44214569100]
    if x >= len(lookup):
        raise NotImplementedError("WE Number not provided for " + str(x))
    return lookup[x]

def furnas_ranks(tree):
    for node in tree.traverse("postorder"):
        if node.is_leaf():
            node.add_feature("furnas_rank", 1)
            continue
        c = node.children
        assert (len(c) == 2)
        if clade_size(tree, c[0]) <= clade_size(tree, c[1]):
            f_l = c[0].furnas_rank
            alpha = clade_size(tree, c[0])
            f_r = c[1].furnas_rank
            beta = clade_size(tree, c[1])
        else:
            f_l = c[1].furnas_rank
            alpha = clade_size(tree, c[1])
            f_r = c[0].furnas_rank
            beta = clade_size(tree, c[0])
        s = 0
        for i in range(1, alpha):
            try:
                s += we(i) * we(clade_size(tree, node) - i)
            except NotImplementedError:
                node.add_feature("furnas_rank", float("nan"))
                continue
        try:
            s += (f_l - 1) * we(beta) + f_r
        except NotImplementedError:
            node.add_feature("furnas_rank", float("nan"))
            continue
        if alpha == beta:
            s -= (f_l * f_l - f_l) / 2
        node.add_feature("furnas_rank", s)


def isomorphic(v1, v2):
    if v1.is_leaf():
        return v2.is_leaf()
    if v2.is_leaf():
        return False
    c1 = v1.children
    assert (len(c1) == 2)
    c2 = v2.children
    assert (len(c2) == 2)
    return (isomorphic(c1[0], c2[0]) and isomorphic(c1[1], c2[1])) or (isomorphic(c1[0], c2[1]) and isomorphic(c1[1], c2[0]))



def I_value(tree, v):
    c = v.children
    assert (len(c) == 2)
    n_v1 = max(clade_size(tree, c[0]), clade_size(tree, c[1]))
    n_v = clade_size(tree, v)
    half = math.ceil(n_v / 2.0)
    if (n_v - 1 - half) == 0:
        return 0
    return (n_v1 - half) / (n_v - 1 - half)

def I_prime(tree, v):
    I_v = I_value(tree, v)
    n_v = clade_size(tree, v)
    if n_v > 0 and n_v % 2 == 0:
        I_v *= (n_v - 1) / n_v
    return I_v


def I_weight(tree, v):
    n_v = clade_size(tree, v)
    if n_v % 2 == 1:
        return 1
    if n_v == 0:
        return 0
    I_v = I_value(tree, v)
    if I_v == 0:
        return (2 * (n_v - 1)) / n_v
    return (n_v - 1) / n_v

def I_weight_sum(tree):
    weights = []
    for node in tree.traverse("postorder"):
        if clade_size(tree, node) >= 4:
            weights.append(I_weight(tree, node))
    return sum(weights) / len(weights)

def I_w(tree, v, sw):
    return (I_weight(tree, v) * I_value(tree, v)) / sw


def I_values(tree, mode, sw = 0):
    assert(mode in ["I", "I_prime", "I_w"])
    values = []
    for node in tree.traverse("postorder"):
        if clade_size(tree, node) >= 4:
            if mode == "I":
                values.append(I_value(tree, node))
            elif mode == "I_prime":
                values.append(I_prime(tree, node))
            elif mode == "I_w":
                values.append(I_w(tree, node, sw))
    return values

def E_l(n, Xset):
    if n > len(Xset):
        return 0
    if n == len(Xset):
        return math.prod(Xset)
    if n == 1:
        return sum(Xset)
    P = [sum([math.pow(val, x) for val in Xset]) for x in range(1, n+1)]
    mat = [[0 for _ in range(n)] for __ in range(n)]
    for x in range(n):
        mat[x][:x + 1] = P[:x+1][::-1]
    for x in range(n - 1):
        mat[x][x+1] = x + 1
    return np.linalg.det(mat) / math.factorial(n)

def precompute_rqi(tree):
    q = range(5)
    q = [q[0]] + [q[i] - q[0] for i in range(1, 5)]
    for node in tree.traverse("postorder"):
        if node.is_leaf():
            node.add_feature("ypsilon", 0)
            node.add_feature("rooted_quartet_index", 0)
            continue
        n_v = clade_size(tree, node)
        c = node.children
        ccs = [clade_size(tree, child) for child in c]
        E3 = E_l(3, ccs)
        E4 = E_l(4, ccs)
        node.add_feature("ypsilon", sum([child.ypsilon for child in c]) + E3)
        rqi = sum([child.rooted_quartet_index for child in c])
        rqi += q[4] * E4 #star
        rqi += q[3] * E_l(2, [math.comb(cs, 2) for cs in ccs]) #fully balanced
        rqi += q[2] * (clade_size(tree, node) * (node.ypsilon - E3) - \
                sum([clade_size(tree, child) * child.ypsilon for child in c])) #3-pitchfork  + 1
        rqi += q[1] * (0.5 * E3 * E_l(1, ccs) - 2 * E4 - 1.5 * E3) # cherry + 2
        node.add_feature("rooted_quartet_index", rqi)
    tree.rooted_quartet_index = tree.rooted_quartet_index + q[0] * math.comb(clade_size(tree, tree), 4)


def colijn_plazotta_recursive(node):
    if node.is_leaf():
        node.add_feature("colijn_plazotta_rank", 1)
        return
    c = node.children
    assert len(c) == 2
    colijn_plazotta_recursive(c[0])
    colijn_plazotta_recursive(c[1])
    if c[0].colijn_plazotta_rank >= c[1].colijn_plazotta_rank:
        node.add_feature("colijn_plazotta_rank", 0.5 * c[0].colijn_plazotta_rank * (c[0].colijn_plazotta_rank - 1) + c[1].colijn_plazotta_rank + 1)
    else:
        node.add_feature("colijn_plazotta_rank", 0.5 * c[1].colijn_plazotta_rank * (c[1].colijn_plazotta_rank - 1) + c[0].colijn_plazotta_rank + 1)


def is_bifurcating(tree):
    try: #check if heights already precomputed
        return tree.bifurcating
    except AttributeError:
        tree.add_feature("bifurcating", bifurcating_recursive(tree))
        return tree.bifurcating

def bifurcating_recursive(tree):
    c = tree.children
    if len(c) == 2:
        return bifurcating_recursive(c[0]) and bifurcating_recursive(c[1])
    if len(c) == 0:
        return True
    return False
