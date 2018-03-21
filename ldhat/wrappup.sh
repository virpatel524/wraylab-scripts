dir=${1}
samnum=${2}
lkfile=${3}
vcf=${4}

python2.7 /newhome/vdp5/projects/vivax_cambodia/scripts/ldhat/setup_of_regions.py --vcffile ${vcf} --out ${dir} --ncount ${samnum}

for alpha in ${dir}/*fasta; do
	python2.7 /newhome/vdp5/projects/vivax_cambodia/scripts/ldhat/edit_headers_fasta.py --fastafile ${alpha}
done

