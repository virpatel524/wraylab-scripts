snpeffjar=/home/vdp5/source_code/snpEff/snpEff.jar

#run from within directory of interest

joinx vcf-merge $(ls -1 *.vcf.gz | perl -pe 's/\n/ /g')  > cambodia_vivax_merged.vcf
java -jar $snpeffjar PVP01 cambodia_vivax_merged.vcf > cambodia_vivax_merged.vcf.ann

