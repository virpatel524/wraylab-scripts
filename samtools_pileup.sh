# for alpha in $1/*; do
# 	IFS=. read -a newarray <<< $alpha
# 	base=$(basename $alpha)
# 	if [[ ${newarray[-1]} == "bai" ]]; then
# 		continue
# 	else
# 		samtools mpileup -o /home/vdp5/data/cambodia_samples/sequences_samtools_pileup/$base.pileup --vcf -uf /home/vdp5/data/reference_genomes/PVP01.fasta $alpha 
# 	fi
# done

for alpha in ../data/sequences_samtools_pileup/*; do
	vcfutils.pl varFilter $alpha | awk '$6>=20' > ../data/sequences_pileup_edited/$(basename $alpha).final
done
