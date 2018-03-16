import os
import csv
import sys
import argparse
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="Directory for play")
parser.add_argument('--vcfdir', help="Directory for play")
args = parser.parse_args()

if not os.path.isdir('{}/vcfedited'.format(args.dir)):
	os.mkdir('{}/vcfedited'.format(args.dir))

for alpha in os.listdir('{}'.format(args.dir)):
	if 'rates.txt' in alpha:
		splitter = os.path.join(args.dir, '.'.join(alpha.split('.')[:-2]) + '.')
		newstr = '/newhome/vdp5/source_code/LDhat/stat -input {}rates.txt -burn 5 -loc {}locs.txt -prefix {}'.format(splitter, splitter, splitter)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()


		chrom = splitter.split('.')[-2]

		newstr = 'Rscript /newhome/vdp5/source_code/LDhat/res2map.r --file {}res.txt --chr {} --out {}map'.format(splitter, chrom, splitter)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

		newtxt = list(csv.reader(open('{}map'.format(splitter)),delimiter='\t'))
		newset = []

		for beta in newtxt:
			beta[-1] = beta[-1][:-3]

		newfle = open('{}list'.format(splitter),'w')
		for beta in newtxt:
			tmp = beta[0].split(' ')
			if 'e' in tmp[-1]: continue
			newfle.write('{}:{}-{}\n'.format(tmp[0], tmp[-1], tmp[-1]))

		newfle.close()

		splitsme = splitter + 'edited.vcf'
		splitsme = splitsme.split('/')
		tmp = splitsme[-1]
		splitsme[-1] = 'vcfedited'
		splitsme = splitsme + [tmp,]
		newpath = '/'.join(splitsme)

		# newfle = open('{}map'.format(splitter),'w')
		# for beta in newtxt:
		# 	tmp = beta[0].split(' ')[-1]
		# 	if 'e' in tmp: continue
		# 	newfle.write('{}\n'.format('\t'.join(beta)))

		# newfle.close()

		filme = ''
		for it in os.listdir(args.vcfdir):
			if chrom in os.path.join(args.vcfdir, it):
				if it[-2:] == 'gz':
					filme = os.path.join(args.vcfdir, it)

		print filme

		# newstr = 'java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -L {}list -R $PVP01REF -V {} -o {}'.format(splitter, filme, newpath)
		# print newstr
		# process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		# process.wait()

