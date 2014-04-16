''' ****************************************
Author: Tarang Patel

ID: 201101110

Email: patel_tarang@daiict.ac.in

Brief: This python script will take an file as input.
	   The input file will contain the Genarator matrix 
	   of binary linear code [n, k, d].
	   Note that, the input generator matrix should start
	   from the first line of the file.
	   Also the format of the generator matrix should be as
	   follows: 
	   
	   For e.g,

	   '0 0 0 0
        1 1 1 1'

	   The script will compute the Dual code of the given binary
	   linear code and will store the list of the codewords in 
	   a output file. It will also store the parameters of the code
	   [n, k, d] in the file.
	   The script will also output the list of the codewords and the 
	   parameters of the code in the standard output.
'''

from math import *
import math

# Global variables
codes = []                  # Contains all the codewords of the given binary linear code
dualCodes = []              # Contains all the codewords of the computed Dual code.
inputK = 0					# 'k' value of input code.
dualK = 0					# 'k' value of Dual code.
inputN = 0					# Length of the codewords of input code.
dualN = 0					# Length of the codewords of Dual code.
dualD = 10000000		    # Minimum hamming distance of the Dual code. Initialized to a high 
							# value.
 
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
				break

		if isOrthogonal:
			generatedCode = []
			shift = inputN - 1
			while shift != -1:
				generatedCode.append((code >> shift) & 1)
				shift -= 1
			dualCodes.append(generatedCode)

def computeMinumumHammingDistance():
	global dualD
	for selectedCode in dualCodes:
		for otherCode in dualCodes:
			hammingDistance = 0
			if selectedCode != otherCode:
				for i in range(0, inputN):
					if selectedCode[i] != otherCode[i]:
						hammingDistance += 1
				dualD = min(dualD, hammingDistance)

def writeOutputToFile():
	output_file = open('output.txt', 'w')
	output_file.write("Dual code of the given binary linear code has parameters [n, k, d] = ["+str(inputN) +", "+str(inputN - inputK)+", "+str(dualD)+"]\n\n")
	output_file.write("All the codewords of the Dual code are as follows:\n\n")
	for dualCode in dualCodes:
		output_file.write("(")
		for i in range(0, inputN - 1):
			output_file.write(str(dualCode[i])+", ")
		output_file.write(str(dualCode[inputN - 1])+")\n")

def output():
	print "Dual code of the given binary linear code has parameters [n, k, d] = ["+str(inputN) +", "+str(inputN - inputK)+", "+str(dualD)+"]\n"
	print "All the codewords of the Dual code are as follows:\n"
	for dualCode in dualCodes:
		print "(",
		for i in range(0, inputN - 1):
			print str(dualCode[i])+",",

		print str(dualCode[inputN - 1])+" )"


