from Bio.Seq import Seq
from Bio.Alphabet import IUPAC, generic_dna, generic_protein
seq1 = Seq("ACGT", IUPAC.unambiguous_dna)
seq2 = Seq("ACGT", IUPAC.ambiguous_dna)
print(str(seq1)==str(seq2))
print(seq1==seq2)
print(seq1=="ACGT")

dna_seq = ("ACGT", generic_dna)
prot_seq = ("ACGT", generic_protein)
print(dna_seq==prot_seq)
