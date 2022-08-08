# Subsambling-from-GISAID
A randomized, stratified downsampling code for genomic data downloaded from GISAID.

GISAID is the most comprehensive public database for SARS-CoV-2 genomic data.

This code is useful to downsample large datasets to allows for analyses such as phylogenetic tree construction.

The main code of this project is in downsampling.py.
The input file requires some processing, since only the accession numbers are exported by GISAID in a simple CSV file.
To create the CSV file used as the input for this code, I individually filtered the search with combinations of month and lineage
and separated the resulting codes in folder containing the month information (example 'august2020') and infiles containing the
lineage information (example 'B.1.csv'). Once all accession numbers were downloaded and the files and folders were properly renamed,
I used a bash command to automatically generate the input file named input_from_GISAID.csv. This bash command was written to
generate_input.sh.

This downsampling strategy is also prepared to remove accession numbers based on a restraint list, in case of unwanted sequences
that were not simple to exclude in a previous step.
