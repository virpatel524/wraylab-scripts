import os
import csv
import sys
import argparse
import gzip

parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for use")

args = parser.parse_args()


nombre = args.vcffile.split('/')[-1]
newname = '/'.join(args.vcffile.split('/')[:-1]) + '/' + '.'.join(nombre.split('.')[:-2]) + '.phased.vcf.gz'
print newname

newfle = gzip.open(newname, 'wb')


counter  = 1

data = gzip.open(args.vcffile, 'rb')
for alpha in data:
	if alpha[:2] != 'LT':
		newfle.write(alpha)
	else:
		holder = alpha.split('\t')[9:]
		rest = alpha.split('\t')[:9]
		newstuff = []

		for beta in holder:
				newstuff.append(beta[:1] + '|' + beta[2:])

		newcreate = '\t'.join(rest + holder)
		newfle.write(newcreate)


newfle.close()