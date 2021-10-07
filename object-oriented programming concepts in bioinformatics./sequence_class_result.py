from s13724_Q2 import *

sequence=Sequence.fasta_Split("OSDREB_sequences.FASTA")
seq_objects = []

for key,value in sequence.items():
    if Sequence.get_Seq_Type(value[1])=="DNA":
        seq_objects.append(DNAseq(key,value[0][1],value[0][2],value[0][3],value[1]))
    elif Sequence.get_Seq_Type(value[1]) == "mRNA":
        seq_objects.append(mRNAseq(key,value[0][1], value[0][2], value[0][3], value[1]))
    else:
        seq_objects.append(Proteinseq(key,value[0][1],value[0][2],value[0][3],value[1],value[0][1],True))

for objects in seq_objects:
    print(objects.sequence_type)

    if objects.sequence_type == "DNA" and "DREB1A" in objects.seq_name:
        print('i')
        print("Gene ID: ",objects.seq_id)
        print("Sequence length: ", objects.sequence_length)
        print("Sequence type: ", objects.sequence_type)
        print("AT content: ", objects.AT_content)
        print()

    if objects.sequence_type == "DNA" and "DREB1B" in objects.seq_name:

        print('ii')
        new_seq = DNAseq.transcribe_Sequence(DNAseq, objects.sequence)
        mRNA = mRNAseq(objects.seq_name,objects.seq_id,objects.species_name,objects.subspecies_name, new_seq)
        print("Sequence length: ", mRNA.seq_len)
        print("Sequence type: ", mRNA.sequence_type)
        print("AT content: ", mRNA.AT_content)
        print("Sequence: ",mRNA.sequence)
        print()

        print('iii')
        prot = mRNA.Translated_sequence
        print("protein: ", prot)
        print("length: ",len(prot))
        print()

    if objects.sequence_type == "protein" and "DREB2A_P" in objects.seq_name:

        print('iv')
        print("Uniprot ID: ",objects.uniprot_id)
        print("reviewed: ","yes" if objects.reveiwed else "no")
        print("Composition: ", objects.get_Character_Count(objects.sequence))
        print("hydrophobicity: ",objects.Hydrophobicity)
        print()

print(Sequence.sequence_count)
