import time
import math

'''
This program contains 4 hashing schemes to insert elements into a hash table and methods to handle collisions. It starts off with a Probing_Base class with all the hashing statistics
we want to measure, and then a Linear Probing, Quadratic Probing, Chaining, and our custom hashing scheme. The program takes in a file input and inserts the integers in a file into a hash table
based on the scheme chosen. The user has the option to choose their hashing scheme of choice and a input file. The program also generates statistics such as runtime, number of collisions,
and more to give additional information on the hashing function efficiency. 
'''



#User Input to use named files. User can input any file they chooes
input_file= input("Enter name of input file: ")
output_file= input("Enter name of output file: ")


#Define a Base class which will contain all required parameters to measure hash function efficiency
class Probing_Base:
    def __init__(self, mod, bucket_size, hash_scheme):
        self.mod= mod
        self.table_size= 120
        self.bucket_size= bucket_size
        self.total_collisions =0
        self.comparisons= 0
        self.primary_collisions=0
        self.secondary_collisions=0
        self.inserted= 0
        self.items_not_inserted= 0
        self.load_factor= 0
        self.total_process= 0
        self.buckets= []
        self.empty_slots= mod
        self.start_time= time.time()
        self.hash_scheme= hash_scheme
        print(f"Start_Time : {self.start_time}ms")
        for i in range(self.table_size):
            self.buckets.append(None)



    #Define output function to hold hash table and all the hash function statistics
    def output(self,file_name):
        end_time = time.time()
          


        #Output to file
        with open(output_file, "w") as f:
            runtime = end_time - self.start_time
            f.write(f"Start_Time : {self.start_time}\n")
            f.write(f"End_Time : {end_time}\n")
            f.write(f"Runtime : {runtime*1000}ms\n")
            f.write(f"Input Count: {input_count}\n")
            f.write(f"Hash table size: {self.table_size}\n")
            f.write(f"Bucket Size: {self.bucket_size}\n")
            f.write(f"Total Collisions: {self.total_collisions}\n")
            f.write(f"Number of Primary Collisions: {self.primary_collisions}\n")
            f.write(f"Number of Secondary Collisions: {self.secondary_collisions}\n")
            f.write(f"Number of Comparisons: {self.total_process+self.total_collisions}\n")
            f.write(f"Number of Items Inserted: {self.inserted}\n")
            f.write(f"Number of Items Not Inserted: {self.items_not_inserted}\n")
            f.write(f"Load Factor: {self.inserted/self.mod}\n")
            



            #Write out hash table slots (each slot will be a open bracket)
            columns= 5 if self.bucket_size== 1 else 3
            for i in range(self.table_size):
                #Print empty brackets only if the buckets is none otherwise print whats in the bucket(number) and end must be empty space so it doenst go to next line
                f.write(str("[     ] " if self.buckets[i] is None else f"[{self.buckets[i]}]"))
                if ((i+1) %columns)==0:
                    f.write(str("\n"))


    #Function for our custom hashing method (Multiplication) based        
    def custom_hashing(self, integer):
         A= 0.6180339887
         k= integer
         h= math.floor(self.mod* (k*A-math.floor(k*A)))
         return h


    #Default modulo hashing function
    def modulo_hashing(self, integer):
        return integer % self.mod
        
        
#Linear Probing Class (Use inheritance to call Probing_Base class)

'''
Linear Probing is one collision handling method where if two hash values map to the same slot, we need to find a way to make sure there is only one slot per hash value. Therefore
we look to the next adjacent slot to see if its empty and do this until we find an empty slot
'''


class Linear_Probing(Probing_Base):           
        

    #Process function where we input integer integers into slots, and if they are filled, move to next slot
    def process(self, integer):

        self.total_process+=1 #Counter for how many inputs there are   
        
        #Check if we have enough slots
        if self.empty_slots > 0:
            if self.hash_scheme== "modulo":
                
                h= self.modulo_hashing(integer) #Default hashing scheme

            else:
                h= self.custom_hashing(integer) #Custom hashing scheme if user inputs "custom" instead of "modulo"
                

            #Checks to see if slot is empty, if empty we input integer into the slot
            if self.buckets[h] is None:
                self.buckets[h] = integer
                self.inserted +=1
                self.empty_slots -=1

                
            #If not empty, go to next slot and perform modulo operation until we find a empty slot
            else:
                h_next= (h+1) % self.mod            # %self mod allows us to wrap around to first hash value. For example, 
                self.total_collisions +=1
                self.primary_collisions+=1
                
              
                #If this next slot is not empty again, perform another modulo operation to handle this
                while self.buckets[h_next] is not None:       
                    h_next= (h_next+1) % self.mod
                    self.total_collisions +=1
                    self.secondary_collisions+=1
                    
                self.buckets[h_next]= integer
                self.inserted +=1
                self.empty_slots -=1
         
        else:
            self.items_not_inserted+=1



