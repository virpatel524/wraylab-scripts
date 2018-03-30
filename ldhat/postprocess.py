import os
import csv
import sys
import argparse
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="Directory for play")
parser.add_argument('--lk', help="lk files")
args = parser.parse_args()

# print args.dir

for alpha in os.listdir('{}'.format(args.dir)):
	if 'rates.txt' in alpha:
		splitter = os.path.join(args.dir, '.'.join(alpha.split('.')[:-2]) + '.')
		# print splitter
		newstr = '/newhome/vdp5/source_code/LDhat/stat -input {}rates.txt -burn 5 -loc {}locs -prefix {}'.format(splitter, splitter, splitter)
		# print newstr
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()


		chrom = splitter.split('.')[-2]
		print chrom

		newstr = 'Rscript /newhome/vdp5/source_code/LDhat/res2map.r --file {}res.txt --chr {} --out {}map'.format(splitter, chrom, splitter)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()