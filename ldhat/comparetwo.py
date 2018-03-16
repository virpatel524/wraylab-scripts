import argparse
import csv
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('--tab', help="VCF file for use")
parser.add_argument('--map', help="VCF file for use")

args = parser.parse_args()

tabdict = []


for beta in list(csv.reader(open(args.tab),delimiter='\t'))[1:]:
	tabdict.append(beta[1])

for beta in list(csv.reader(open(args.map),delimiter=' ')):
	if beta[-1][:-3] not in tabdict:
		print beta
