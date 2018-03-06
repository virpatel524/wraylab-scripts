import os 
import csv 
import argparse
import subprocess
import vcf
import numpy
import sys

def check_call(name, rec):
	var = False
	for alpha in rec.samples:
		if alpha.sample == name:
			if alpha.gt_bases == None:
				var = True
	return var

parser = argparse.ArgumentParser()
parser.add_argument('--sampfile', help="samples that we will process")
parser.add_argument('--vcffile', help="VCF file that will be cut up")
args = parser.parse_args() 

sampfile = args.sampfile 
vcffile = args.vcffile

sampname = sampfile.split('/')[-1].split('.')[0]

process = subprocess.Popen('java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -o /nfs/wraycompute/vir/seperated_variantfiles/{}_holden.vcf -R /home/vdp5/data/reference_genomes/PVP01.fasta -V {} -sf {}'.format(sampname, args.vcffile, sampfile), shell=True, stdout=subprocess.PIPE)
process.wait()

vcf_reader = vcf.Reader(open('/nfs/wraycompute/vir/seperated_variantfiles/{}_holden.vcf'.format(sampname), 'r'))
vcf_writer = vcf.Writer(open('/nfs/wraycompute/vir/seperated_variantfiles/{}_refined.vcf'.format(sampname), 'w'), vcf_reader)

writers = []
plafs = []

datplaf = open('/home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_plaf/{}_scenariominor_plaf.txt'.format(sampname), 'w')
datplaf.write('CHROM\tPOS\tPLAF\n')
for index, rec in enumerate(vcf_reader):
	if rec.var_type != 'snp': continue
	if rec.num_called == 0:
		continue
	print rec.num_called
	if check_call(sampname, rec): continue
	minorallelefreq = float(rec.aaf[0])
	datplaf.write('{}\t{}\t{}\n'.format(rec.CHROM, rec.start + 1, minorallelefreq))
	vcf_writer.write_record(rec)

datplaf.close()
vcf_writer.close()