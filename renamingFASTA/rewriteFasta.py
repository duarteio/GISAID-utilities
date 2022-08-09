fasta = open("../../datasetB.fasta","r")
new_headers = [i.strip() for i in open("new_headers.txt","r").readlines()]
output_fasta = open("renamed_datasetB.fasta","a")
while True:
	line = fasta.readline().strip()
	if line == "":
		break
	if line.startswith(">"):
		for header in new_headers:
			if header.split("@")[0] == line.split(">")[1]:
				output_fasta.write(">"+header+"\n")
	else:
		output_fasta.write(line+"\n")
