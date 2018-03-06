for alpha in $1/*; do
	if [[ $1 != *"2.fastq.gz"* ]]; then
		IFS='.' read -ra ADDR <<< $alpha
		tmp=${ADDR[0]}
		v2=${tmp%?}2.fastq.gz
		fin=${tmp%??}.sorted
		echo $fin
		bwa mem -t 12 /newhome/vdp5/data/reference_genomes/PVP01.fasta $alpha $v2 -M  -v 2 -A 2 -L 15 -U 9 -T 75 -k 19 -w 100 -d 100 -r 1.5 -c 10000 -B 4 -O 6 -E 1 | samtools view  -Sb - | samtools sort - $fin 
	fi
done


