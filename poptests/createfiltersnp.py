import argparse
import csv


data = list(csv.reader(open('/newhome/vdp5/data/reference_genomes/PVP01.geneslist'),delimiter='\t'))

newfile = open('/home/vdp5/projects/vivax_cambodia/scripts/poptests/extractgenevariants.sh', 'w')


for alpha in data:
	newfile.write('java -jar /newhome/vdp5/source_code/snpEff/SnpSift.jar filter "(ANN[*].GENE = \'{}\')" /nfs/wraycompute/vir/variant_storage/5iter_allvariants_filtered.heteroremove.rareremove.ann.vcf > /home/vdp5/projects/vivax_cambodia/data/variant_storage/genevariants/{}.vcf\n'.format(alpha[0], alpha[0]))
