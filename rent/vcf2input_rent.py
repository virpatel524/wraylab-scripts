import csv
import sys
import argparse
import vcf


parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for use")
parser.add_argument('--output', help="output prefix")

args = parser.parse_args()


vcf_reader = vcf.Reader(filename='{}'.format(args.vcffile))

for record in vcf_reader:
	print record
