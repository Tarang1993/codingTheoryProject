from math import *
import math

codes = []
dualCodes = [] 
inputK = 0.0
dualK = 0
inputN = 0
dualN = 0
dualD = 0

# Generate all the codewords of the given code [n, k, d] and store in it codes matrix.
def generateInputCodes():

	global inputN, inputK, codes
	# Open the input file to read the Generator matrix of binary linear code [n, k, d]
	fid = open('input.txt', 'r')
	rows = fid.readlines()
	inputK= len(rows)
	generator_codes = []

	for i in range(0, inputK):
		code = rows[i].split()
		code = map(int, code)
		
		# Insert all the codes of generator matrix in codes array.
		generator_codes.append(code)
	
	inputN = len(generator_codes[0])
	
	# Generate all the codewords of the input code.
	totalCodes = int(math.pow(2, inputK))
	for i in range(0, int(totalCodes)):
		code = inputN*[0]
		shift = 0
		#print inputK
		while( shift != inputK):
			if( (i >> shift) & 1):
				for j in range(0, inputN):
					code[j] += generator_codes[shift][j] % 2
			shift += 1
		codes.append(code)

# Compute all the parameters and all the codewords of the dual code of [n, k, d] code.
def computeDualCode():

	global dualCodes
	totalCodeSpace = int(pow(2, inputN))
	for code in range(0, totalCodeSpace):
		isOrthogonal = 1
		for inputCode in codes:
			shift = inputN - 1
			sum = 0
			while shift != -1:
				sum = (sum + inputCode[inputN - shift - 1] * ((code >> shift) & 1)) % 2
				shift -= 1
			if sum != 0:
				isOrthogonal = 0
				print code,inputCode,sum
				break

		if isOrthogonal:
			generatedCode = []
			shift = inputN - 1
			while shift != -1:
				generatedCode.append((code >> shift) & 1)
				shift -= 1
			dualCodes.append(generatedCode)
