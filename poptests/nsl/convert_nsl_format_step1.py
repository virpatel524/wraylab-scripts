import os
import csv
import argparse
import sys
import vcf


parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="vcf file to parse")
parser.add_argument('--sample', help='sample name')
args = parser.parse_args()


holdem="""---
pop: All
build: PVP01
hapmap_release: lol
start:
stop:
snps:
"""


samples = []


vcf_reader = vcf.Reader(open(args.vcffile, 'r'))
chromdata = {}

for record in vcf_reader:
	if 'FLZR' in record.CHROM:
		continue
	chromdata.setdefault(record.CHROM, []).append(record)
	if len(samples) == 0:
		for sam in record.samples:
			samples.append(sam.sample)
			
if not os.path.isdir('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl/input/{}'.format(args.sample)):
	os.mkdir('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl/input/{}'.format(args.sample))


for chrom in chromdata:
	newfle = open('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl/input/chr{}_samples.txt'.format(chrom))
	for beta in samples:
		newfle.write(beta + '\n')
	newfle.close()

	setofall = []
	strbig = {}

	newfle = open('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl/input/chr{}_ansder.txt'.format(chrom))
	counter = 0
	for beta in chromdata[chrom]:
		for call in beta.samples:
			if call.sample not in strbig:
				strbig[call.sample] = call.gt_bases[0]
			else:
				strbig[call.sample] = strbig[call.sample] + call.gt_bases[0]

		counter += 1
		newfle.write('rs{}\t{}\t{}\n'.format(counter, beta.REF, beta.ALT))
		setofall.append(['rs{}'.format(counter), chrom.POS])
		newfle.close()

	newfle = open('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl/input/chr{}_haplotype.txt'.format(chrom))
	newfle.write(holdem)
	for it in setofall:
		newfle.write('  - {}: {}\n'.format(it[0], it[1]))
	newfle.write('phased_haplotypes:\n')

	for sinca in sorted(samples):
		newfle.write('  - {}: {}\n'.format(sinca, strbig[sinca]))

	newfle.close()













