sed -e 's/ /_/g' metadata.tsv | awk -v OFS=@ '{print $1,$18,$19,$5}' | sed 's/?@//' | sed 's/GR@//' | sed 's/G@//' | sed 's/O@//' | sed 's/GRY@//' > new_headers.txt
