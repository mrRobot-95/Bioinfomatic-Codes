'''
Author: Navindu
input: codon_table.txt
output: amino acid sequence
'''
Codon_map = {}
# open codon_table and store in to variable
with open('codon_table.txt', 'r') as C_table:
    for line in C_table:

        # remove header and empty lines
        if '#' not in line and line != '\n':
            (codon, amino_acid, Letter, FullName) = line.strip().split('\t')
            # make dictionary from codons as key and amino acids as value
            Codon_map[codon] = Letter
print(Codon_map)
seq = ""
Header = ""

# read mRNA and store in variablere
with open('OSDREB1A_mRNA.fasta', 'r') as sequence:
    for line1 in sequence:
        if line1 != '\n':
            line1 = line1.strip()
            # remove header
            if '>' not in line1:
                seq = seq + line1
        # get header to write in protien file
        if '>' in line1:
            Header = Header + line1
            Header = Header.strip()

print(seq)


# define start and stop codons
stop_codons = 'UGA' or 'UAA' or 'UAG'
start_codon ='AUG'

# read mRNA sequence
i=0
flag = 0
protein=''
while seq:
    # select 3 bases in seq
    codon = seq[i:i+3]
    aa=Codon_map[codon]

    # break the translation when stop codon found
    if codon == stop_codons:
        break

    # find start codon
    if codon==start_codon:
        flag = 1

    #if start codon find translate codons to amino acid
    if flag == 1:
        protein=protein+aa
    i = i + 3

print(protein)
print(len(protein))

# write translated protein
with open("Translated_mRNA.fasta", 'w') as output:
    output = output.write(Header + "_Trnslated" + '\n' + protein)
