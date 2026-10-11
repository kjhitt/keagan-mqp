import json

with open("BIGb0172_comparison.json", "r") as f172:
    data172 = json.load(f172)

with open("BIGb0393_comparison.json", "r") as f393:
    data393 = json.load(f393)

in_both = []

#very inefficient to do this as O(n*m), but they're fairly small
#so not doing a more efficient algorithm (could sort them first, transform into hashs first, etc.)
for i in range(len(data172)):
    for j in range(len(data393)):
        #finds any matches
        if data172[i]['ref_genome_patric_id'] == data393[j]['comp_genome_1_patric_id']:
            in_both.append(data172[i])

sorted_both = sorted(in_both, key=lambda x: x['comp_genome_4_percent_identity'])

print("Protein & Sequence IDs (in BIGb0172):")
for seq in sorted_both:
    print(seq['ref_genome_patric_id'], seq['comp_genome_4_percent_identity'])