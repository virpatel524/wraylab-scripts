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


samp2output = {}
samp = ''

for alpha in data:
	if len(alpha[0]) == 0: continue
	if alpha[0][0] == '>':
		samp = alpha[0].split(' ')[0]
		countersamp += 1


	else:
		samp2output.setdefault(samp, []).append(alpha[0])


for beta in samp2output:
	samp2output[beta] = ''.join(samp2output[beta])
	length = len(''.join(samp2output[beta]))




name = args.fastafile
holder = name.split('.') 
holder.insert(-1, 'headeredited')
name = '.'.join(holder)

newfle = open(name, 'w')

newfle.write('{}\t{}\t{}\n'.format(countersamp, length, 1))


for alpha in samp2output:
	newfle.write('{}\n'.format(alpha))
	newfle.write(samp2output[alpha] + '\n')
newfle.close()

