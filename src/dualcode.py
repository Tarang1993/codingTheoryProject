from math import *

codes = []
inputK = 0
dualK = 0
inputN = 0
dualN = 0
dualD = 0

def generateInputCodes():

	# Open the input file to read the Generator matrix of binary linear code [n, k, d]
	fid = open('input.txt', 'r')
	inputK = fid.readlines()
	inputN= len(inputK)
	generator_codes = []

	for i in range(0, len(inputK)):
		code = inputK[i].split()
		code = map(int, code)

		# Insert all the codes of generator matrix in codes array.
		generator_codes.append(code)


	# Generate all the codewords of the input code.

	totalCodes = pow(2, inputK)
	for i in range(0, totalCodes):
		code = inputN*[0]
		shift = 0
		while( shift != inK):
			if( (i >> shift) & 1):
				for j in range(0, inputN):
					code[j] += generator_codes[shift][j]%2
				shift += 1
		codes.append(code)