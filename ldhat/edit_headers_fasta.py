import os 
import csv
import sys
import argparse

#output will be released with .headeredited. tag


parser = argparse.ArgumentParser()
parser.add_argument('--fastafile', help="FASTA file for use")
args = parser.parse_args()


data = list(csv.reader(open(args.fastafile),delimiter='\t'))

newholder = []
length = 0

countersamp = 0

ifnotcontainer = 0


for alpha in data:
	if len(alpha) == 0: continue
	if alpha[0][0] == '>':
		countersamp += 1
		txt = alpha[0]
		if ifnotcontainer != 0:
			length = ifnotcontainer
			ifnotcontainer = 0
		newholder.append(txt.split('-')[0])

	else:
		newholder.append(alpha[0])
		ifnotcontainer += len(alpha[0])

name = args.fastafile
holder = name.split('.') 
holder.insert(-1, 'headeredited')
name = '.'.join(holder)

newfle = open(name, 'w')

newfle.write('{}\t{}\t{}\n'.format(countersamp, length, 1))


for alpha in newholder:
	newfle.write(alpha + '\n')

newfle.close()