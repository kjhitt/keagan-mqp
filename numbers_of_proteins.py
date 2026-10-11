fileName = "../Proteins/MYb11.faa"

with open(fileName, "r") as file:
    lines = file.readlines()

protein_count = sum(1 for line in lines if line.startswith(">"))
print(f"Number of proteins in {fileName}: {protein_count}")