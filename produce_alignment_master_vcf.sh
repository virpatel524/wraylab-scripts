mkdir /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2

for alpha in $1/*.bam; do
	zeta=$(basename $alpha)
	IFS='.' read -ra ADDR <<< $zeta
	zeta=${ADDR[0]}
	java -jar ~/source_code/GenomeAnalysisTK.jar -T SelectVariants -sn $zeta -L $2 --excludeNonVariants -V /newhome/vdp5/projects/vivax_cambodia/data/var_processing/se_asia_4.10.17.vcf -o /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.vcf -R /home/vdp5/data/reference_genomes/PVP01.fasta
	java -jar ~/source_code/GenomeAnalysisTK.jar -T FastaAlternateReferenceMaker -L $2 -R /home/vdp5/data/reference_genomes/PVP01.fasta -o /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta_tmp -V /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.vcf
	sed "s/>.*/>${zeta}_${2}/g"  /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta_tmp > /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta
	rm -rf /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.vcf* /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta_tmp
done

cat /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/* >  /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/all_reference_$2.fasta
