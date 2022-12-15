# GISAIDutilities

GISAIDutilities is a set of tools that allows genomic scientists to deal with large datasets downloaded from GISAID to build phylogenetic trees.

GISAID is the most comprehensive public database for SARS-CoV-2 genomic data. These tools allow for the downsampling of large genomic datasets
and for renaming the headers of multiFASTA files to include lineage information and the collection date.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have Python 3 installed.
* You have a Linux machine (if you don't, minor adjustments in the code will be necessary).
* You are familiar with the data retrieved from GISAID.

## Installing GISAIDutilities

No installation is necessary. Scripts are written in bash and python and can be directly run.

## Tools

### downsampling (GISAID datasets)

A randomized, stratified downsampling code for genomic data downloaded from GISAID.

This code is useful to downsample large datasets to allow for analyses such as phylogenetic tree construction.

The main code of this project is in downsampling.py.
The input file requires some processing, since only the accession numbers are exported by GISAID in a simple CSV file.
To create the CSV file used as the input for this code, I individually filtered the search with combinations of month and lineage
and separated the resulting codes in folder containing the month information (example 'august2020') and in files containing the
lineage information (example 'B.1.csv'). Once all accession numbers were downloaded and the files and folders were properly renamed,
I used a bash command to automatically generate the input file named input_from_GISAID.csv. This bash command was written to
generate_input.sh.

This downsampling strategy is also prepared to remove accession numbers based on a restraint list, which is useful if there are unwanted sequences
that were not simple to exclude in a previous step.

### renaming (multiFASTA files)

Rewrites the headers of a multiFASTA file downloaded from GISAID to add useful information.

This is particularly useful to label the tips of phylogenetic trees with information that will facilitate the analysis: lineage and collection date.
The bash command uses as input the metadata CSV file downloaded from GISAID, which main contain some issues. The code tries to prevent common issues
but other issues can also be found, so it is important to carefully check the resulting list.

The code in rewriteFasta.py will accept a FASTA file, that can be downloaded from GISAID, as input and will create another FASTA file, with the new labels.
