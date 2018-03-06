#!/data/wraycompute/vdp5/bin/bin/python2.7
#
#SBATCH --job-name=test
#SBATCH --ntasks=1
#SBATCH --mem=8G

# testing stuff

import vcf
import os
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sampname', help="sample name")
args = parser.parse_args()



newvcf = []
sampname = args.sampname

vcf_reader = list(csv.reader(open('/home/vdp5/data/variant_staging/indiv_samples_deploid/{}_alone.vcf'.format(sampname)),delimiter='\t'))

hapkey = list(csv.reader(open('/home/vdp5/data/variant_associated_data/MOI1_11.4.17_withindexhap.txt'),delimiter='\t'))
newflevcf = open('/home/vdp5/data/variant_staging/indiv_samples_deploid/{}_alone.modded.vcf'.format(sampname), 'w')



indexofhap = 0 

for alpha in hapkey:
	if alpha[0] == sampname:
		indexofhap = int(alpha[1]) + 2

haplotypes = list(csv.reader(open('/home/vdp5/data/variant_staging/deploid/hapfiles/{}.hap'.format(sampname)),delimiter='\t'))

haplotypes = map(list, zip(*haplotypes))
haplotypes = [haplotypes[0], haplotypes[1], haplotypes[indexofhap]]
haplotypes = map(list, zip(*haplotypes))

happa = 0

masterdicthaplotype = {}

for index, alpha in enumerate(haplotypes):
	print index, len(haplotypes)
	if alpha[0] not in haplotypes:
		newdict = {}
		newdict[alpha[1]] = alpha[2]
		masterdicthaplotype[alpha[0]] = newdict
	else:
		masterdicthaplotype[alpha[0]][alpha[1]] = alpha[2]





for alpha in vcf_reader:
	if alpha[:2] == '##':
		newflevcf.write('\t'.join(alpha) + '\n')
		continue
	stringmanip = alpha[-1]
	if stringmanip[:3] == '0/1':
		newstr = masterdicthaplotype[alpha[0]][alpha[1]]
		newstr = '{}/{}'.format(newstr)
		stringmanip[:3] = newstr
		ad = stringmanip.split(':')[1].split(',')
		dp = float(stringmanip.split(':')[2])
		ad = [int(a) for a in ad]
		dp = int(dp)

		if masterdicthaplotype[alpha[0]][alpha[1]] == 0:
			newad = '{},{}'.format(ad[0], 0)
			newdp = str(ad[0])

		if masterdicthaplotype[alpha[0]][alpha[1]] == 1:
			newad = '{},{}'.format(0, ad[1])
			newdp = str(ad[1])


		broken = stringmanip.split(':')
		broken[1] = newad
		broken[2] = newdp
		fixed = ':'.join(broken)
		alpha[-1] = fixed
		newflevcf.write('\t'.join(alpha) + '\n')
		continue

	else:
		newflevcf.write('\t'.join(alpha) + '\n')



