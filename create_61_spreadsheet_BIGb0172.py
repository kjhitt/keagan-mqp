#purpose of file:
#    Takes the IDs from the 61 proteins, then makes a spreadheet
#    with each protein, sequence identity between BIGb0172 and BIGb0393,
#    annotated function, amino acid sequence, and 

import pandas as pd
from Bio import SeqIO

#defining files here
ids_path = "61ProteinsBIGb0172.txt"
genomic_path = "C:\\Users\\kh1\\OneDrive\\Documents\\WPI\\MQP\\Unzipped Assemblies\\BIGb0172\\ncbi_dataset\\data\\GCF_014109725.1\\genomic.gbff"
output = "proteins_with_data.xlsx"

df = pd.read_csv(ids_path, sep=r"\s+") #reads the text file

annots = {} #annotations dict

#parses the genomic file (thank you Biopython)
for record in SeqIO.parse(genomic_path, "genbank"):
    for feature in record.features:
        if feature.type != "CDS":
            continue #means it doesn't code a protein

        qualifiers = feature.qualifiers

        protein_ids = qualifiers.get("protein_id", [])

        if not protein_ids:
            continue #protein ID doesn't exist somehow!

        protein_id = protein_ids[0]

        #get the things i want
        old_locus_tag = qualifiers.get("old_locus_tag", [""])[0]
        product = qualifiers.get("product", [""])[0]
        translation = qualifiers.get("translation", [""])[0]

        #adds it to the dictionary so that when searching a protein_id, this information can be found
        annots[protein_id] = {
            "old_locus_tag": old_locus_tag,
            "product": product,
            "translation": translation
        }

#can now add the columns to the dataframe!
df["old_locus_tag"] = df["protein_id"].map(
    lambda x: annots.get(x, {}).get("old_locus_tag", "")
)

df["product"] = df["protein_id"].map(
    lambda x: annots.get(x, {}).get("product", "")
)

df["translation"] = df["protein_id"].map(
    lambda x: annots.get(x, {}).get("translation", "")
)

df.to_excel(output, index=False) #writes to output

print(f"Saved to {output}!")