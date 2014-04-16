Brief: 	This python script will take an file as input.
	The input file ('input.txt') will contain the Genarator matrix 
	of binary linear code [n, k, d].
	Note that the input generator matrix should start
	from the first line of the file. Also the format of the generator matrix should be as follows: 
	For e.g, <br>
	'0 0 0 0 <br>
         1 1 1 1' <br>
	The script will compute the Dual code of the given binary
	linear code and will store the list of the codewords in 
	a output file (output.txt). It will also store the parameters of the code
	[n, k, d] in the file.
        The script will also output the list of the codewords and the 
        parameters of the code in the standard output.

Input: 	   'input.txt' file that contains the generator matrix of the given
	    binary linear code in specified format.
	    You can edit the input file and provide valid generator matrix 
	    of the binary linear code.

Ouput:      'output.txt' file that contains the parameters [n, k, d] of the dual
	    code and the list of all the codewords of the dual code.

