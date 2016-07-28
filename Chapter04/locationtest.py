from Bio import SeqIO
my_snp = 380
record = SeqIO.read("ls_orchid_part.gbk","genbank")
for feature in record.features:
#    print(feature)
    if my_snp in feature:
        print("%s %s" % (feature.type, feature.qualifiers.get('db_xref')))
