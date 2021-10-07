'''
Author- Navindu Sandumina
INPUT-OSDREB_sequences.FASTA/codon_table.txt
OUTPUT-Sequence class / DNAseq class / mRNAseq class/ Proteinseq class
'''
class Sequence:
    seq_name=''
    seq_id=''
    sequence_type = ''
    sequence_length = 0
    sequence_count = 0
    species_name = ''
    subspecies_name = ''
    sequence=''

    def __init__(self, seq_name, seq_id, species_name, subspecies_name, sequence):
        self.seq_id=seq_id
        Sequence.sequence_count+=1
        self.seq_name=seq_name
        self.sequence_type=Sequence.get_Seq_Type(sequence)
        self.sequence_length=len(sequence)
        self.species_name=species_name
        self.subspecies_name=subspecies_name
        self.sequence = sequence

    #method for split multiple fasta file in to dictionary containing the Gene name
    @staticmethod
    def fasta_Split(file_name):
        sequences = {}
        with open(file_name, 'r') as sequence:
            gene_name = ''
            seq=''
            for line in sequence:
                if line != '\n':
                    line = line.strip()
                    if '>' in line :
                        gene_name= line.strip().split('-')[0]
                        list = line.strip().split('-')[0:]
                        seq=''
                    if '>' not in line:
                        seq=seq+line
                        sequences[gene_name]=list,seq
        print(sequences)
        return (sequences)

    #method for identydy sequence type
    def get_Seq_Type(sequence):
            if 'A' in sequence and 'T' in sequence and 'C' in sequence and 'G' in sequence and 'M' not in sequence:
                #print("This is DNA sequence")
                return "DNA"

            if 'A' in sequence and 'U' in sequence and 'C' in sequence and 'G' in sequence and 'M' not in sequence:
                #print("This is mRNA sequence")
                return "mRNA"

            if 'M' in sequence:
                #print("This is protein sequence")
                return "protein"

    #methode for count characters in sequnece
    def get_Character_Count(self,sequence):

        character_counts={}
        baseA = 0
        baseT = 0
        baseC = 0
        baseG = 0
        aa = 0

        if 'A' in sequence and 'T' in sequence and 'C' in sequence and 'G' in sequence and 'M' not in sequence:
            name='DNA'
            for j in sequence:
                if j == 'A':
                    baseA+=1
                if j == 'T':
                    baseT+=1
                if j == 'C':
                    baseC += 1
                if j == 'G':
                    baseG+=1
        else:
            name='protein'
            for j in sequence:
                    aa+=1
        character_counts[name]=["adeninne count is:"+str(baseA),"Thymine count is:"+str(baseT),"Cytocine count is:"+str(baseC),"Guanine count is:"+str(baseG),"Amino acid count is:"+str(aa)]
        #print(character_counts)
        return character_counts


#sub class for DNA
class DNAseq(Sequence):
    AT_content=0
    Transcribed_sequence=''


    def __init__(self, seq_name, seq_id,species_name, subspecies_name,sequence):
        super().__init__(seq_name, seq_id, species_name, subspecies_name, sequence)

        self.AT_content = self.AT_Contents(sequence)
        self.Transcribed_sequence=self.transcribe_Sequence(sequence)


    #method for transcribe DNA sequence
    def transcribe_Sequence(self,sequence):
        transcribed_sequence=sequence.replace('T','U')
        #print(Transcribed_seq)
        return transcribed_sequence

    # method for get A T bases content in sequence
    def AT_Contents(self,sequence):
        AT=0
        for i in sequence:
            if i== 'A' or i=='T':
                AT+=1
        AT_con=str(AT/len(sequence))
        #print(AT_con)
        return AT_con
#sub class for store mRNA sequences
class mRNAseq(Sequence):
    AT_content=0
    Amino_acid_codons=''
    Translated_sequence=''


    def __init__(self, seq_name, seq_id,species_name, subspecies_name,sequence):
        super().__init__(seq_name, seq_id, species_name, subspecies_name, sequence)

        self.mRNA_id = seq_id
        self.mRNA_name = seq_name
        self.seq_type = "mRNA"
        self.seq_len = len(sequence)
        self.AT_content = self.get_ATcontent(sequence)
        self.Translated_sequence = self.translate_Sequence(sequence)

    # methode for get AT content in mRNA sequnce
    def get_ATcontent(self,sequence):
        AT = 0
        for i in sequence:
            if i == 'A' or i == 'U':
                AT += 1
        AT_con = AT / len(sequence)
        #print(AT_con)
        return AT_con

    # method for get codons dictionary from text file
    def upload_Codons(mRNAseq,CodonfileName):
        Codon_map = {}
        # open codon_table and store in to variable
        with open('codon_table.txt', 'r') as C_table:
            for line in C_table:

                # remove header and empty lines
                if '#' not in line and line != '\n':
                    (codon, amino_acid, Letter, FullName) = line.strip().split('\t')
                    # make dictionary from codons as key and amino acids as value
                    Codon_map[codon] = Letter

        # print(Codon_map)
        return Codon_map

    # method for translate mRNA sequnce and get aminoacid sequnce
    def translate_Sequence(self,sequence,CodonfileName="OSDREB_sequences.fasta"):
        stop_codons = 'UGA' or 'UAA' or 'UAG'
        start_codon = 'AUG'
        codonDict = self.upload_Codons(CodonfileName)

        # read mRNA sequence
        i = 0
        flag = 0
        protein = ''
        while sequence:
            # select 3 bases in seq
            codon = sequence[i:i + 3]
            aa = codonDict[codon]

            # break the translation when stop codon found
            if codon == stop_codons:
                break

            # find start codon
            if codon == start_codon:
                flag = 1

            # if start codon find translate codons to amino acid
            if flag == 1:
                protein = protein + aa
            i = i + 3
        #print(protein)
        return protein

#subclass for protein sequences
class Proteinseq(Sequence):
    Uniprot_ID=''
    Reviewed_status=''
    Hydrophobicity=0.0

    def __init__(self, seq_name, seq_id, species_name, subspecies_name, sequence,uniprot_id, reviewed):
        super().__init__(seq_name, seq_id, species_name, subspecies_name, sequence)
        self.prot_name=seq_name
        self.prot_id=seq_id
        self.uniprot_id=uniprot_id
        self.reveiwed=reviewed
        self.Hydrophobicity=self.get_Hydrophobicity(sequence)

    # method for count hydropohobicity of protein sequence
    def get_Hydrophobicity(self,sequence):
        hydrovalue=0
        length=len(sequence)
        for i in sequence:
            if i=='A' or i=='I' or i=='L' or i == 'M'or i == 'F' or i == 'W' or i == 'Y' or i == 'V':
                hydrovalue+=1
        hydrophobicity=(hydrovalue/length)*100
        #print(hydrophobicity)
        return hydrophobicity

