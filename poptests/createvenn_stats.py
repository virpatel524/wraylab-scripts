import vcf
import csv
import os 
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--statfile', help='File with VCF stats created from rtg vcfstats command')
args = parser.parse_args()


data = list(csv.reader(open(args.statfile),delimiter='\t'))
samp2snp = {}
samp2missing = {}



sampname = ''
for alpha in data:
	if len(alpha) == 0: continue
	if 'Sample Name' in alpha[0]:
		sampname = alpha[0].split(' ')[-1]
	else:
		if 'SNPs' in alpha[0]:
			num = int(alpha[0].split(' ')[-1])
			samp2snp[sampname] = num
		if 'Missing Genotype' in alpha[0]:
			num = int(alpha[0].split(' ')[-1])
			samp2missing[sampname] = num

print samp2snp
print samp2missing