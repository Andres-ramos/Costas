#Andres Ramos Rodriguez

import sys
from sage.all import *
from collections import deque

#Class for working with Costas Sequences. 

#Todo:
#	1) Document better and clean up code
#	2) Implement Shears for dimensiones > 3
#	3) Write Tests

#Helper function del helper function de shear
#Creates vector to be added to original entry
def helper_helper(value, index, dimension):
	v = [0]*dimension
	v[index] = value
	return vector(v)



class CostasSequence:

	sequence = []
	length = 0
	dimension = 0
	n = 0

	#Instanciates sequence
	#Checks if its costas
	#Otherwise prints error
	def __init__(self, seq, n):

		if self.is_costas():
			try : 
				self.length = len(seq)
				self.n = n
				self.sequence = [0]*self.length
				#Fails if sequence is 1 dimensional
				self.dimension = len(seq[0]) + 1	
				for i in range(self.length):
					self.sequence[i] = vector(seq[i])

				

			except:
				self.dimension = 2
				self.sequence = seq
				self.length = len(seq)
				self.n = n
			
		else :
			print("Error: Sequence is not Costas")


	#Checks if the given sequence is Costas
	#Uses difference triangle method
	def is_costas(self):
	    for h in range(1, self.length):
	        v = []
	        for i in range(self.length - h):
	            if self.sequence[i + h] - self.sequence[i] in v:
	                return False 
	            else :
	                v.append(self.sequence[i + h] - self.sequence[i])
	        
	    return True

	#Outputs the difference triangle of the sequence
	def diff_triangle(self):
		T = []
		for h in range(1, self.length):
			v = []
			for i in range(self.length - h):
				v.append((self.sequence[i + h] - self.sequence[i]))
			T.append(v)

		return T

	#Inputs index by which we want to shift
	#Outputs sequence shifted to the right by index
	def cyclic_shift(self, index):
		d = [-1]*(self.length)

		for i in range(self.length):
			d[(i + index)%self.length] = self.sequence[i]
		return CostasSequence(d, self.n)

	#Input: vector dimension m if self is m+1 dimensional costas
	#Output: row-column mult of the costas sequence by the input
	def RC_multiplication(self, vector):

		print(sorted(vector))
		#Input validation. Checks if entries in vector bigger than 0
		if sorted(vector)[0] > 0:

			nseq = [0]*self.length
			for i in range(self.length):
				row = [0]*(self.dimension - 1)
				for j in range(self.dimension - 1):
					# print(self.sequence[i][j], "*", vector[j])
					row[j] = ((self.sequence[i][j]*vector[j])%self.n)
				# print(row)
				nseq[i] = row

			return CostasSequence(nseq, self.n)

		else :
			print("Error: RC multiplication defined for non-zero entries\n")
			

	#Returns costas sequence of self multiplied by m
	#Needs input validation for m (has to be relatively prime to self.length)
	def multiplication(self, m):

		if gcd(m, self.length) == 1:
			nseq = [0]*self.length
			for i in range(self.length):
				nseq = [self.sequence[(i*m)%self.length] for i in range(self.length)]
			return CostasSequence(nseq, self.n)

		else :
			print("Error: input must be comprime to the length")					# print(vector)
					# print(self.sequence)


	#Helper function for shear
	#El (index + 1)%2 es un terrible hacky fix que no va a funcionar si se trata de generalizar
	def helper_shear(self, m, index):
		v = [(vector(self.sequence[i]) + 
			helper_helper(self.sequence[i][(index + 1)%2]*m[index], index, self.dimension-1))%self.n
			for i in range(self.length)]
		return CostasSequence(v, self.n)
 
	#Hardcoded for dimension 3 (sequence of vectors of size 2)
	#Write the case for higher dimensions
	def shear(self, vector):

		#Checks vector has positive entries
		if sorted(vector)[0] >= 0:
			#Checks if dimensions match
			if self.dimension - 1 == len(vector):

				if self.dimension == 3:
					#Aqui para tres dimensiones
					# nseq = [0]*self.length
					c = self
					for i in range(len(vector)):
						if vector[i] != 0 :
							v = [0]*len(vector)
							v[i] = vector[i]
							c = c.helper_shear(v, i)
					return c
					
				else :
					print("Error: Function only implemented for 3 dimensions")
			else :
				print("Error: Dimensions of vector and costas sequence must match")
		else :
			print("Error: Shear only defined for non-negative entries")


	#Prints costas sequence in 2 and 3 dimensions
	def show(self):
		if self.dimension == 2:
			print(self.sequence)
		elif self.dimension == 3:
			M = self.make_matrix()
			print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in M]))
		else :
			print("Function not implemented for dimension > 3")
		#Implement for 2d, 3d y tira error por more dimensions
		return 


	def make_matrix(self):
		if self.dimension == 3:
			M = [[None]*self.n for i in range(self.n)]
			for i in range(self.length):
				x = int(self.sequence[i][1])
				y = int(self.sequence[i][0])

				M[x][y] = i 
			new_M = [M[len(M) - 1 - i] for i in range(self.n)]
			return new_M

		else :
			print("Error: Not implemented for dimensions other than 3")

	def decompose(self, special_value):
		nseq = []
		for i in range(self.length):
			if i < special_value:
				nseq.append([self.sequence[i]])
			else :
				nseq[i%special_value].append(self.sequence[i])
		return nseq



