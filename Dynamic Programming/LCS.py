import time
import re

'''
The following algorithm is a dynamic programming apporach to solving the
longest common subsequence problem. The algorithm specifically looks at DNA strings 
consisting of bases A, C, G, and T and compares these strings with each other. It will
output the input sequences, the length of the LCS, the actual LCS sequence, and the time taken to get the sequence
'''

# User Input to use named files. User can input any file they choose
input_file = input("Enter name of input file: ")
output_file = input("Enter name of output file: ")


# Get input from Input File
try:
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Parse Input Line by Line by splitting using the "="
    inputs = []
    for line in lines:
        if '= ' in line:
            inputs.append(line.split('= ')[1].strip())

#Handle exceptions when file does not exist
except FileNotFoundError:
    file_error = "The file "+ input_file + " doesn't exist. Enter a new file. "
    print(file_error)

        
#Function to compare each sequence A and B
def comparison(a, b):

    #Handle any characters that arent A, T, G, or C
    required_bases =re.compile('[CATG]+')
    a=''.join(required_bases.findall(a))
    b=''.join(required_bases.findall(b))

    m = len(a)
    n = len(b)


    # Empty matrix generation where we will store elements
    matrix= []
    for i in range(m + 1):
        matrix.append([0] * (n + 1))
    

    # Dynamic Programming to get count comparisons amd generate matrix
    total_count = 0
    for i in range(m):
        for j in range(n):
            total_count += 1
            if a[i] == b[j]:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

                
    # Store the LCS Sequence in comparison variable
    comparison = []
    i = m
    j= n
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            comparison.insert(0, a[i - 1]) #Insert elements into first part of list
            i = i- 1
            j = j- 1
        elif matrix[i-1][j] >= matrix[i][j-1]:
            i = i- 1
        else:
            j = j- 1
    return matrix[m][n], total_count, comparison



# Generate Output File containing the LCS and Execution Time

Counts = {} #Define Counter Variable
comparison_count =0 #Define variable for # of LCS Combinations
Overall_time=0 #Define variable for overall time

#Nested Loop to Iterate through each comparison and get LCS and individual counts
for i,a in enumerate(inputs):
    for j, b in enumerate(inputs[i+1:], i+1):
        comparison_count += 1
        start_time = time.perf_counter()
        string_a= inputs[i]
        string_b=inputs[j]
        length_lcs, count_mat, lcs_sequence = comparison(string_a, string_b)
        ind_time = (time.perf_counter() - start_time) * 1000
        Counts[(i+1, j+1)] = (length_lcs, count_mat, ind_time)


        #Write to File Inputs, LCS Sequence, and Execution Time
        with open(output_file, 'a') as f:
            f.write(f"1: S{i+1} = {inputs[i]}\n")
            f.write(f"2: S{j+1} = {inputs[j]}\n")
            f.write(f"Length of LCS: {length_lcs}\n")
            f.write(f"LCS sequence: {lcs_sequence}\n")
            f.write(f"Time taken: {ind_time:.3f} ms\n")
            f.write('\n')
        Overall_time += ind_time


#Total Number of LCS Combinations will appear at bottom
with open(output_file, 'a') as f:
    f.write(f"Total pairwise LCS Combinations Completed: {comparison_count}\n")
    f.write(f"Total execution time: {Overall_time} ms\n")
    
