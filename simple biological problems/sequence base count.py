'''
author: Navindu Sandumina
input: DNA sequence in FASTA fomat
output: count bases in sequence
'''

#Open/Read sequence and store in variable

with open ('sequence.fasta','r' ) as sequnceFile:
    sequence = ''
    for line in sequnceFile:
        if line != '\n':
            #line=line.strip()
            #Remove the fasta header
            if ('>') not in line and ('A') not in line:
                sequence=sequence+line
    print(sequence)
sequnceFile.close()

# Define counterA,G,C,T
counterA=0
counterC=0
counterG=0
counterT=0

# For each letter in sequence
for letter in sequence:
    #if letter is A increase the counterA by 1
    if (letter == 'A') :
        counterA+=1
    #elseif letter is C increase the counterC by 1
    elif (letter =='C'):
        counterC+=1
    #elseif letter is G increase the counterG by 1
    elif (letter =='G'):
        counterG+=1
    #else increase the CounterT by 1
    else:
        counterT += 1
# Return counters value
print("adenine base count in sequence is",counterA)
print("cytosine base count in sequence is",counterA)
print("guanine base count in sequence is",counterG)
print("thymine base  count in sequence is",counterT)
