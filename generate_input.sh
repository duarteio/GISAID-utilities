for file in */*
do
	mes=$( echo $file | cut -d\/ -f1 | rev | cut -c 5- | rev )
	ano=$( echo $file | cut -d\/ -f1 | rev | cut -c -4 | rev )
	linhagem=$( echo $file | cut -d\/ -f2 | rev | cut -c 5- | rev )
	for line in $( cat $file )
	do
		echo -e $linhagem'\t'$mes'\t'$ano'\t'$line >> lista.tsv
	done
done
