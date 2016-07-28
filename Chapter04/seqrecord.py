from Bio.Seq import Seq
simple_seq = Seq("GATC")
from Bio.SeqRecord import SeqRecord
simple_seq_r = SeqRecord(simple_seq)

print(simple_seq_r.id)
simple_seq_r.id="AC12345"
simple_seq_r.description = "Made up sequence I wish I could write a paper about"
print(simple_seq_r.description)
print(simple_seq_r.seq)

simple_seq_r2 = SeqRecord(simple_seq, id="AC12345")

simple_seq_r.annotations["evidence"]="None,I just made it up"
print(simple_seq_r.annotations)
print(simple_seq_r.annotations["evidence"])

simple_seq_r.letter_annotations["phred_quality"] = [40,40,38,30]
print(simple_seq_r.letter_annotations)
print(simple_seq_r.letter_annotations["phred_quality"])


