import os
import csv
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dustmasker', help="VCF file for use")
parser.add_argument('--chrom', help="VCF file for use")
args = parser.parse_args()
linestoworkwith = []

for beta in list(csv.reader(open(args.dustmasker),delimiter='\t')):
	if beta[0] == args.chrom:
		linestoworkwith.append(beta[1:])

newfle = open('/home/vdp5/data/reference_genomes/PVP01_gapfiles/{}_gap.txt'.format(args.chrom), 'w')

newfle.write('start\tend\n')

for beta in linestoworkwith:
	newfle.write('{}\t{}\n'.format(beta[0], beta[1]))

newfle.close()