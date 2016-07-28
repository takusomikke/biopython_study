from Bio.Seq import Seq, MutableSeq
from Bio.Alphabet import IUPAC
my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)

try :
    my_seq[5] = "G"
except TypeError:
    print("NYA!!")

mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)
print(mutable_seq)
mutable_seq[5] = "C"
print(mutable_seq)
mutable_seq.remove("T")
print(mutable_seq)
mutable_seq.reverse()
print(mutable_seq)


