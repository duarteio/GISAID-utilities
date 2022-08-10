import pandas as pd
import os

gisaid_accnums = pd.read_csv("input_from_gisaid.tsv")

#1: ignoring restraints, if there are any
# My restraints are simply a file listing the accession numbers that don't interest me. So this informationa can be stored to a list.
# For more complex restraints, a few lines should be added to the code.
restraint_codes = [i.strip() for i in open("restraints.csv","r").readlines()]
gisaid_accnums = gisaid_accnums.loc[~gisaid_accnums["accnum"].isin(restraint_codes)].reset_index(drop=True)

#2: subsample
# I am subsampling to get up to 500 accession numbers, by stratified randomization, considering one or more variables.
# Here, my variables are lineage and month. The number of samples from each group is either 30 or the length of the group,
# whichever is lowest. This number can be altered depending on the case, we set it to 30 because it yielded a final dataset
# of aproximately 500 sequences.
subsampled = gisaid_accnums.groupby(['lineage','month'], group_keys=False).apply(lambda x: x.sample(min(len(x), 30))).reset_index(drop=True)

#3: create the output
# The output is the ideal format for submitting to the GISAID website to create an EPI_SET.
for i in list(subsampled["accnum"]):
    open("subset_ids.txt","a").write(i+",")

with open("subset_ids.txt","rb+") as idfile:
    idfile.seek(-1,os.SEEK_END)
    idfile.truncate()
