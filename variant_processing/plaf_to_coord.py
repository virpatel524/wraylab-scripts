import os 
import csv
import sys
import subprocess

for filename in os.listdir('/home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_plaf'):
	sample = filename.split('_scenariominor_plaf.txt')[0]
	fullshit = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_plaf', filename)
	newfle = open('/home/vdp5/projects/vivax_cambodia/data/poptests/deploid/coordinatefiles/{}_coordinates.list'.format(filename.split('_scenariominor_plaf.txt')[0]), 'w')
	data = list(csv.reader(open(fullshit),delimiter='\t'))
	for alpha in data[1:]:
		newfle.write('{}:{}-{}\n'.format(alpha[0], alpha[1], int(alpha[1])))
	newfle.close()
	process = subprocess.Popen('java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -o /home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_samplefiles_11.20.17/{}_alone.vcf -R /home/vdp5/data/reference_genomes/PVP01.fasta -V /nfs/wraycompute/vir/variant_storage/5iter_allvariants_filtered.heteroremove.rareremove.noheteroconsid.vcf -sn {} -L {}'.format(sample, sample,'/home/vdp5/projects/vivax_cambodia/data/poptests/deploid/coordinatefiles/{}_coordinates.list'.format(sample)), shell=True, stdout=subprocess.PIPE)
	process.wait()

