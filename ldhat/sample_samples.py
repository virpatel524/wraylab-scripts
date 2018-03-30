import os
import csv
import argparse
import sys
import random


parser = argparse.ArgumentParser()
parser.add_argument('--inputfile', help="VCF file for use")
parser.add_argument('--howmanyin', help="numberinput")
args = parser.parse_args()


data = list(csv.reader(open(args.inputfile),delimiter='\t'))

sampsize = int(args.howmanyin)

inputline = data[0]


setters = {}

src = ''

for beta in data[1:]:
	if '>' in beta[0]:
		src = beta[0]
		setters.setdefault(src, []).append(beta)
	else:
		setters.setdefault(src, []).append(beta)


print len(setters.keys()), sampsize

keepers = random.sample(setters.keys(), sampsize)


inputline[0] = str(sampsize)


newfle = open(os.path.join(args.inputfile + '.{}reduced.fasta'.format(sampsize)), 'w')

newfle.write('\t'.join(inputline) + '\n')
for samp in keepers:
	for item in setters[samp]:
		newfle.write('\t'.join(item) + '\n')
	
newfle.close()