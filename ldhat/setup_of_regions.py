import os
import csv
import sys
import argparse
import subprocess
import random


parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for use")
parser.add_argument('--out', help="outputregion")
parser.add_argument('--ncount', help="outputregion")

args = parser.parse_args()


lendict = {}

lengthdata = list(csv.reader(open('/newhome/vdp5/data/reference_genomes/PVP01.lengths'),delimiter='\t'))
for beta in lengthdata:
	lendict[beta[0]] = int(beta[1])


newstr = 'bcftools query -l {} > /tmp/samplelst.txt'.format(args.vcffile)
process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
process.wait()

# newstr = 'zcat {} | vcf-to-tab > {}.tab'.format(args.vcffile, args.vcffile)
# process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
# process.wait()

chrom2subjects = {}
chrom2locs = {}
subjects2chrom2value = {}
tabfile = list(csv.reader(open('{}.tab'.format(args.vcffile)),delimiter='\t'))


subjects = tabfile[0][3:]


for alpha in tabfile[1:]:
	chrom2subjects.setdefault(alpha[0], []).append(int(alpha[1]))


for alpha in chrom2subjects:
	print alpha, len(chrom2subjects[alpha])

vcfparse = '.'.join(args.vcffile.split('/')[-1].split('.')[:-1])


samples = list(csv.reader(open('/tmp/samplelst.txt'),delimiter='\t'))

for chrom in lendict:
	if 'LT' in chrom:

		newstr = 'python2.7 /newhome/vdp5/source_code/alignment-from-vcf/alignment-from-vcf.py $PVP01REF {} {} 1 {} 1 {}/{}.{}.fasta'.format(args.vcffile, chrom, lendict[chrom], args.out, vcfparse, chrom)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()


		locs = open('{}/{}.{}.locs'.format(args.out, vcfparse, chrom), 'w')

		lst = sorted(chrom2subjects[chrom])

		lst = [str(a) for a in lst]

		tmpstorage = {}

		lenster = 0


		locs.write('{}\t{}\t{}\n'.format(len(lst), lendict[chrom], 'L'))

		locs.write('{}\n'.format('\t'.join(lst)))
		locs.close()



