ReadMe

Below is a brief introduction and instructions on how to run the LCS.py script in Python 3.8 64-Bit. The LCS.py script
is a concise, easy to use script containing the algorithm to solve the Longest Common Subsequence Problem using dynamic programming.


The script requires a file input containing a list of input DNA strings that will be analyzed. Below is a example of Input1.txt which contains 4 strings. 


S1 = ACCGGTCGACTGCGCGGAAGCCGGCCGAA
S2 = GTCGTTCGGAATGCCGTTGCTCTGTAAA
S3 = ATTGCATTGCATGGGCGCGATGCATTTGGTTAATTCCTCG
S4 = CTTGCTTAAATGTGCA


The Input1(Errors).txt file is the same file but with some randomly introduced numbers and characters that are not supposed to be in the file. 


S1 = ACCGGTCGACTGCGCGGSR2gAAGCCGGCCGAA
S2 = GTCGTTCGGAATGCCGT3sTGCTCTGTAAA
S3 = ATTGCATTGCATGGGCGCGATGCFS$ATTTGGTTAATTCCTCG
S4 = CTTGCTTA3jhmrAATGTGCA



Executing the script is simple and user-friendly. The folder contains input files that can be ran by the script.

1.  Execute the code in Python and the prompt will ask the user to input the name of an input file. Input the desired file to be processed and click enter. Then the prompt will ask the user
to output the name of an output file. Again, input the name of the output file and press enter. 

(You will see this in the prompt)

Enter name of input file: Input1.txt    	 	(Here I typed in the input file and click enter)


Enter name of output file: Output1.txt 			(Type output file name of my choice and click enter)



2. The script generates an output file Output1.txt which you will find in the directory you ran your script in. This file will contain,
each of the input sequences, the length of the LCS, the actual LCS sequence, and the time taken to get the sequence. At the bottom of the page,
you will be able to find the total number of pairwise combinations completed and the total execution time. 