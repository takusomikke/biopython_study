from Bio import SeqFeature
start_pos = SeqFeature.AfterPosition(5)
end_pos = SeqFeature.BetweenPosition(9, left=8, right=9)
my_location = SeqFeature.FeatureLocation(start_pos, end_pos)

print(my_location)
print(my_location.nofuzzy_start)
print(my_location.nofuzzy_end)

exact_location = SeqFeature.FeatureLocation(5,9)
print(exact_location)

