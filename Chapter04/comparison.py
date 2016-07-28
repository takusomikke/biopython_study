from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
record1 = SeqRecord(Seq("ACGT"),id="test")
record2 = SeqRecord(Seq("ACGT"),id="test")

try:
    print(record1==record2)
except:
    print("NYA!!")

print(record1.id==record2.id)
