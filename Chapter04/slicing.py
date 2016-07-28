from Bio import SeqIO
record = SeqIO.read("ls_orchid_part.gbk","genbank")
print(len(record))
print(len(record.features))
print(record.features[1])
