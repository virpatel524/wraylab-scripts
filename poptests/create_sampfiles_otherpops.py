# since we need to recreate PLAFs for populations with very few members, we're going to use this script to do the holden and PLAF processing. 
import csv
import os 
import sys
import subprocess
import vcf

data = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/other/sample-population.txt'),delimiter='\t'))

stem = '/home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_samplefiles_11.13.17'

dicter = {}

for alpha in data:
	dicter.setdefault(alpha[-1], []).append(alpha[0])



for alpha in dicter:
	newfle = open(stem + '/' + '{}_samps.list'.format(alpha), 'w')
	for beta in dicter[alpha]:
		newfle.write(beta + '\n')
	newfle.close()


def check_call(name, rec):
	var = False
	for alpha in rec.samples:
		if alpha.sample == name:
			if alpha.gt_bases == None:
				var = True
	return var



newboys = ['/newhome/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_samplefiles_11.13.17/INDIA_samps.list', '/newhome/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_samplefiles_11.13.17/LAOS_samps.list', '/newhome/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_samplefiles_11.13.17/MALAYSIA_samps.list', '/newhome/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_samplefiles_11.13.17/MYANMAR_samps.list', '/newhome/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_samplefiles_11.13.17/PNG_samps.list']


for alpha in newboys:
	mastername = alpha.split('/')[-1].split('_')[0]
	process = subprocess.Popen('java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -o /nfs/wraycompute/vir/seperated_variantfiles/{}_holden.vcf -R /home/vdp5/data/reference_genomes/PVP01.fasta -V {} -sf {}'.format(mastername, '/nfs/wraycompute/vir/5iter_allvariants_filtered.heteroremove.rareremove.noheteroconsid.vcf', alpha), shell=True, stdout=subprocess.PIPE)
	process.wait()

	data = list(csv.reader(open(alpha), delimiter='\t'))
	for beta in data:
		sampname = beta[0]
		vcf_reader = vcf.Reader(open('/nfs/wraycompute/vir/seperated_variantfiles/{}_holden.vcf'.format(mastername), 'r'))
		vcf_writer = vcf.Writer(open('/nfs/wraycompute/vir/seperated_variantfiles/{}_refined.vcf'.format(sampname), 'w'), vcf_reader)

		writers = []
		plafs = []

		datplaf = open('/home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_plaf/{}_scenariominor_plaf.txt'.format(sampname), 'w')
		datplaf.write('CHROM\tPOS\tPLAF\n')
		for index, rec in enumerate(vcf_reader):
			if rec.var_type != 'snp': continue
			if check_call(sampname, rec): continue
			minorallelefreq = float(rec.aaf[0])
			datplaf.write('{}\t{}\t{}\n'.format(rec.CHROM, rec.start + 1, minorallelefreq))
			vcf_writer.write_record(rec)

		datplaf.close()
		vcf_writer.close()
