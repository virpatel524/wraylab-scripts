rm -rf /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2
mkdir -p /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2

# java -jar /home/vdp5/source_code/snpEff/SnpSift.jar filter "(ANN[*].GENE = '${2}')" /newhome/vdp5/projects/vivax_cambodia/data/var_processing/se_asia_4.10.17.ann.vcf > ../../data/extracted_vcf/${2}_extracted.ann.vcf


for alpha in $1/*.bam; do
	zeta=$(basename $alpha)
	IFS='.' read -ra ADDR <<< $zeta
	zeta=${ADDR[0]}
	java -jar ~/source_code/GenomeAnalysisTK.jar -T SelectVariants -sn $zeta --excludeNonVariants -V ../../data/extracted_vcf/${2}_extracted.ann.vcf -o /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.vcf -R /home/vdp5/data/reference_genomes/PVP01.fasta
	java -jar ~/source_code/GenomeAnalysisTK.jar -T FastaAlternateReferenceMaker -R /home/vdp5/data/reference_genomes/PVP01.fasta -o /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta_tmp -V ../../data/extracted_vcf/${2}_extracted.ann.vcf -L LT635623:2430567-2444082
	sed "s/>.*/>${zeta}_${2}/g"  /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta_tmp > /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta
	rm -rf /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.vcf* /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/$zeta.fasta_tmp
done

cat /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/* >  /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/all_reference_$2.fasta

mafft --auto /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/all_reference_$2.fasta --thread 8 >  /home/vdp5/projects/vivax_cambodia/data/alternate_reference/$2/all_reference_$2_aligned.fasta

