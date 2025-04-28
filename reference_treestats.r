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
	
	results <- c(results, treestats::blum(tree))
	names <- c(names, "blum_statistics")
	results <- c(results, treestats::j_one(tree))
        names <- c(names, "j_one")
        results <- c(results, treestats::avg_ladder(tree))
        names <- c(names, "average_ladder")
        results <- c(results, treestats::max_ladder(tree))
        names <- c(names, "maximum_ladder")
        results <- c(results, treestats::mean_pair_dist(tree))
        names <- c(names, "mean_pairwise_distance")
        results <- c(results, treestats::var_pair_dist(tree))
        names <- c(names, "pairwise_distance_variance")
        results <- c(results, treestats::mntd(tree))
        names <- c(names, "mean_minimum_pairwise_distance")
        results <- c(results, treestats::entropy_j(tree))
        names <- c(names, "j_statistic")
        results <- c(results, treestats::phylogenetic_diversity(tree))
        names <- c(names, "phylogenetic_diversity")
        results <- c(results, treestats::mean_branch_length(tree))
        names <- c(names, "mean_branch_length")
        results <- c(results, treestats::var_branch_length(tree))
        names <- c(names, "branch_length_variance")
        results <- c(results, treestats::mean_branch_length_int(tree))
        names <- c(names, "mean_internal_branch_length")
        results <- c(results, treestats::var_branch_length_int(tree))
        names <- c(names, "internal_branch_length_variance")
        results <- c(results, treestats::mean_branch_length_ext(tree))
        names <- c(names, "mean_external_branch_length")
        results <- c(results, treestats::var_branch_length_ext(tree))
        names <- c(names, "external_branch_length_variance")
	
	data <- data.frame(names,results)
	write.csv(data,	paste("data/reference_results_treestats/", tree_name, ".csv", sep=""))
}
