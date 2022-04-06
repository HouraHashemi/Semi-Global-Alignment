import copy
import numpy as np
import time

class dynamic_semi_global_alignment():
	

	gap_penalty, score = 9, 0
	score_matrix = np.empty
	n, m, pairs = list(), list(), list()
	paths = dict()
	s0,s1 = str(), str()

	"""
	PAM: Point Accepted Mutation
	"""
	PAM250 = {
		'A': {'A':  2, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N':  0, 'P':  1, 'Q':  0, 'R': -2, 'S':  1, 'T':  1, 'V':  0, 'W': -6, 'Y': -3},
		'C': {'A': -2, 'C': 12, 'D': -5, 'E':-5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S':  0, 'T': -2, 'V': -2, 'W': -8, 'Y':  0},
		'D': {'A':  0, 'C': -5, 'D':  4, 'E': 3, 'F': -6, 'G':  1, 'H':  1, 'I': -2, 'K':  0, 'L': -4, 'M': -3, 'N':  2, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
		'E': {'A':  0, 'C': -5, 'D':  3, 'E': 4, 'F': -5, 'G':  0, 'H':  1, 'I': -2, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
		'F': {'A': -3, 'C': -4, 'D': -6, 'E':-5, 'F':  9, 'G': -5, 'H': -2, 'I':  1, 'K': -5, 'L':  2, 'M':  0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W':  0, 'Y':  7},
		'G': {'A':  1, 'C': -3, 'D':  1, 'E': 0, 'F': -5, 'G':  5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N':  0, 'P':  0, 'Q': -1, 'R': -3, 'S':  1, 'T':  0, 'V': -1, 'W': -7, 'Y': -5},
		'H': {'A': -1, 'C': -3, 'D':  1, 'E': 1, 'F': -2, 'G': -2, 'H':  6, 'I': -2, 'K':  0, 'L': -2, 'M': -2, 'N':  2, 'P':  0, 'Q':  3, 'R':  2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y':  0},
		'I': {'A': -1, 'C': -2, 'D': -2, 'E':-2, 'F':  1, 'G': -3, 'H': -2, 'I':  5, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -5, 'Y': -1},
		'K': {'A': -1, 'C': -5, 'D':  0, 'E': 0, 'F': -5, 'G': -2, 'H':  0, 'I': -2, 'K':  5, 'L': -3, 'M':  0, 'N':  1, 'P': -1, 'Q':  1, 'R':  3, 'S':  0, 'T':  0, 'V': -2, 'W': -3, 'Y': -4},
		'L': {'A': -2, 'C': -6, 'D': -4, 'E':-3, 'F':  2, 'G': -4, 'H': -2, 'I':  2, 'K': -3, 'L':  6, 'M':  4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V':  2, 'W': -2, 'Y': -1},
		'M': {'A': -1, 'C': -5, 'D': -3, 'E':-2, 'F':  0, 'G': -3, 'H': -2, 'I':  2, 'K':  0, 'L':  4, 'M':  6, 'N': -2, 'P': -2, 'Q': -1, 'R':  0, 'S': -2, 'T': -1, 'V':  2, 'W': -4, 'Y': -2},
		'N': {'A':  0, 'C': -4, 'D':  2, 'E': 1, 'F': -3, 'G':  0, 'H':  2, 'I': -2, 'K':  1, 'L': -3, 'M': -2, 'N':  2, 'P':  0, 'Q':  1, 'R':  0, 'S':  1, 'T':  0, 'V': -2, 'W': -4, 'Y': -2},
		'P': {'A':  1, 'C': -3, 'D': -1, 'E':-1, 'F': -5, 'G':  0, 'H':  0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N':  0, 'P':  6, 'Q':  0, 'R':  0, 'S':  1, 'T':  0, 'V': -1, 'W': -6, 'Y': -5},
		'Q': {'A':  0, 'C': -5, 'D':  2, 'E': 2, 'F': -5, 'G': -1, 'H':  3, 'I': -2, 'K':  1, 'L': -2, 'M': -1, 'N':  1, 'P':  0, 'Q':  4, 'R':  1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
		'R': {'A': -2, 'C': -4, 'D': -1, 'E':-1, 'F': -4, 'G': -3, 'H':  2, 'I': -2, 'K':  3, 'L': -3, 'M':  0, 'N':  0, 'P':  0, 'Q':  1, 'R':  6, 'S':  0, 'T': -1, 'V': -2, 'W':  2, 'Y': -4},
		'S': {'A':  1, 'C':  0, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P':  1, 'Q': -1, 'R':  0, 'S':  2, 'T':  1, 'V': -1, 'W': -2, 'Y': -3},
		'T': {'A':  1, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  0, 'H': -1, 'I':  0, 'K':  0, 'L': -2, 'M': -1, 'N':  0, 'P':  0, 'Q': -1, 'R': -1, 'S':  1, 'T':  3, 'V':  0, 'W': -5, 'Y': -3},
		'V': {'A':  0, 'C': -2, 'D': -2, 'E':-2, 'F': -1, 'G': -1, 'H': -2, 'I':  4, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -6, 'Y': -2},
		'W': {'A': -6, 'C': -8, 'D': -7, 'E':-7, 'F':  0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R':  2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y':  0},
		'Y': {'A': -3, 'C':  0, 'D': -4, 'E':-4, 'F':  7, 'G': -5, 'H':  0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W':  0, 'Y': 10}
		}

		

	def __init__(self,s0,s1):
		self.s0 = s0
		self.s1 = s1
		self.initialize_matrix()


	def initialize_matrix(self):
		# Shift strings one char for adding aditional one row and one column to matrix
		if len(self.s0) < len(self.s1):
			self.n, self.m = self.s0, self.s1
		else:
			self.n, self.m = self.s1, self.s0
		self.score_matrix = np.zeros((len(self.n), len(self.m)))


	def calculate_cells_of_score_matrix(self):
		# Create score_matrix
		for i in range(1, len(self.n)):
			for j in range(1, len(self.m)):
			
				N, M = self.n[i], self.m[j]
				# print(N,M,i,j,self.PAM250[N][M])		
				score = max(
							self.score_matrix[i-1][j-1] + self.PAM250[N][M],
							self.score_matrix[i-1][j] - self.gap_penalty,
							self.score_matrix[i][j-1] - self.gap_penalty
							)
				
				self.score_matrix[i][j] = score
		# print(self.score_matrix)
			
		# Check last row and last column for the maximum value
		max_coor_roots = list()
		last_row = self.score_matrix[len(self.n)-1]
		last_col = self.score_matrix[:,len(self.m)-1]
		
		self.score = max(np.amax(last_row),np.amax(last_col))
		max_coor_roots_row =[(len(self.n)-1, coor) for coor in np.array(np.where(last_row == self.score))[0]]
		max_coor_roots_col =[(coor, len(self.m)-1) for coor in np.array(np.where(last_col == self.score))[0]]
		max_coor_roots = list(set(max_coor_roots_row + max_coor_roots_col))
		
		# Return list of start coordinates
		return max_coor_roots


	def trace_back(self, coordinates):
		for coor in coordinates:
			coor_value = self.score_matrix[coor[0]][coor[1]]
			# print(coor, coor_value)
			if (coor_value <= 0):
				pass
			else:
				N, M = self.n[coor[0]], self.m[coor[1]]
				max_score = max(
							self.score_matrix[coor[0]-1][coor[1]-1] + self.PAM250[N][M],
							self.score_matrix[coor[0]-1][coor[1]]-self.gap_penalty,
							self.score_matrix[coor[0]][coor[1]-1]-self.gap_penalty
							)

				max_coordinates = list()
				if self.score_matrix[coor[0]-1][coor[1]-1]+ self.PAM250[N][M] == int(max_score):
					max_coordinates.append((coor[0]-1,coor[1]-1))
				
				if (self.score_matrix[coor[0]-1][coor[1]]-self.gap_penalty) == int(max_score):
					max_coordinates.append((coor[0]-1,coor[1]))

				if (self.score_matrix[coor[0]][coor[1]-1]-self.gap_penalty) == int(max_score):
					max_coordinates.append((coor[0],coor[1]-1))

				# Save connections between nodes
				self.paths[coor] = max_coordinates
				self.trace_back(max_coordinates)

		return None


	def generate_branch_of_paths(self,roots):
		branches = list()
		for root in roots:
			branch = self.find_all_paths(root,list())
			if len(branch) == 0:
				pass
			else:
				branches = branches + branch
		return branches


	# function to generate all possible paths
	def find_all_paths(self, start, path):
		path = path + [start]
		if start not in self.paths:
			return [path]
		paths = []
		for node in self.paths[start]:
			if node not in path:
				newpaths = self.find_all_paths(node, path)
			for newpath in newpaths:
				paths.append(newpath)
		return paths
	   


	def generate_sequent(self,all_paths):
		for path in all_paths:
			n_seq , m_seq = list(), list()

			# Gaps of before alignment
			n_before = list(self.n[1:path[-1][0]+1])
			m_before = list(self.m[1:path[-1][1]+1])

			if len(m_before) > len(n_before):
				n_before = ['-' for i in range(len(m_before)-len(n_before))] + n_before
			elif len(m_before) < len(n_before):
				m_before = ['-' for i in range(len(n_before)-len(m_before))] + m_before
			else:
				pass

			# Alignment
			for node in path[:-1]:
				next_node = path[path.index(node)+1]
	
				ni, mi = node[0], node[1]
				nxt_ni, nxt_mi = next_node[0], next_node[1]
				
				if (abs(ni - nxt_ni) == 1) and (abs(mi - nxt_mi) == 1):   # to diagon
					n_seq = [self.n[ni]] + n_seq
					m_seq = [self.m[mi]] + m_seq
				elif (abs(ni - nxt_ni) == 0) and (abs(mi - nxt_mi) == 1): # to left
					n_seq = ['-'] + n_seq
					m_seq = [self.m[mi]] + m_seq
				elif (abs(ni - nxt_ni) == 1) and (abs(mi - nxt_mi) == 0): # to up
					n_seq = [self.n[ni]] + n_seq
					m_seq = ['-'] + m_seq
				else:
					pass

			# Gaps of after alignment
			n_after = list(self.n[path[0][0]+1:len(self.n)])
			m_after = list(self.m[path[0][1]+1:len(self.m)])
			
			if len(m_after) > len(n_after):
				n_after = ['-' for i in range(len(m_after)-len(n_after))] + n_after
			elif len(m_after) < len(n_after):
				m_after = ['-' for i in range(len(n_after)-len(m_after))] + m_after
			else:
				pass

			# Generate pairs of string
			n_string = "".join(n_before+n_seq+n_after)
			m_string = "".join(m_before+m_seq+m_after)			
			if (self.n == self.s0) and (self.m == self.s1):
				self.pairs.append((n_string,m_string))
			else:
				self.pairs.append((m_string,n_string))

		self.pairs = list(set(self.pairs))
		# print(self.pairs)


	def print_pairs(self):
		print(int(self.score))
		sortedSeq = [i[0]+i[1] for i in self.pairs]
		sortedSeq.sort()
		for i in sortedSeq:
		    print(i[0:int(len(i)/2)])
		    print(i[int(len(i)/2):])
		return True


# ================================================================


if __name__ == '__main__':	
	s0, s1 = list(' ' + input()), list(' ' + input())

	dsga = dynamic_semi_global_alignment(s0, s1)
	roots_coordinates = dsga.calculate_cells_of_score_matrix()
	dsga.trace_back(roots_coordinates)
	all_paths = dsga.generate_branch_of_paths(roots_coordinates)
	dsga.generate_sequent(all_paths)
	dsga.print_pairs()


