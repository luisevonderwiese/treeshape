tree_names <- c("covid_edited.rooted.tree", 
		#"nextstrain_ncov_gisaid_global_all-time_timetree.nwk", 
		#"flu_seasonal_h1n1pdm_ha_2y_timetree.nwk", 
		#"nextstrain_rsv_a_genome_timetree.nwk", 
		#"flu_seasonal_h3n2_ha_2y_timetree.nwk", 
		#"nextstrain_seasonal-flu_h3n2_ha_12y_timetree.nwk", 
		#"nextstrain_avian-flu_h9n2_ha_all-time_timetree.nwk", 
		"sequences_rsv_a_treeseq_al_ed.rooted.tree", 
		#"nextstrain_measles_genome_timetree.nwk", 
		"sequences_rsv_b_treeseq_al_ed.rooted.tree")
for (tree_name in tree_names) {
	print(tree_name)
	tree <- ape::read.tree(paste("data/virus/trees/rooted/", tree_name, sep=""))
	results <- c()
	names <- c()
	times <- c()

	start.time <- Sys.time()
	results <- c(results, treestats::area_per_pair(tree))
	names <- c(names, "area_per_pair_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::average_leaf_depth(tree))
	names <- c(names, "average_leaf_depth")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::avg_ladder(tree))
	names <- c(names, "average_ladder")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::avg_vert_depth(tree))
	names <- c(names, "average_vertex_depth")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::b1(tree))
	names <- c(names, "B_1_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::b2(tree))
	names <- c(names, "B_2_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::blum(tree))
	names <- c(names, "s_shape")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::cherries(tree))
	names <- c(names, "cherry_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::colless(tree))
	names <- c(names, "colless_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::colless_corr(tree))
	names <- c(names, "corrected_colless_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::colless_quad(tree))
	names <- c(names, "quadratic_colless_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::diameter(tree))
	names <- c(names, "diameter")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::ew_colless(tree))
	names <- c(names, "I_2_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::mean_i(tree))
	names <- c(names, "mean_I_prime")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::j_one(tree))
	names <- c(names, "j_one")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::j_stat(tree))
	#names <- c(names, "blum_statistic")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::max_del_width(tree))
	names <- c(names, "maxdiff_widths")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::max_depth(tree))
	names <- c(names, "maximum_depth")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)
	
	start.time <- Sys.time()
	results <- c(results, treestats::max_ladder(tree))
	names <- c(names, "maximum_ladder")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::max_width(tree))
	names <- c(names, "maximum_width")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::mean_branch_length(tree))
	#names <- c(names, "mean_branch_length")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)
	
	#start.time <- Sys.time()
	#results <- c(results, treestats::mean_branch_length_ext(tree))
	#names <- c(names, "mean_external_branch_length")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)
	
	#start.time <- Sys.time()
	#results <- c(results, treestats::mean_branch_length_int(tree))
	#names <- c(names, "mean_internal_branch_length")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::mntd(tree))
	names <- c(names, "mean_minimum_pairwise_distance")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::mean_pair_dist(tree))
	#names <- c(names, "mean_pairwise_distance")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::mw_over_md(tree))
	names <- c(names, "max_width_over_max_depth")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::phylogenetic_diversity(tree))
	#names <- c(names, "phylogenetic_diversity")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::rogers(tree))
	names <- c(names, "rogers_j_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::root_imbalance(tree))
	names <- c(names, "root_imbalance")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::rquartet(tree))
	names <- c(names, "rooted_quartet_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::sackin(tree))
	names <- c(names, "sackin_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::stairs(tree))
	names <- c(names, "stairs1")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::stairs2(tree))
	names <- c(names, "stairs2")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)
	
	start.time <- Sys.time()
	results <- c(results, treestats::sym_nodes(tree))
	names <- c(names, "symmetry_nodes_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::tot_coph(tree))
	names <- c(names, "total_cophenetic_index")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::tot_internal_path(tree))
	names <- c(names, "total_internal_path_length")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::tot_path_length(tree))
	names <- c(names, "total_path_length")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::treeness(tree))
	names <- c(names, "treeness")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::var_branch_length(tree))
	#names <- c(names, "branch_length_variance")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::var_branch_length_ext(tree))
	#names <- c(names, "external_branch_length_variance")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::var_branch_length_int(tree))
	#names <- c(names, "internal_branch_length_variance")
        #end.time <- Sys.time()
        #times <- c(times, end.time - start.time)

	start.time <- Sys.time()
	results <- c(results, treestats::var_leaf_depth(tree))
	names <- c(names, "variance_of_leaves_depths")
        end.time <- Sys.time()
        times <- c(times, end.time - start.time)

	#start.time <- Sys.time()
	#results <- c(results, treestats::vpd(tree))
	#names <- c(names, "pairwise_distance_variance")
	#end.time <- Sys.time()
	#times <- c(times, end.time - start.time)


	data <- data.frame(names,results)
	write.csv(data,	paste("data/treestats_results/", tree_name, ".csv", sep=""))
	data <- data.frame(names,times)
        write.csv(data, paste("data/treestats_profiling/", tree_name, ".csv", sep=""))

}
