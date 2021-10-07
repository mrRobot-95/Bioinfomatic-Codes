'''
Author- Navindu Sandumina
INPUT-OSDREB_sequences.FASTA
OUTPUT- DNA dictionary / type of sequence /AT content
'''


def SplitSequnce():
    fastaFileName = input("Fasta file name")
    sequences = {}
    with open(fastaFileName, 'r') as sequence:
        header = None
        data = ''
        for line in sequence:
            if line.startswith('>'):
                if header and data:
                    sequences[header] = data
                data = ''
                header = line.strip()
            else:
                data += line.strip()

        if header and data:
            sequences[header] = data
    print(sequences)
    return (sequences)


def Type():
    sequences = SplitSequnce()
    for i in sequences:
        sequence = sequences[i]
        if 'A' in sequence and 'T' in sequence and 'C' in sequence and 'M' not in sequence:
            print(i + "is DNA sequence")
        if 'A' in sequence and 'U' in sequence and 'C' in sequence and 'M' not in sequence:
            print(i + " is mRNA sequence")
        if 'M' in sequence:
            print(i + " is protein sequence")


def baseATcontent():
    sequences = SplitSequnce()
    for i in sequences:
        A = 0
        T = 0
        seq = sequences[i]
        if 'A' in seq and 'T' in seq and 'C' in seq and 'M' not in seq:

            for base in seq:
                if base == 'A':
                    A += 1
                elif base == 'T':
                    T += 1
        print(i + ' ' + "sequence" + ' ' + "A base count is:", A)
        print(i + ' ' + "sequence" + ' ' + "T base count is:", T)


SplitSequnce()
Type()
baseATcontent()
