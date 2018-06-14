import os
import sys
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="dir with output")
args = parser.parse_args()



newfle = open(os.path.join(args.dir, 'total_nsl.txt'), 'w')


for beta in os.listdir(args.dir):
	if '100bins.norm' in beta:
		chrom = beta.split('.')[6]
		data = list(csv.reader(open(os.path.join(args.dir, beta)),delimiter='\t'))
		for i in data:
			loc = i[1]
			nsl = abs(float(i[-2]))
			newfle.write('{}\t{}\t{}\t{}\n'.format('{}_{}'.format(chrom, loc), chrom, loc, nsl))

newfle.close()