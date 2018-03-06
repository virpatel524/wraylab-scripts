import os 
import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--vcftab', help="VCF file for use")
parser.add_argument('--poplab', help='pop labels')

args = parser.parse_args()
data = list(csv.reader(open(args.vcftab),delimiter='\t'))


kagra = '.'.join(args.vcftab.split('.')[:-1])

newfle_tab = open('{}.geno'.format(kagra), 'w')
newfle_snp = open('{}.snp'.format(kagra), 'w')
newfle_samp = open('{}.ind'.format(kagra), 'w')


poplabels = list(csv.reader(open(args.poplab),delimiter='\t'))

counter = 0
for alpha in data[1:]:
	counter += 1
	ref = alpha[2]
	stringer = ''
	for beta in alpha[3:]:
		tmp = beta.split('/')
		if tmp[0] == '.':
			stringer += '9'
		elif tmp[0] == ref and tmp[1] == ref:
			stringer += '2'
		elif tmp[0] == ref and tmp[1] != ref:
			stringer += '0'
		elif tmp[0] != ref and tmp[1] != ref:
			stringer += '0'
	newfle_tab.write('{}\n'.format(stringer))
	newfle_snp.write('snp{}\t{}\t{}\t{}\n'.format(counter, alpha[0], 0.0, alpha[1]))

for i in range(len(data[0])):
	if i < 3:
		continue
	print i
	pop = poplabels[i-3][0]
	samp = data[0][i]
	newfle_samp.write('{}\tU\t{}\n'.format(samp, pop))

newfle_samp.close()
newfle_tab.close()
newfle_snp.close()