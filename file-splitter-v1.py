#import os
import re
import math
import pprint
#import itertools

# Path to notices
# TO DO: Condense path to VI File
input_text = "./SampleText/Input_Text_Sample.txt"

# initialize empty list to contain list of parsed lists of text
parsed = []

# initialize empty list to temporarily contain the parsed record
lastblock = []  

# define the pattern "beginning of new block"
newblockregex = re.compile('^"GROUP.*') 

#

"""
Pythonic comprehension for opening a text file.
Would use 'while text is open is True' in R.

From python documentation on 'with' keyword:
It is good practice to use the with keyword when dealing with file objects. 
The advantage is that the file is properly closed after its suite finishes, 
even if an exception is raised at some point. 
Using 'with' is also much shorter than writing equivalent try-finally blocks.
"""
def create_parsed(input_text, parsed, lastblock, newblockregex):
    with open(input_text) as vifile:
        # use readlines in for loop to loop over each line in the txt
        for line in vifile.readlines():
            
            # if regex is matched at the beginning of the line,
            # removing the spaces at the end of the line
            if newblockregex.match(line.rstrip('\n')):
                
                # and if the last block is initialized (is true)
                if lastblock:
                    # take parsed list and add the block of lines (record)
                    parsed.append(lastblock)
                    
                    # then reset last block to empty
                    lastblock = []
                
                # Add the line being evaluated to the last block list
                lastblock = [line.rstrip('\n')]
            else:
                # Add every other line
                lastblock.append(line.rstrip('\n'))
    parsed.append(lastblock)
    return parsed

create_parsed(input_text, parsed, lastblock, newblockregex)
print(parsed)

####====================####

# Get total number of lines
viTotal = sum([len(rec) for leng, rec in enumerate(parsed)])
print(f"\nTotal rows of record: {viTotal}\n")

"""
Function to calculate number of resulting files given the number of forms.
"""
def maxPrimeFactors (n):   
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1

    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 

"""
Count of blocks (forms/records) in the file.
Gets number of forms in the VI file.
"""
formno = len(parsed)

# Number of resulting files
splitsnum = maxPrimeFactors(formno)
blocks_per_file = round(formno / splitsnum)
#print(f"Blocks per file: {blocks_per_file}")
print(f"There are {formno} records.\n")
print(f"Number of records per output file: {blocks_per_file}\n")

"""
Divide number of forms by desired number of lines to determine number of file splits needed
"""
      
finalLineNum = round(viTotal / splitsnum)

print(f"Total number of lines per file: {finalLineNum}\n")


"""
Splitting records and writing to smaller text files.
"""

def split_records(formnumber=formno, parsed=parsed, blocks_per_file=blocks_per_file, splitsnum=splitsnum):
    
    i=0
    j = 1
    
    while i < formno:
        with open(f'notices_{j}.txt', 'w+') as output_txt:
            parsed_section = parsed[i:blocks_per_file]
            for record in parsed_section:
                for line in record:
                    output_txt.write(line+"\n")
            print(f"File records: {j}")
            print(f"Raw record block: {parsed_section}")
            print("\n")
            print(f"Check small file {j}")
            
            print("\n")
            
            j += 1
            i += splitsnum
            blocks_per_file += blocks_per_file
    output_txt.close()

    #print()

    return(f"Ended on record #{i} \n")

split_records()
