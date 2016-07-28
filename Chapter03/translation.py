from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
print("messenger_rna = " + messenger_rna)
amino_array01 = messenger_rna.translate()
print("amino_array01 = " + amino_array01)

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
print("coding_dna = " + coding_dna)
amino_array02 = coding_dna.translate()
print("amino_array02 = " + amino_array02)
