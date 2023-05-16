ReadMe

Below is a brief introduction and instructions on how to run the Hashing.py script in Python 3.8 64-Bit. The Hashing.py script
is a concise, easy to use script containing 4 different hashing schemes that will insert elements into a hash table
and handle collisions. The schemes include linear probing, quadratic probing, chaining, and our custom scheme.


The script requires a file input containing a list of integers that will be stored in a hash table like so:



605.421 Foundations of Algorithms 		            Project 1

Minimal required input:

12501
84763
22599
02698
55555
72501




Executing the script is simple and user-friendly. The folder contains input files that can be ran by the script.

1. Scroll to the bottom of the Hashing.py script until you find the hashing schemes

#hash = Linear_Probing(mod= 120, bucket_size=1, hash_scheme="custom")
#hash= Quadratic_Probing(mod=120, bucket_size=1, hash_scheme="modulo")
#hash= Chaining_Probing(mod=120, bucket_size=1,hash_scheme= "modulo")


2. To execute one of the schemes,simply remove the hashtag and then choose the scheme you want to run. 
For example, for linear probing, we choose this scheme as shown below with our parameters. You can choose any integer for the modulo,bucket_size has to be 1 or 3, and hash_scheme can be either "modulo" or "custom". 
Modulo refers to the simple modulo division hashing scheme, where as the custom scheme is hashing multiplication. Here we decided to do "modulo".

hash= Linear_Probing(mod=120, bucket_size=1, hash_scheme="modulo")


Note: For the custom hashing scheme(multiplication hashing) you need to input in the hash_scheme condition "custom".
For example if you want to run scheme 9, custom hashing scheme, bucket size=1, linear probing, this would be your parameters.

hash= Linear_Probing(mod=120, bucket_size=1, hash_scheme="custom")


Additonal Note:
If you want to change the C1 and C2 constants for quadratic probing you have to do it manually. In the Quadratic Probing class, under the "process" function
you can change the C1 and C2 to a integer, currently it is defaulted as 0.5 and 0.5



3. After choosing our scheme, and entering our parameters its time to run the script. Execute the code in Python and the prompt will
ask the user to input the name of an input file. Input the desired file to be processed and click enter. Then the prompt will ask the user
to output the name of an output file. Again, input the name of the output file and press enter. 

(You will see this in the prompt)

Enter name of input file: LabHashingInput(1).txt    	 	(Here I typed in the input file and click enter)
Enter name of output file: LabHashingLinearOutput(1).txt 	(Type output file name of my choice and click enter)



4. The script generates an output file LabHashingLinearOutput(1).txt which you will find in the directory you ran your script in. This file will contain,
the start time, end time, run time, input count(number of integers in input file), size of hash table, bucket size, collision statistics,
comparisons, number of itens not inserted, load factor, and finally the complete hash table with all the elements inserted.
