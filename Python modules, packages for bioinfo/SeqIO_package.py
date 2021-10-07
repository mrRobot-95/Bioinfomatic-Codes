'''
Author: Navindu
input: ATdreb2a.fasta
output:dreb2a_blast.xml
'''

from Bio import SeqIO
import re

for sequence in SeqIO.parse('ATdreb2a.fasta','fasta') :
    print(sequence.id)
    print(sequence.description)
    print(sequence.seq)
    print(len(sequence))


from Bio.Blast import NCBIWWW
fasta_string = open("ATdreb2a.fasta").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

with open("dreb2a_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()


from Bio.Blast import NCBIXML
result_handle = open("dreb2a_blast.xml",'r')
blast_record = NCBIXML.read(result_handle)


E_VALUE = 0.05
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE:
            print("sequence:", alignment.title)
            print("length:",alignment.length)
            print("e value:", hsp.expect)
            print(hsp.query[0:75] + "...")
            print(hsp.sbjct[0:75] + "...")


string1= "ACGTG"
string2="TC"
count=1
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        count+=1


        rx1=re.compile(string1)
        result1 = rx1.search(hsp.sbjct)
        if result1:
            print(result1.group())
            print(result1.span())
            print("blast hit number is:"+str(count))
        rx2 = re.compile(string2)
        result2 = rx2.search(hsp.sbjct)
        if result2:
            print(result2.group())
            print(result2.span())
            print("blast hit number is:" + str(count))



result_handle.close()

