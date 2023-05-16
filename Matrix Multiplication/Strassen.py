import time
from random import randint

'''
Need to split each matrix into 4 parts. For Matrix A and Matrix B we split into 4 ways shown below, and we split it by n/2 
because we are doing operations based on 2^n
'''
    
    # Split matrices in following orders:
    
    #Split by n//2 rows and first n//2 columns, 
    #Split by first n//2 rows and last n//2 columns
    #Split by last n//2 rows and first n//2 columns
    #Split by last n//2 rows and last n//2 columns

    #We will use this general partition method for both Matrices

def partition(M):
    length = len(M)
    
    #Define Empty Submatrices
    A1= []
    A2= []
    A3= []
    A4= []
    
    #For loops to Input Each Matrix Split into its own Respective Variable
    for i in range(length//2):
            A1.append(M[i][:length//2])
    
    for i in range(length//2):
            A2.append(M[i][length//2:])
                
    for i in range(length//2,length ):
        A3.append(M[i][:length//2])
    
    for i in range(length//2, length):
        A4.append(M[i][length//2:])   
    
    #Extract Each of the Elements to be used for the Strassen Multiplications
    return A1, A2, A3, A4

#Add Matrix Function (Use indexes [i][j] in Matrix A and B to represent row and columns)
#Here we use a nested loop where we will iterate through the rows and columns for both Matrix A and B and add them together

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


#Subtract Matrix Function similar to add function except this time we are subtracting the [i][j] elements from A and B
def subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

#Define Strassen Multiplication Function
def strassen(A, B):
    count=0 
    length = len(A)
    K = [[0 for i in range(length)] for i in range(length)]
    
    #Want n to be multiple of 2 but if not, carry out regular multiplication
    if length == 1:
        K[0][0] = A[0][0] * B[0][0]
        return K
    
    #Else statement to carry out Strassen Multiplication
   
    else:
        A1, A2, A3, A4 = partition(A)
        B1, B2, B3, B4 = partition(B)
        
        #Add and subtract each of the splitted elements based on Strassen's Algorithm
        sub1 = subtract(B2, B4)
        sub2 = add(A2, A1)
        sub3 = add(A4, A3)
        sub4 = subtract(B3, B1)
        sub5 = add(A4, A1)
        sub6 = add(B4, B1)
        sub7 = subtract(A2, A4)
        sub8 = add(B4, B3)
        sub9 = subtract(A1, A3)
        sub10 = add(B2, B1)
        
        #Use Strassen Function to multiply submatrices
        strass1 = strassen(A1, sub1)
        count+=1
        strass2 = strassen(sub2, B4)
        count+=1
        strass3 = strassen(sub3, B1)
        count+=1
        strass4 = strassen(A4, sub4)
        count+=1
        strass5 = strassen(sub5, sub6)
        count+=1
        strass6 = strassen(sub7, sub8)
        count+=1
        strass7 = strassen(sub9, sub10)
        count+=1
        
        #Get the final values from the submatrices using the add and subtract methods that were defined above
        final1 = add(subtract(add(strass5, strass4), strass2), strass6)
        final2 = add(strass1, strass2)
        final3 = add(strass3, strass4)
        final4 = subtract(subtract(add(strass5, strass1), strass3), strass7)
        
        #Iterate over the length of n//2 and then append indices
        for i in range(length//2):
            for j in range(length//2):
                K[i][j] = final1[i][j]
                K[i][j+(length//2)] = final2[i][j]
                K[i+(length//2)][j] = final3[i][j]
                K[i+(length//2)][j+(length//2)] = final4[i][j]
    
        return f"Output Matrix: {K}    Number of Strassen Multiplications: {count}"




#Ordinary Multiplication
'''
1. n= D A:rows
2. let C be a new n x n matrix
3. for i = 1 to n
4.   for j = 1 to n
5.       cij=0 
6.       for= 1 to n
7.          cij= cij + aik*bkj
8 return C
'''

def ordinary(A, B):
    
    #Get Counts
    
    counter= 0
    
    #C is a n x n matrix and we will append the products of A[i][k] and B[k][j]
    C =[]
    for i in range(len(A)):
        row= [0]*len(B)
        C.append(row)
    
    #Carry out Three Nested For loops to iterate over A Matrix, B[0], and B Matrix and Append products to C[i][j]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
                counter+=1
   
    return f"Output Matrix: {C}   Number of Ordinary Multiplications: {counter}"



#Get Rid of Zeros generated from Ordinary Function
def no_zero(A):
    a_no_zero= []
    index= 0
    for i in A:
        a_no_zero.append([]) 
        for j in i:
            if j !=0:
                a_no_zero[index].append(j)
        index+=1
    return a_no_zero



#Generate Input that prompts users to enter their desired inputs

order= int(input("Enter Integer Input: "))
Type= input("Enter Multiplication Type: ")
input_file= input("Enter name of input file: ")
output_file= input("Enter name of output file: ")



#Function to open file and perform strassen multiplication
def Strassen(Type):
    with open(input_file, 'r') as file:
        
        #Create Empty Matrix that we will append our data
        matrix = [[], []]
        
        # First Matrix
        for i in range(order):
            matrixinput = file.readline()
            matrix_list = matrixinput.split()
            matrix_list = list(map(int, matrix_list))
            matrix[0].append(matrix_list)
        
        # Second Matrix
        for i in range(order):
            matrixinput = file.readline()
            matrix_list = matrixinput.split()
            matrix_list = list(map(int, matrix_list))
            matrix[1].append(matrix_list)
            
        
    product=strassen(matrix[0], matrix[1])
    return product

#Function to open file and perform ordinary multiplication
def Ordinary(Type):
    with open(input_file, 'r') as file:
        
        #Create Empty Matrix that we will append our data
        matrix = [[], []]
        
        # First Matrix
        for i in range(order):
            matrixinput = file.readline()
            matrix_list = matrixinput.split()
            matrix_list = list(map(int, matrix_list))
            matrix[0].append(matrix_list)
        
        # Second Matrix
        for i in range(order):
            matrixinput = file.readline()
            matrix_list = matrixinput.split()
            matrix_list = list(map(int, matrix_list))
            matrix[1].append(matrix_list)
            
    
    product=ordinary(matrix[0], matrix[1])
    return product



#Print Output to file based on Multiplication Scheme we are using

if Type== "Strassen":
    with open(output_file, "w") as f:
        f.write(f"Matrix Size Check (Order): {order}\n")
        f.write(Strassen(Type))
else:
    with open(output_file, "w") as f:
        f.write(f"Matrix Size Check (Order): {order}\n")
        f.write(Ordinary(Type))
    

    



