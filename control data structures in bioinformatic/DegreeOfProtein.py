'''
Author: Navindu
input: codon_table.txt
output: amino acid sequence
'''

import networkx as nx
count = 0
connections={}
# open the codon table and store it in a variable
with open('string_interactions.tsv', 'r') as dataTable:
    for line in dataTable:
        count += 1
        #create the dictionary
        if '#' not in line and line != '\n':
            con = line.strip().split('\t')
            connections[count] = con[0:2]
print(connections)

#create empty graph
g = nx.Graph()

for key, value in connections.items():
    g.add_edge(value[0],value[1])

degreeOfP=str(g.degree['ERF24'])

print('Degree of DREB1A is: ' + degreeOfP)
