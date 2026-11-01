#purpose of file:
#    Counts the number of homologs for each bacteria compared against the reference genome in both files
import pandas as pd
import math

df172 = pd.read_excel("BIGb0172_comparison.xls")
df393 = pd.read_excel("BIGb0393_comparison.xls")

df172 = df172[['comp_genome_1_percent_identity', 'comp_genome_2_percent_identity', 'comp_genome_3_percent_identity', 'comp_genome_4_percent_identity', 'comp_genome_5_percent_identity']]
df393 = df393[['comp_genome_1_percent_identity', 'comp_genome_2_percent_identity', 'comp_genome_3_percent_identity', 'comp_genome_4_percent_identity', 'comp_genome_5_percent_identity']]
counts172 = [0, 0, 0, 0, 0]
count172 = 0 #kinda repetitive variable here, just checking to make sure it loops the correct amount of times
counts393 = [0, 0, 0, 0, 0]
count393 = 0


#adds to count if there's one matching per bacteria
for i in range(1, len(df172)):
    count172 += 1
    if not math.isnan(df172.iloc[i]['comp_genome_1_percent_identity']):
        counts172[0] += 1
    if not math.isnan(df172.iloc[i]['comp_genome_2_percent_identity']):
        counts172[1] += 1
    if not math.isnan(df172.iloc[i]['comp_genome_3_percent_identity']):
        counts172[2] += 1
    if not math.isnan(df172.iloc[i]['comp_genome_4_percent_identity']):
        counts172[3] += 1
    if not math.isnan(df172.iloc[i]['comp_genome_5_percent_identity']):
        counts172[4] += 1

for i in range(1, len(df393)):
    count393 += 1
    if not math.isnan(df393.iloc[i]['comp_genome_1_percent_identity']):
        counts393[0] += 1
    if not math.isnan(df393.iloc[i]['comp_genome_2_percent_identity']):
        counts393[1] += 1
    if not math.isnan(df393.iloc[i]['comp_genome_3_percent_identity']):
        counts393[2] += 1
    if not math.isnan(df393.iloc[i]['comp_genome_4_percent_identity']):
        counts393[3] += 1
    if not math.isnan(df393.iloc[i]['comp_genome_5_percent_identity']):
        counts393[4] += 1

print(f"Counts for BIGb0172 ({count172} Proteins): \n")
print("MYb11: ", counts172[0], "JUb44: ", counts172[1], "JUb19: ", counts172[2], "BIGb0393: ", counts172[3], "BIGb0170: ", counts172[4])
print(f"Counts for BIGb0393 ({count393} Proteins): \n")
print("BIGb0172: ", counts393[0], "MYb11: ", counts393[1], "JUb44: ", counts393[2], "JUb19: ", counts393[3], "BIGb0170: ", counts393[4])