import os
import sys
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for use")
parser.add_argument('--output', help="output file")
args = parser.parse_args()

data = list(csv.reader(open(args.vcffile),delimiter='\t'))
newset = []
chromset = []

for alpha in data:
	if alpha[0][0] == '#':
		continue
	else:
		chromset.append(alpha[0])

chromset = sorted(list(set(chromset)))

newcorresponding = {}

counter = 0
for alpha in chromset:
	if 'LT' not in alpha: continue
	counter += 1
	newcorresponding[alpha] = str(counter)

newflecoord = open('/home/vdp5/projects/vivax_cambodia/data/other/vcf_coordiantes_12.2.17.txt','w')

for alpha in newcorresponding:
	newflecoord.write('{}\t{}\n'.format(alpha, newcorresponding[alpha]))

newflecoord.close()

newfle = open(args.output, 'w')

for index, alpha in enumerate(data):
	for beta in newcorresponding:
		for i in range(len(alpha)):
			if beta in alpha[i]:
				alpha[i] = alpha[i].replace(beta, newcorresponding[beta])

for alpha in data:
	newfle.write('\t'.join(alpha) + '\n')

newfle.close()

