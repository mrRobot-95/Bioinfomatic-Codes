'''
Author: Navindu
input: ATdreb2a.fasta/lab4_2.tsv
output:ordered list of unknown proteins with majority voting score
'''
import networkx as nx
proteins=[]
p_knowns=[]

# Create a graph
g = nx.Graph()

# read stress protein and store it in variable
with open ('string_interactions.tsv' ,'r' ) as file:
    for lines in file:
        if '#' not in lines:
            lines=lines.strip().split('\t')
            proteins.append(lines[0].upper())
            proteins.append(lines[1].upper())
            g.add_edge(lines[0].upper(), lines[1].upper())
print(g.degree)
print(proteins)

# Read the interactions and store it in variable
with open ('AT_stress_proteins.txt' ,'r' ) as file:
    for lines in file:
        p_knowns.append(lines.strip().split('\t')[1].upper())
print(p_knowns)


# Find the unknown proteins
Unknowns=[]
for protein in proteins:
    Unknowns= list(set(proteins) - set(p_knowns))
print(Unknowns)

Mvoting = {}
newKey = ''
# find neighbors of unknown proteins
for unknownP in Unknowns:
    newKey = unknownP
    neighborsList = (list(nx.all_neighbors(g, unknownP)))
    # get only neighbor proteins which are in known protein list
    nset = list(set(neighborsList) & set(p_knowns))
    # count number of known proteins and store in dict
    Mvoting[newKey] = len(nset)

#sort dictionary in discending order
sorted_dict = dict( sorted(Mvoting.items(),key=lambda item: item[1],reverse=True))
print(sorted_dict)
