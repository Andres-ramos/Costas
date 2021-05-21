import sys
import os

sys.path.append(".")
from CostasSequences import *
from CostasSequence2D import *
from sage.all import *

#############################################################################
#Costas Construct uses Welch Construction to construct Costas Sequences of #length p^m - 1 for some prime p and any dimension m


#Todo:
#   1) Implement Lempel-Golomb Construction for 2 dimensions
##############################################################################


#Converts polynomial list into vectors into corresponding vectors
#Input: Polynomial list and the dimension
#Output: Vector list corresponding to the polynomials

#Example: [2x^2 + 3x + 10] -> [2,3,10]

#Can be modularized further
def PolyListToVector(PolyList, dimension):
    C = []#
    #Iterates over polynomial list
    for l in PolyList:
        #Uses Sage built in function to convert to list
        a = l.polynomial().list()
        #If there are zero coefficients, fills the list with zeroes
        if len(a) < dimension:
            for i in range(0, dimension - len(a)):
                a.append(0)

        #Reverse list
        point = vector(list(reversed(a)))
        C.append(point)

    return C

#Uses Welch Construction in 2D to create Costas Sequence of length p - 1
#Input: Multiplicative generator of the finite field Fp and prime number
#Output: Welch Costas Sequence

#Example: For alpha = 2 and p = 5,
#       
#       [2^0, 2^1, 2^2, 2^3] = [1,2,4,3]
#

def CreateWelch2D(alpha, prime):
    return [alpha^(i)for i in range(prime - 1)]

#Uses multidimensional Welch Construcction to create a polynomial list that #corresponds to a multidimensional Costas Sequence
#Input: Generator alpha, prime p and dimension m
#Output: M dimensional Costas sequence 

def CreateWelchMD(alpha, prime, dimension):
    poly_list = [alpha^(i) for i in range(prime^dimension-1)]
    return PolyListToVector(poly_list,  dimension)

#Construts Welch Costas Sequence of specified prime and dimension
def CostasConstructor(prime, dimension):
    n = prime^dimension
    F.<a>= FiniteField(n, 'x')

    if dimension > 1 :
        CostasSeq = CreateWelchMD(a, prime, dimension)
        return CostasSequence(CostasSeq, prime, dimension)

    #dimension 2
    else :
        a = F.multiplicative_generator()
        CostasSeq = CreateWelch2D(a, prime)
        return CostasSequence2d(CostasSeq, prime - 1)


