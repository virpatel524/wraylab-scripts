cd /nfs/wraycompute/vir/test
rm -rf /home/vdp5/projects/vivax_cambodia/data/other/samplenames.txt 


for alpha in /nfs/wraycompute/vir/mapped/*; do
	IFS='.' read -ra ADDR <<< $(basename $alpha)
	echo $(basename $alpha)	>> /home/vdp5/projects/vivax_cambodia/data/other/samplenames.txt
	nam=$(basename $alpha)
	 java -jar ~/source_code/picard.jar MarkDuplicates I=${alpha} O=${nam}.sorted.marked.bam M=~/tmp/marko.txt VALIDATION_STRINGENCY=LENIENT
done

