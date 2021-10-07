'''
author: Navindu Sandumina
input: DNA sequence in FASTA fomat
output: Sequence length
'''

#Open/Read sequence and store in variable

with open ('sequence.fasta','r' ) as sequnceFile:
    sequence = ''
    for line in sequnceFile:
        if line != '\n':
            line=line.strip()
            #Remove the fasta header
            if ('>') not in line:
                sequence=sequence+line
    print(sequence)
sequnceFile.close()

#Define counter
counter=0


for letter in sequence:        #count letters
    #increase the counter by 1
    counter+=1

#Return counter value
print("the length of the sequnce is",counter)
