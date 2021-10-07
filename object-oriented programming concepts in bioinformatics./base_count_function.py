'''
Author- Navindu Sandumina
INPUT-DNA sequence
OUTPUT- AT content
'''

# read and store sequence in to variable
def baseATcontent(seq):
    #define counters
    A=0
    T=0
    for base in seq:
        if base=='A':
            A+=1
        elif base=='T':
            T+=1
    print("A base count is:",A)
    print("T base count is:",T)

baseATcontent('ATATATATAT')
