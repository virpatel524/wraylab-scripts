import os
import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--vcftab', help="VCF file for use")
parser.add_argument('--poplab', help='pop labels')
args = parser.parse_args()


data = list(csv.reader(open(args.vcftab),delimiter='\t'))


kagra = '.'.join(args.vcftab.split('.')[:-1])

newfle_tree = open('{}.treemix_input'.format(kagra), 'w')



poplabels = list(csv.reader(open(args.poplab),delimiter='\t'))
dataset_add = []

popstr = ''

for alpha in data[1:]:
	categories = {}
	ref = alpha[2]
	for i in range(len(alpha[3:])):
		pop = poplabels[i][0]
		snp = alpha[3:][i].split('/')
		if snp[1] == '.':
			continue
		if snp[1] != ref and pop not in categories:
			categories[pop] = [0, 1]
		if snp[1] == ref and pop not in categories:
			categories[pop] = [1, 0]
		if snp[1] != ref and pop in categories:
			categories[pop][1] = categories[pop][1] + 1
		if snp[1] == ref and pop in categories:
			categories[pop][0] = categories[pop][0] + 1
	popstr = ' '.join(sorted(categories.keys()))
	beg = ''
	for country in poplabels:
		if country[0] not in categories:
			categories[country[0]] = [0,0] 
	popstuff = sorted(categories.keys())	
	for i in range(len(popstuff)):
		if i != len(popstuff) - 1:
			beg += '{},{} '.format(categories[popstuff[i]][0],categories[popstuff[i]][1])
		else:
			beg += '{},{}\n'.format(categories[popstuff[i]][0],categories[popstuff[i]][1])
        dataset_add.append(beg)

newfle_tree.write(popstr + '\n')

for alpha in dataset_add:
        newfle_tree.write(alpha)

	

newfle_tree.close()
