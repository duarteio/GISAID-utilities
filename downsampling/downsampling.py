import pandas as pd

gisaid_accnums = pd.read_csv("input_from_gisaid.tsv")

#1: ignoring restraints, if there are any
# My restraints are simply a file listing the accession numbers that don't interest me. So this informationa can be stored to a list.
# For more complex restraints, a few lines should be added to the code.
restraint_codes = [i.strip() for i in open("restraints.csv","r").readlines()]
gisaid_accnums = gisaid_accnums.loc[~gisaid_accnums["accnum"].isin(restraint_codes)].reset_index(drop=True)

#2: subsample
# I am subsampling to get up to 500 accession numbers, by stratified randomization, considering one or more variables.
# Here, my variables are lineage and month.
subsampled = gisaid_accnums.groupby(['lineage','month'], group_keys=False).apply(lambda x: x.sample(min(len(x), 30))).reset_index(drop=True)

#3: create output
for i in list(subsampled["accnum"]):
    open("subset_ids.txt","a").write(i+",")