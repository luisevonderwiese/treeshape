import math

import treeshape.depth_indices as depth_indices
import treeshape.width_indices as width_indices
import treeshape.structure_indices as structure_indices
import treeshape.subgraph_indices as subgraph_indices
import treeshape.distance_indices as distance_indices
import treeshape.network_indices as network_indices
import treeshape.root_indices as root_indices
import treeshape.node_indices as node_indices
import treeshape.Ibased_indices as Ibased_indices
import treeshape.ranking_indices as ranking_indices
import treeshape.branchlength_indices as branchlength_indices
import treeshape.util as util


class TreeShape:
    def __init__(self, tree, mode):
        if mode not in ["BINARY", "ARBITRARY"]:
            raise ValueError(f"Unknown mode: {mode}")
        if mode == "BINARY" and not util.is_bifurcating(tree):
            raise ValueError("BINARY mode only possible for strictly bifurcating trees")
        self.mode = mode
        self.tree = tree
        self.n = len(tree)
        if mode == "BINARY":
            self.m = self.n - 1
        else:
            self.m = len([node for node in tree.traverse()]) - self.n
        self.indices = {}

    def index(self, index_name):
        if index_name not in self.indices:
            instance = self.index_instance(index_name)
            if instance is None:
                raise ValueError(f"Unknown index: {index_name}")
            self.indices[index_name] = instance
        return self.indices[index_name]

    def absolute(self, index_name):
        return self.index(index_name).evaluate(self.tree, self.mode)

    def relative(self, index_name):
        v = self.absolute(index_name)
        min_v = self.index(index_name).minimum(self.n, self.m, self.mode)
        max_v = self.index(index_name).maximum(self.n, self.m, self.mode)
        if math.isnan(min_v) or math.isnan(max_v):
            raise ValueError(index_name + " cannot be normalized for " + self.mode.lower() + " trees")
        if min_v == max_v:
            raise ValueError("Minimum equals maximum for " + index_name +  " for " + self.mode.lower() + " trees")
        if max_v - v < -0.00001:
            raise ArithmeticError("Value above maximum for " + index_name)
        if v - min_v < -0.00001:
            raise ArithmeticError("Value below minimum for " + index_name)
        return (v - min_v) / (max_v - min_v)


    def relative_normalized(self, index_name):
        rel = self.relative(index_name)
        factor = self.index(index_name).imbalance()
        if factor == 0:
            raise ValueError(index_name + " cannot be normalized as it is no (im)balance index")
        rel = self.relative(index_name)
        if factor == -1: # index is a balance index
            return 1 - rel
        return rel # index is an imbalance index


    def index_instance(self, index_name):
        match index_name:
            case "average_leaf_depth":
                return depth_indices.AverageLeafDepth()
            case "variance_of_leaves_depths":
                return depth_indices.VarianceOfLeavesDepths()
            case "sackin_index":
                return depth_indices.SackinIndex()
            case "total_path_length":
                return depth_indices.TotalPathLength()
            case "total_internal_path_length":
                return depth_indices.TotalInternalPathLength()
            case "average_vertex_depth":
                return depth_indices.AverageVertexDepth()
            case "maximum_depth":
                return depth_indices.MaximumDepth()
            case "B_1_index":
                return depth_indices.B1Index()
            case "B_2_index":
                return depth_indices.B2Index()
            case "maximum_width":
                return width_indices.MaximumWidth()
            case "maxdiff_widths":
                return width_indices.MaxdiffWidths()
            case "modified_maxdiff_widths":
                return width_indices.ModifiedMaxdiffWidths()
            case "max_width_over_max_depth":
                return width_indices.MaxWidthOverMaxDepth()
            case "s_shape":
                return structure_indices.SShape()
            case "d_index":
                return structure_indices.DIndex()
            case "rooted_quartet_index":
                return structure_indices.RootedQuartetIndex()
            case "ladder_length":
                return structure_indices.LadderLength()
            case "IL_number":
                return structure_indices.ILNumber()
            case "cherry_index":
                return subgraph_indices.CherryIndex()
            case "modified_cherry_index":
                return subgraph_indices.ModifiedCherryIndex()
            case "pitchforks":
                return subgraph_indices.Pitchforks()
            case "four_caterpillars":
                return subgraph_indices.FourCaterpillars()
            case "double_cherries":
                return subgraph_indices.DoubleCherries()
            case "total_cophenetic_index":
                return distance_indices.TotalCopheneticIndex()
            case "diameter":
                return distance_indices.Diameter()
            case "area_per_pair_index":
                return distance_indices.AreaPerPairIndex()
            case "wiener_index":
                return network_indices.WienerIndex()
            case "minimum_farness":
                return network_indices.MinimumFarness()
            case "maximum_farness":
                return network_indices.MaximumFarness()
            case "total_farness":
                return network_indices.TotalFarness()
            case "root_imbalance":
                return root_indices.RootImbalance()
            case "I_root":
                return root_indices.IRoot()
            case "colless_index":
                return node_indices.CollessIndex()
            case "corrected_colless_index":
                return node_indices.CorrectedCollessIndex()
            case "quadratic_colless_index":
                return node_indices.QuadraticCollessIndex()
            case "I_2_index":
                return node_indices.I2Index()
            case "stairs1":
                return node_indices.Stairs1()
            case "stairs2":
                return node_indices.Stairs2()
            case "rogers_j_index":
                return node_indices.RogersJIndex()
            case "symmetry_nodes_index":
                return node_indices.SymmetryNodesIndex()
            case "mean_I":
                return Ibased_indices.MeanI()
            case "total_I":
                return Ibased_indices.TotalI()
            case "mean_I_prime":
                return Ibased_indices.MeanIPrime()
            case "total_I_prime":
                return Ibased_indices.TotalIPrime()
            case "mean_I_w":
                return Ibased_indices.MeanIW()
            case "total_I_w":
                return Ibased_indices.TotalIW()
            case "colijn_plazotta_rank":
                return ranking_indices.ColijnPlazottaRank()
            case "furnas_rank":
                return ranking_indices.FurnasRank()
            case "treeness":
                return branchlength_indices.Treeness()
            case "stemminess":
                return branchlength_indices.Stemminess()

        return None
