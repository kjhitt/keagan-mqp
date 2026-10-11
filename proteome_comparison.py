# purpose of file:
#    writes to output json file given filter of proteome comparison

import pandas as pd
import math
import json

ID_CUTOFF = 0.7

df = pd.read_excel("BIGb0172_comparison.xls")
output = "BIGb0172_comparison_70.json"
#df = pd.read_excel("BIGb0393_comparison.xls")
#output = "BIGb0393_comparison_70.json"
#main difference:
# 0393 has 1 as the other symptom-alleviating bacteria,
# 0172 has 4


df_filtered = df[['ref_genome_patric_id', 'comp_genome_4_patric_id', 'comp_genome_1_percent_identity', 'comp_genome_2_percent_identity', 'comp_genome_3_percent_identity', 'comp_genome_4_percent_identity', 'comp_genome_5_percent_identity']]
#df_filtered = df[['ref_genome_patric_id', 'comp_genome_1_patric_id', 'comp_genome_1_percent_identity', 'comp_genome_2_percent_identity', 'comp_genome_3_percent_identity', 'comp_genome_4_percent_identity', 'comp_genome_5_percent_identity']]

data = []

# should be above the cutoff for the other bacteria but under for the rest
# also makes sure the other bacteria has a homolog (NaN would mean absolutely no match)
for i in range(1, len(df_filtered)):
    if (math.isnan(df_filtered.iloc[i]['comp_genome_4_percent_identity'])
        or (df_filtered.iloc[i]['comp_genome_4_percent_identity'] < ID_CUTOFF)
        or (df_filtered.iloc[i]['comp_genome_2_percent_identity'] > ID_CUTOFF)
        or (df_filtered.iloc[i]['comp_genome_3_percent_identity'] > ID_CUTOFF)
        or (df_filtered.iloc[i]['comp_genome_1_percent_identity'] > ID_CUTOFF)
        or (df_filtered.iloc[i]['comp_genome_5_percent_identity'] > ID_CUTOFF)):
        continue
    data.append(df_filtered.iloc[i].to_dict())

with open(output, "w") as f:
    json.dump(data, f)