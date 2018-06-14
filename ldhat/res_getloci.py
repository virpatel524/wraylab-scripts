import os
import sys
import csv
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="Directory to iterate over")
args = parser.parse_args()


for alpha in os.listdir('{}'.format(args.dir)):
	if 'res.txt' in alpha:
		splitter = os.path.join(args.dir, '.'.join(alpha.split('.')[:-2]) + '.')
		chrom = splitter.split('.')[-3]	
		newfle_loci = open(splitter + 'list', 'w')
		dat = list(csv.reader(open(os.path.join(args.dir, alpha)),delimiter='\t'))[2:]
		for beta in dat:
			newfle_loci.write('{}:{}-{}\n'.format(chrom, beta[0].split(' ')[-1].split('.')[0],  beta[0].split(' ')[-1].split('.')[0]))
		newfle_loci.close()

		newstr = ' ./res2map.r --file {}res.txt --chr {} --out {}map'.format(os.path.join(args.dir, splitter), chrom, os.path.join(args.dir, splitter))
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()
