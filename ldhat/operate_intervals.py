import os
import sys
import csv
import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--dir_list', help="Where intervals stored")
parser.add_argument('--dir_vcf', help="Where intervals stored")
args = parser.parse_args()

for beta in os.listdir(args.dir_vcf):
	print beta 
	if beta[-2:] == 'gz' and 'relevantloci' not in beta:
		vcf = os.path.join(args.dir_vcf, beta)
		chrom = vcf.split('.')[-3]
		for alpha in os.listdir(args.dir_list):
			if '.list' in alpha and chrom in alpha:
				intervalfle = os.path.join(args.dir_list, alpha)
		root = vcf.split('.')[:-1]
		root = root + ['relevantloci','vcf'] 
		root = '.'.join(root)
		newstr = 'java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R /newhome/vdp5/data/reference_genomes/PVP01.fasta -V {} -L {} -o {}'.format(vcf, intervalfle, root)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()


