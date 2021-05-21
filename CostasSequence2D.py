import matplotlib.pyplot as plt
import numpy as np

class CostasSequence2d:

	sequence = []	#Sequence
	length = 0		#Length of sequence
	n = 0			#Biggest entry in the sequence

	########################################################################

	#Constructors

	#########################################################################
	#Input: sequence of elements, largest entry in the sequence
	def __init__(self, seq):

		#Initializes sequence and sequence length
		self.sequence = seq
		self.length = len(seq)

		#Verifies if sequence is Costas
		#This uses the sequence and its length
		if self.is_costas():
			#Sets largest entry
			self.n = max(sorted(seq))

		#If sequence isnt costas, display error and reset values of seq and length
		else :
			self.sequence = []
			self.length = 0
			print("Error: Sequence is not Costas")

	##########################################################################

	#Costas Condition Verifiers

	#########################################################################

	#Checks if the given sequence is Costas
	#Uses difference triangle method
	def is_costas(self):
	    for h in range(1, self.length):
	        v = []
	        for i in range(self.length - h):
	            if self.sequence[i + h] - self.sequence[i] in v:
	            	# print("en false")
	            	return False 
	            else :
	                v.append(self.sequence[i + h] - self.sequence[i])
	                # print("en true")
	        # print(v)
	        
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

	##########################################################################


	#Costas Transformations

	##########################################################################

	#Inputs index by which we want to shift
	#Outputs sequence shifted to the right by index
	def cyclic_shift(self, index):
		d = [-1]*(self.length)

		for i in range(self.length):
			d[(i + index)%self.length] = self.sequence[i]

		return CostasSequence2d(d)

	#More research into this transformation is required
	#Index multiplication
	def I_multiplication(self, X):
		seq = [0]*(self.length)
		for i in range(self.length):
			va = ((i +1)*X)%(self.length + 1) - 1 
			seq[i] = self.sequence[va]
		# print(seq)
		return CostasSequence2d(seq, self.n)

	#Rotates Costas Array to the right	
	def rotate(self):
		l = inverse(self.reflect().sequence)
		return CostasSequence2d(l)

	#Reflects Costas Array along a vertical line
	def reflect(self):
		v = [0]*self.length
		for i in range(self.length):
			v[i] = self.sequence[self.length - i - 1]
		return CostasSequence2d(v)

	##########################################################################

	#Costas Display

	##########################################################################

	#Grid plot for 2d costas arrays
	def show(self):

		#Sets x values
		x = np.array([i for i in range(1, self.n + 1)])
		y = np.array(self.sequence)

		plt.xlim([0, len(x)])
		plt.ylim([0,len(x)])

		#Constructs gridlines
		for i in range(len(x)+ 1):

			plt.hlines(y=i, xmin = 0, xmax = len(x) + 1)
			plt.vlines(x =i, ymin = 0, ymax = len(x) + 1)

		#Rescales X and Y values

		X = list(map(rescale, x))
		Y = list(map(rescale, y))

		#Plots the costas array
		plt.scatter(X, Y, s = 250)
		plt.show()




#Miscellaneous functions

def rescale(v):
	v = v - .5
	return v

def inverse(list):
	inv = [0]*len(list)
	for i in range(len(list)):

		inv[list[i] - 1] = i + 1

	return inv

###########################################################################

#Tests


# C = CostasSequence2d([1,2,4,3])
# C.show()
# l = [1,5,3,2,4]
# # print([0,1,2,3,4])
# # print(l)
# C.rotate().show()
# C1 = CostasSequence2d([1,3,2])
# C2 = CostasSequence2d([1])
# print(C.sequence)
# C.show()
# print(C.reflect().sequence)
# C.reflect().show()
# print(C1.n)
# print(C.sequence)
# print("Cyclic shifts")
# for i in range(6):
	# print(C.cyclic_shift(i).sequence)
	# C.cyclic_shift(i).show()

# print(C1.cyclic_shift(1).sequence)

# print("I_multiplication")
# for i in range(1, 5):

# 	print(C.I_multiplication(i).sequence)

# C.show()