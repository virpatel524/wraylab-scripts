import os
import sys
import csv
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="VCF file for use")
parser.add_argument('--mapdir', help="Directory with map file")

args = parser.parse_args()


for beta in os.listdir(args.dir):
	if 'relevantloci' in beta and 'phased' not in beta:
		newpath = os.path.join(args.dir, beta)
		chrom = beta.split('.')[-4]
		if chrom == 'LT635627': continue
		print newpath
		root = beta.split('.')[:-3]
		newroot = root + ['relevantloci', 'phased']
		newroot = '.'.join(newroot)
		newroot = os.path.join(args.dir, newroot)
		for alpha in os.listdir(args.mapdir):
			if '.map' in alpha and chrom in alpha:
				mapfle = os.path.join(args.mapdir, alpha)
		newstr = 'java -jar /newhome/vdp5/source_code/beagle.27Jan18.7e1.jar gt={} ne=30353 map={} out={}'.format(newpath, mapfle, newroot)
		# print newstr
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