#Quadratic Probing Class

'''
Quadratic probing is another way to handle collisions, this time instead of using just modulo we use the equation h(k,i)= h(k+ +c1i + c2i^2 (modm)). This requires two constants C1 and C2, which we defined
as C1= 0.5 and C2= 0.5 but they can be changed
'''

class Quadratic_Probing(Probing_Base):
     

    #Process function where we input integer integers into slots, and if they are filled, move to next slot
    def process(self, integer):
        self.total_process+=1

        #Define c1 and c2 constants
        c1, c2= 0.5, 0.5
        if self.hash_scheme== "modulo":
            h= self.modulo_hashing(integer)
        else:
            h= self.custom_hashing(integer)


        #Checks to see if slot is empty, if empty we input integer into the slot
        if self.empty_slots > 0: 
            if self.buckets[h] is None:
                self.buckets[h] = integer
                self.inserted+=1
                self.comparisons+=1
                self.empty_slots-=1



            #Introduce Quadratic Hash Function h(k,i)= h(k+ +c1i + c2i^2 (modm))
            else:
                i= 1
                hash_value= (h + c1 * i + c2 * (i * i))
                
                h_next= hash_value %self.mod
                self.total_collisions += 1
                self.primary_collisions+=1


            #Perform Quadratic Probing again until we find a available slot. i is incremented by 1 each time.
                while self.buckets[int(h_next)] is not None: 
                    i= i +1
                    h_next= (h + (c1 * i) + (c2 * (i*i))) %self.mod  #This wraps around
                    self.total_collisions += 1
                    self.comparisons +=1
                    self.secondary_collisions+=1
                    
                self.buckets[int(h_next)]= integer
                self.inserted+=1
                self.empty_slots-=1

        else:
            self.items_not_inserted+=1
            
    
#Chaining Probing Class

'''
Chaining is another way to handle collisions. This time instead of trying to solve the issue when multiple integers map to the same slot, we can just accept this and store them into a linked list. Essentially,
we will allow multiple values to hash to the same slot. These values will be stored into a linked list
'''

class Chaining_Probing(Probing_Base):           
        

    #Process function where we input integer integers into slots, and if they are filled, move to next slot
    def process(self, integer):

        self.total_process+=1  
        if self.hash_scheme== "modulo":
                h= self.modulo_hashing(integer)
                
        else:
            h= self.custom_hashing(integer)


        #Checks to see if slot is empty, if empty we input integer into the slot
        if self.buckets[h] is None:
            #This time we set the slot as a list instead of integer. This way the slot can take a list and we can have multiple integers in the list
            self.buckets[h] = list()
            self.buckets[h].append(integer)
            self.inserted +=1
            self.empty_slots-=1
            

        #If there is a collision, then we can add another integer to the list
        else:
            self.primary_collisions+=1
            self.total_collisions+=1    
            self.buckets[h].append(integer)
            self.inserted +=1
         
        #else:
            #self.items_not_inserted+=1



'''
Here are the 4 hashing schemes with 3 parameters, the modulo, bucket size, and hash_scheme. The mod parameter can be changed to any integer,
bucket_size takes 1 or 3, and hash_scheme takes either "modulo" or "custom" hashing scheme.
'''

#hash = Linear_Probing(mod= 120, bucket_size=1, hash_scheme="modulo")
#hash= Quadratic_Probing(mod=120, bucket_size=1, hash_scheme="modulo")
hash= Chaining_Probing(mod=120, bucket_size=1,hash_scheme= "modulo")




#Function to open file and parse integers
with open(input_file, "r") as f:
    input_count=0
    lines=f.readlines()
    for line in lines[4:]:
        line= line.strip()
        #Check if it is numeric (if its a space or a string it will bypass and carry on)
        if line and line.isnumeric():
            line= int(line)
            input_count+=1
            hash.process(line)
            
hash.output(output_file)


