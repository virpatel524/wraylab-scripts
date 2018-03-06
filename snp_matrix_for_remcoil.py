import csv
import os
import argparse 



data = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/variant_files/intersect/dir/merged_274samp.tab'),delimiter='\t'))
samples = data[0]


samp2index = {}

counter  = 3
for alpha in samples[3:]:
	samp2index[alpha] = counter
	counter += 1

m = []
samps = sorted(samp2index.keys())
newmat = []

counter_alpha = 1
for alpha in samps:
	newmat.append('ind{}'.format(counter_alpha))
	counter_alpha += 1

m.append(['ind_name',] + samps)

counter = 1


finalfile = open('/home/vdp5/projects/vivax_cambodia/data/var_processing/5iter_6.6.17.txt', 'w')

counter_beta = 1
for alpha in data[1:]:
	zeep = alpha
	huzzah = []
	chrom = zeep[0]
	site = zeep[1]
	original = zeep[2]
	huzzah.append('site{}'.format(counter_beta))
	counter_beta += 1
	for samp in samps:
		var = zeep[samp2index[samp]]
		var = var.split('/')
		if var[0] == '.':
			huzzah.append('-1')
			continue
		if var[0] == original:
			if var[1] == original:
				huzzah.append('1')
				continue 
			else:
				huzzah.append('0.5')
				continue
		if var[0] != original:
			if var[0] == var[1]:
				huzzah.append('0')
			else:
				huzzah.append('0.5')
	m.append(huzzah)


rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

for alpha in rez:
	finalfile.write('{}\n'.format('\t'.join(alpha)))
finalfile.close()