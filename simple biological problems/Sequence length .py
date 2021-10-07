'''
author: Navindu Sandumina
input: DNA sequence in FASTA fomat
output: Sequence length by len function
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

#count length of the sequence
length=len(sequence)

#return lenght
print("the length of the sequnce is",length)
