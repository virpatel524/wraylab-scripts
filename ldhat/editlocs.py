import os 
import csv
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--tabfile', help="VCF file for use")
parser.add_argument('--loc', help="VCF file for use")
args = parser.parse_args()


locdata = list(csv.reader(open(args.loc),delimiter='\t'))
tabdata = list(csv.reader(open(args.tabfile),delimiter='\t'))

loclst = []

tot = locdata[0][0].split(' ')[1]

newfle = open(args.loc + '.tmp', 'w')
for beta in tabdata[1:]:
	loclst.append(beta[1])

print loclst

newfle.write('{} {} {}\n'.format(len(loclst), tot, 'L'))

for beta in loclst:
	newfle.write('{}.000\n'.format(beta))


