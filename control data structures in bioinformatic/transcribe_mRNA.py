'''
input=OSDREB1A.fasta file
output=OSDREB1A_mRNA.fasta
Author=Navindu Sandumina
'''
# open/read sequence and store in variable
#fasta1 is main sequnce file with 2 sequnces
seq=''
Header=''
with open('OSDREB1A.fasta','r') as fasta1:
    for line in fasta1:
        #select mRNA sequnce
        if ('A') in line and ('T') in line and ('C') in line and ('G') in line and ('M') not in line:
            seq = seq + line
        #select Header
        if ('>') in line and ('.') in line :
            Header=Header+line
            Header=Header.strip()


#change T to U
sequence=(seq.replace('T','U'))


Header1="_transcribed"
#add transcribed to header end
Header2=("".join([Header,Header1]))
print(Header2+'\n'+sequence)

#write new fasta file
with open("OSDREB1A_mRNA.fasta",'w') as output:
    output=output.write(Header2+'\n'+sequence)
