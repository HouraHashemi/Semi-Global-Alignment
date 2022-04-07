import semi
import time

if __name__ == '__main__':

	test_cases = {1: (' AAAAA',' AA'),
				  2: (' WWWTGCA',' CCTGCA'),
	 			  3: (' WWWTGCA',' CCTGCA'),
	 			  4: (' ACGTGGG',' ACGTCCC'),
	 			  5: (' HEAGAWGHE',' PAWHEA'),
	 			  6: (' CGTCCGAAGTG',' GTCGAA'),
 	 			  7: (' CACGGTCCGAA',' AACTTCGAA'),
	 			  8: (' GTCCCCCCCCC',' GTCCCCCWWWWCCC'),
	 			  9: (' ACTATATTATATATA',' ACTATATATATATA'),
	 			  10:(' ACGTACGTACGTCCCCCCCCC',' ACTGACGTCCCCCWWWWCCC')
	 			  }

	
	test = 9

	print("=============================")
	s0 = test_cases[test][0]
	s1 = test_cases[test][1]

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
	
	# CGTCCGAAGTG
	# GTCGAA
	# 20
	# CGTCCGAAGTG
	# -GT-CGAA---
	# CGTCCGAAGTG
	# -GTC-GAA---
	# CGTCCGAAGTG  
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

