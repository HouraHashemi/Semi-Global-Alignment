import semi
import time

if __name__ == '__main__':

	test_case = [(' AAAAA',' AA'),
				 (' AAPAAAIAA',' AA'),
	 			 (' WWWTGCA',' CCTGCA'),
	 			 (' ACGTGGG',' ACGTCCC'),
	 			 (' HEAGAWGHE',' PAWHEA'),
 	 			 (' CACGGTCCGAA',' AACTTCGAA'),
	 			 (' GTCCCCCCCCC',' GTCCCCCWWWWCCC'),
	 			 (' ACTATATTATATATA',' ACTATATATATATA'),
	 			 (' ACGTACGTACGTCCCCCCCCC',' ACTGACGTCCCCCWWWWCCC')
	 			 ]

		
	s0 = test_case[0][0]
	s1 = test_case[0][1]

	dsga = semi.dynamic_semi_global_alignment(s0, s1)
	roots_coordinates = dsga.calculate_cells_of_score_matrix()
	dsga.trace_back(roots_coordinates)
	all_paths = dsga.generate_branch_of_paths(roots_coordinates)
	dsga.generate_sequent(all_paths)
	dsga.print_pairs()
	print("=============================")


	# =============================
	# AAAAA
	# AA
	# 4
	# AAAAA
	# ---AA
	# AAAAA
	# --AA-
	# AAAAA
	# -AA--
	# AAAAA
	# AA---

	# =============================

	# AAPAAAIAA
	# AA
	# 4
	# AAPAAAIAA
	# -------AA
	# AAPAAAIAA
	# ----AA---
	# AAPAAAIAA
	# ---AA----
	# AAPAAAIAA
	# AA-------
	# =============================

	# WWWTGCA
	# CCTGCA
	# 10
	# WWWTGCA----
	# -----CCTGCA
	# WWWTGCA---
	# ----CCTGCA
	# =============================
	
	# ACGTGGG
	# ACGTCCC
	# 13
	# ACGTGGG
	# ACGTCCC
	# =============================

	# ACGTWWW
	# ACGTCCC
	# 10
	#-----ACGTWWW
	# ACGTCCC-----
	# =============================

	# HEAGAWGHE
	# PAWHEA
	# 20
	# HEAGAWGHE-
	# ---PAW-HEA
	# =============================

	# CACGGTCCGAA
	# AACTTCGAA
	# 23
	# --C-ACGGTCCGAA
	# AACTTCGAA-----
	# --CA-CGGTCCGAA
	# AACTTCGAA-----
	# =============================
	
	# GTCCCCCCCCC
	# GTCCCCCWWWWCCC
	# 69
	# GTCCCCC---CCCC
	# GTCCCCCWWWWCCC
	# GTCCCCC--C-CCC
	# GTCCCCCWWWWCCC
	# GTCCCCC-C--CCC
	# GTCCCCCWWWWCCC
	# GTCCCCCC---CCC
	# GTCCCCCWWWWCCC
	# =============================

	# ACTATATTATATATA
	# ACTATATATATATA
	# ACTATATTATATATA
	# ACTATATATATATA
	# 35
	# ACTATATTATATATA
	# ACTATA-TATATATA
	# ACTATATTATATATA
	# ACTATAT-ATATATA
	# =============================

	# ACGTACGTACGTCCCCCCCCC
	# ACTGACGTCCCCCWWWWCCC'
	# 97
	# ACGTACGTACGTCCCCC---CCCC
	# ----ACTGACGTCCCCCWWWWCCC
	# ACGTACGTACGTCCCCC--C-CCC
	# ----ACTGACGTCCCCCWWWWCCC
	# ACGTACGTACGTCCCCC-C--CCC
	# ----ACTGACGTCCCCCWWWWCCC
	# ACGTACGTACGTCCCCCC---CCC
	# ----ACTGACGTCCCCCWWWWCCC
	# =============================


