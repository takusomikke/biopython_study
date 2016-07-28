from Bio import SeqIO
record = SeqIO.read("ls_orchid_part.fasta","fasta")
print(record)
print("record.seq = " + record.seq)
print("record.id = " + record.id)
print("record.name = " + record.name)
print("record.description = " + record.description)

