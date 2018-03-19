import os
import sys
import csv
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--pop1', help="VCF file for use")
parser.add_argument('--pop2', help="VCF file for use")
parser.add_argument('--dir', help="VCF file for use")
args = parser.parse_args()

for alpha in os.listdir('{}'.format(args.dir)):
	if '.map' in alpha:
		splitter = os.path.join(args.dir, '.'.join(alpha.split('.')[:-1]) + '.')
		splitter_xpehh_one = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/xp-ehh', args.pop1, '.'.join(alpha.split('.')[:-1]))
		splitter_xpehh_two = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/xp-ehh', args.pop2, '.'.join(alpha.split('.')[:-1]))


		chrom = splitter.split('.')[-2]
		vcfstorone = os.path.join(args.dir, 'vcfedited', args.pop1)
		vcfstortwo = os.path.join(args.dir, 'vcfedited', args.pop2)

		vcfwewantone = ''
		for beta in os.listdir(vcfstorone):
			if chrom in beta and beta[-2:] == 'gz':
				vcfwewantone = os.path.join(vcfstorone, beta)


		vcfwewanttwo = ''
		for beta in os.listdir(vcfstortwo):
			if chrom in beta and beta[-2:] == 'gz':
				vcfwewanttwo = os.path.join(vcfstortwo, beta)


		newstr = 'selscan --threads 8 --xpehh --map {} --vcf {} --vcf-ref {} --out {} '.format(os.path.join(args.dir, alpha), vcfwewantone, vcfwewanttwo, splitter_xpehh_one)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

		newstr = 'selscan --threads 8 --xpehh --map {} --vcf {} --vcf-ref {} --out {} '.format(os.path.join(args.dir, alpha), vcfwewanttwo, vcfwewantone, splitter_xpehh_two)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()
