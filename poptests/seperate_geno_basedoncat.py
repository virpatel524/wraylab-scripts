import os 
import csv

categories = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/other/sample-population.txt'),delimiter='\t'))
genotype = list(csv.reader(open('/nfs/wraycompute/vir/5iter_allvariants_filtered.heteroremove.rareremove.noheteroconsid.geno'),delimiter='\t'))

genotype = map(list, zip(*genotype))

catdict = {}

for alpha in categories:
	catdict[alpha[0]] = alpha[1]

dict2 = {}

for alpha in genotype:
	if alpha[0] not in catdict:
		continue
	dict2.setdefault(catdict[alpha[0]], []).append(alpha)


for alpha in dict2:
	dict2[alpha] = [genotype[0], genotype[1]] + dict2[alpha]

for alpha in dict2:
	newfle = open('/nfs/wraycompute/vir/5iter_allvariants_filtered.heteroremove.rareremove.noheteroconsid.{}.geno'.format(alpha), 'w') 
	genotype = map(list, zip(*dict2[alpha]))
	chromes = []
	whobe = {}
	chromstuff = {}
	for alpha in genotype:
		chromes.append(alpha[0])
		chromstuff.setdefault(alpha[0], []).append(alpha)
	chromes = list(set(chromes))
	newchromdict = {}
	counter = 0
	newshit = []
	for alpha in sorted(chromes):
		if 'L' not in alpha[0][0]: continue
		counter += 1
		whobe[counter] = genotype[0]
		newchromdict[alpha] = str(counter)
		for beta in chromstuff[alpha]:
			beta[0] = str(counter)
			newshit.append(beta)
	newfle.write('\t'.join(genotype[0]) + '\n')
	for alpha in newshit:
		newfle.write('\t'.join(alpha) + '\n')
	newfle.close()
