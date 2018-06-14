import os 
import csv
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--tab', help="VCF file for use")
args = parser.parse_args()

chrom2num = {}

chromlst = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/extradata/numchrom_to_pvp01.txt'),delimiter='\t'))

for beta in chromlst:
	chrom2num[beta[0]] = beta[1]

data = list(csv.reader(open(args.tab),delimiter='\t'))

sethold = []

samp = data[0][3:]


for index, beta in enumerate(samp):
	samp[index] = beta.replace('_', "-")

for beta in data[1:]:
	if beta[0] == 'LT635626': continue
	chrom = chrom2num[beta[0]]
	loc = beta[1]
	goldstan = beta[2]
	newie = []
	cunt = 0
	for alpha in beta[3:]:
		if alpha[0] == goldstan:
			newie.append('0')
		elif alpha[0] == '.':
			newie.append('-1')
		else:
			newie.append('1')
	sethold.append([chrom, loc] + newie)



nombre = args.tab.split('/')[-1].split('.tab')[0] + '.geno'

newfle = open(os.path.join('/home/vdp5/projects/vivax_cambodia/data/hmmIBD/genotype', nombre ), 'w')

newfle.write('{}\t{}\t{}\n'.format('chrom', 'pos', '\t'.join(samp)))

for beta in sethold:
	newfle.write('{}\n'.format('\t'.join(beta)))

newfle.close()



