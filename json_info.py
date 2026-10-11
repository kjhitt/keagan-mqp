#purpose of file:
#    prints length of json file

import json

with open("BIGb0172_comparison.json", "r") as f:
    data = json.load(f)

print(len(data))