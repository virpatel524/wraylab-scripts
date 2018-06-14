import os 
import sys
import csv
import argparse
csv.field_size_limit(sys.maxsize)

parser = argparse.ArgumentParser()
parser.add_argument('--stem', help="Stem of PED and MAP")
parser.add_argument('--mapdir', help="where the map files are held")
parser.add_argument('--converter', help="where the conversion happens")
args = parser.parse_args()


condat = list(csv.reader(open(args.converter),delimiter='\t'))

condor_dict = {}


for alpha in condat:
	condor_dict[alpha[0]] = alpha[-1]



mapfle = list(csv.reader(open(args.stem + 'map'),delimiter='\t'))
pedfle = list(csv.reader(open(args.stem + 'ped'),delimiter=' '))


newset = []


chrommap = ''

for beta in mapfle:
	chrom = beta[0]
	loc = beta[-1]
	if chrom != chrommap:
		chrommap = chrom
		for it in os.listdir(args.mapdir):
			if chrommap in it:
				mapdat = list(csv.reader(open(os.path.join(args.mapdir, it)),delimiter=' '))

	for theta in mapdat:
		if theta[-1] == loc and theta[0] == chrom:
			newset.append([chrom, '{}_{}'.format(chrom, theta[1]), theta[2], theta[3]])
			break


newfle = open(args.stem + 'new.map', 'w')

print newset[0]


for beta in newset:
	newfle.write('{}\n'.format('\t'.join(beta)))

newfle.close()

newset = []

for beta in pedfle:
	tmp = beta[:]
	tmp[0] = condor_dict[beta[0]]
	tmp[4] = '1'
	newset.append(tmp)

pedfle = []

newfle = open(args.stem + 'new.ped', 'w')

for beta in newset:
	newfle.write('{}\n'.format(' '.join(beta)))

newfle.close()