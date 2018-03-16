import os
import csv
import argparse
import sys
import random


parser = argparse.ArgumentParser()
parser.add_argument('--inputfile', help="FASTA file for use")
parser.add_argument('--howmanyin', help="numberinput")
args = parser.parse_args()


data = list(csv.reader(open(args.inputfile),delimiter='\t'))

sampsize = int(args.howmanyin)

inputline = data[0]


setters = {}

src = 'DICS'

for beta in data:
	if '>' in beta[0]:
		src = beta[0].split(' ')[0]
	else:
		setters.setdefault(src, []).append(beta)



print setters.keys()
keepers = random.sample(setters.keys(), sampsize)



print len(keepers)

inputline[0] = str(sampsize)


newfle = open(os.path.join(args.inputfile + '.{}reduced.fasta'.format(sampsize)), 'w')

cunter = 0
print(len(keepers))
for samp in keepers:
	cunter += 1
	print cunter
	newfle.write(samp + '\n')
	for item in setters[samp]:
		newfle.write('\t'.join(item) + '\n')
	
newfle.close()
