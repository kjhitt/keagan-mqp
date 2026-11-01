# purpose of file:
#    creates JSON files with entire proteome, just sorts by top differences (only reports top 100)
#    coding-wise, incredibly inefficient to do it this way but did it by combining proteome_comparison.py w/ combine_json_data.py


import pandas as pd
import math
import json

ID_CUTOFF = 0

df172 = pd.read_excel("BIGb0172_comparison.xls")
output172 = "BIGb0172_comparison_algo.json"
df393 = pd.read_excel("BIGb0393_comparison.xls")
output393 = "BIGb0393_comparison_algo.json"
#main difference:
# 0393 has 1 as the other symptom-alleviating bacteria,
# 0172 has 4


df_filtered172 = df172[['ref_genome_patric_id', 'comp_genome_4_patric_id', 'comp_genome_1_percent_identity', 'comp_genome_2_percent_identity', 'comp_genome_3_percent_identity', 'comp_genome_4_percent_identity', 'comp_genome_5_percent_identity']]
df_filtered393 = df393[['ref_genome_patric_id', 'comp_genome_1_patric_id', 'comp_genome_1_percent_identity', 'comp_genome_2_percent_identity', 'comp_genome_3_percent_identity', 'comp_genome_4_percent_identity', 'comp_genome_5_percent_identity']]

data = []

# makes sure the other bacteria has a homolog
for i in range(1, len(df_filtered172)):
    if (math.isnan(df_filtered172.iloc[i]['comp_genome_4_percent_identity'])):
        continue
    data.append(df_filtered172.iloc[i].to_dict())

with open(output172, "w") as f:
    json.dump(data, f)

#does the same thing but for hte other file
data = []

for i in range(1, len(df_filtered393)):
    if (math.isnan(df_filtered393.iloc[i]['comp_genome_1_percent_identity'])):
        continue
    data.append(df_filtered393.iloc[i].to_dict())

with open(output393, "w") as f:
    json.dump(data, f)

with open(output172, "r") as f172:
    data172 = json.load(f172)

with open(output393, "r") as f393:
    data393 = json.load(f393)

in_both = []

#very inefficient to do this as O(n*m), but they're fairly small
#so not doing a more efficient algorithm (could sort them first, transform into hashs first, etc.)
for i in range(len(data172)):
    for j in range(len(data393)):
        #finds any matches
        if data172[i]['ref_genome_patric_id'] == data393[j]['comp_genome_1_patric_id']:
            in_both.append(data172[i])

#resets NaN to 0%
for protein in in_both:
    for key in protein:
        if pd.isna(protein[key]): #pd.isna works because otherwise it's treated as a string
            protein[key] = 0

    protein['max_others'] = max(protein['comp_genome_1_percent_identity'], protein['comp_genome_2_percent_identity'], protein['comp_genome_3_percent_identity'], protein['comp_genome_5_percent_identity'])
    protein['dif'] = protein['comp_genome_4_percent_identity'] - protein['max_others']
    

#sorts by symptom-alleviating bacteria - MAX(other bacteria)
sorted_both = sorted(in_both, key=lambda x: (x['dif']))

print(f"{len(sorted_both)} Protein & Sequence IDs (in BIGb0172):")
for seq in sorted_both:
    print(seq['ref_genome_patric_id'], seq['comp_genome_4_percent_identity'], seq['dif'], seq['max_others'])