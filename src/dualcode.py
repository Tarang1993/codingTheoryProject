codes = []
inK = 0
dualK = 0
inN = 0
dualN = 0
dualD = 0

def generateInputCodes():

	# Open the input file to read the Generator matrix of binary linear code [n, k, d]
	fid = open('input.txt', 'r')
	rows = fid.readlines()
	k = len(rows)
	generator_codes = []

	for i in range(0, len(rows)):
		code = rows[i].split()
		code = map(int, code)

		# Insert all the codes of generator matrix in codes array.
		generator_codes.append(code)


	# Generate all the codewords of the input code.





