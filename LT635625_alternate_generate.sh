source ~/.bash_profile

for alpha in $1*; do
	zeta=$(basename $alpha)
	IFS='_' read -ra ADDR <<< $zeta
	newname=${ADDR[0]}
	echo "/home/vdp5/projects/vivax_cambodia/data/alternate_reference/${newname}_LT635625_alternate.fasta"
	if [[ $alpha == *".vcf.gz" ]]; then
		java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T FastaAlternateReferenceMaker -R ~/data/reference_genomes/PVP01.fasta -o "/home/vdp5/projects/vivax_cambodia/data/alternate_reference/${newname}_LT635625_alternate.fasta" -L LT635625 -V $alpha &
	fi
done