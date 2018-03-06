cd /home/vdp5/projects/vivax_cambodia/scripts
while read line; do
	echo $line
	bash /newhome/vdp5/projects/vivax_cambodia/scripts/annotated_faststructure_run.sh ${line} &
done </newhome/vdp5/projects/vivax_cambodia/data/other/genes_interest.txt


