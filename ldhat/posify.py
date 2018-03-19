import os 
import csv
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="VCF file for use")
parser.add_argument('--colfromend', help="VCF file for use")
args = parser.parse_args()

for alpha in os.listdir(args.dir):
	if alpha[-3:] == 'out':
		newpath = os.path.join(args.dir, alpha)
		data = list(csv.reader(open(newpath),delimiter='\t'))
		for index, beta in enumerate(data[1:]):
			tmp = data[index + 1]
			tmp[int(args.colfromend)] = str(abs(float(tmp[int(args.colfromend)])))
			data[index] = tmp
		
		newfle = open(os.path.join(args.dir, alpha), 'w')
		for beta in data:
			newfle.write('\t'.join(beta) + '\n')
		newfle.close()





