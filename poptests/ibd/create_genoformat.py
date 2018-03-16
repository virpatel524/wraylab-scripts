import os
import csv
import sys
import argparse 


parser = argparse.ArgumentParser()
parser.add_argument('--tabfile', help="VCF file for use")
args = parser.parse_args()




data = list(csv.reader(open(args.tabfile),delimiter='\t'))

conversation_matrix = list(csv.reader(open('/home/vdp5/projects/vivax_cambodia/data/txt_files/extradata'),delimiter='\t'))

mat = {}

for beta in mat:
	mat[beta[0]] = beta[1]



topset = ['chrom', 'pos']

topset = topset + beta[3:]

newmix = []

for beta in data[1:]:
	news = [mat[beta[0]], beta[1]]
	anc = beta[2]
	for stuff in beta[3:]:
		if stuff[0] == anc:
			news.append('0')
		if stuff[0] == '.':
			news.append('-1')
		elif stuff[0] != anc and stuff[0] != '.':
			news.append('0')
		