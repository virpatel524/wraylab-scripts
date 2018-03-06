import os
import sys
import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--fastafile', help="VCF file for use")
args = parser.parse_args()

data =  list(csv.reader(open(args.fastafile),delimiter='\t'))

createholder = {}

chrom = ''

for beta in data:
	if beta[0][0] == '>':
		chrom = beta[0]
	else:
		createholder.setdefault(chrom, []).append(beta[0])

fused = {}

for beta in createholder:
	newstuff = ''.join(createholder[beta])
	fused[beta] = newstuff


newfle = open(args.fastafile + '.oneline.fas', 'w')

for beta in fused:
	newfle.write(beta + '\n')
	newfle.write(fused[beta] + '\n')

newfle.close()