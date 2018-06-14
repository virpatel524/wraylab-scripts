import os
import sys
import argparse
import csv
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="Directory containing Phased VCF")
parser.add_argument('--mapdir', help="Directory containing map files")

parser.add_argument('--output', help="output directory")
args = parser.parse_args()


for alpha in os.listdir(args.dir):
	root = '.'.join(alpha.split('.')[:-1] + ['nsl', 'out'])
	output = os.path.join(args.output, root)
	chrom = alpha.split('.')[-4]
	phasedpath = os.path.join(args.dir, alpha)
	for beta in os.listdir(args.mapdir):
		if chrom in beta:
			mapfle = os.path.join(args.mapdir, beta)
	newstr = 'selscan --nsl --map {} --vcf {} --out {} --keep-low-freq --trunc-ok --threads 8'.format(mapfle, phasedpath, output)
	print newstr
	process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
	process.wait()

