import os 
import argparse
import csv
import sys
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="VCF file for use")
args = parser.parse_args()

for beta in os.listdir(args.dir):
	if beta[-2:] == 'gz':
		file = os.path.join(args.dir, beta)
		newstuff = '.'.join(file.split('.')[:-2]) + '.phased'
		newstr = 'java -Xss5m -jar /newhome/vdp5/source_code/beagle.27Jan18.7e1.jar gt={} out={}'.format(file, newstuff)
		print newstr
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

