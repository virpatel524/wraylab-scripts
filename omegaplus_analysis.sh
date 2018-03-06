mkdir -p $1 

java -jar ~/source_code/GenomeAnalysisTK.jar -T FastaAlternateReferenceMaker -R $PVP01REF -o alternate_out.fasta -L $2 -V /newhome/vdp5/projects/vivax_cambodia/data/allvar_sorted.ann.vcf