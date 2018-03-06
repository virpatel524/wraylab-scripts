inputdir="../../data/variant_files_v1/"
picard="/home/vdp5/source_code/picard.jar"
snpeffjar=/home/vdp5/source_code/snpEff/snpEff.jar
for alpha in ${inputdir}*.vcf; do
	bgzip $alpha
	tabix -hp vcf ${alpha}.gz
done

vcf-merge $(ls -1 ../../data/variant_files_v1/*.vcf.gz | perl -pe 's/\n/ /g')  > ../../data/cambodia_vivax_merged.vcf
java -jar $snpeffjar ann  PVP01 ../../data/cambodia_vivax_merged.vcf > ../../data/cambodia_vivax_merged.ann.vcf
java -jar ${picard} SortVcf I=../../data/cambodia_vivax_merged.ann.vcf O=../../data/cambodia_vivax_merged.ann.sorted.vcf SEQUENCE_DICTIONARY=/home/vdp5/data/reference_genomes/PVP01.dict
rm -rf ../../data/cambodia_vivax_merged.vcf ../../data/cambodia_vivax_merged.ann.vcf
