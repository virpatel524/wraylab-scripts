import os
import csv
import allel
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('white')
sns.set_style('ticks')
import bcolz
import pandas
import argparse
import h5py
import math


def plot_fst(ac1, ac2, pos, chrom, blen=1):
		
		fst, se, vb, _ = allel.stats.blockwise_hudson_fst(ac1, ac2, blen=blen)
		
		# use the per-block average Fst as the Y coordinate
		y = vb
		



		# use the block centres as the X coordinate
		x = allel.stats.moving_statistic(pos, statistic=lambda v: (v[0] + v[-1]) / 2, size=blen)
		print chrom, len(x), len(y)

		for i in xrange(len(x)):
			if float(y[i]) < 0: continue
			if math.isnan(y[i]) : continue
			totset.append(['{}_{}'.format(chrom, str(x[i])), str(x[i]), chrom2num[chrom], str(y[i])])

		print len(totset)



parser = argparse.ArgumentParser()
parser.add_argument('--vcfdir', help="VCF file for use")
parser.add_argument('--popfile', help="Populations for use")
args = parser.parse_args()



chomconvraw = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/extradata/numchrom_to_pvp01.txt'),delimiter='\t'))

chrom2num = {}

for item in chomconvraw:
	chrom2num[item[0]] = item[1]




chromlist = list(csv.reader(open('/newhome/vdp5/data/reference_genomes/PVP01.chromosomes'),delimiter='\t'))

properlst = [a[0] for a in chromlist if 'LT' in a[0] and '26' not in a[0] and '27' not in a[0]]


totset = []


for chromname in properlst:
	vcfname = '/nfs/wraycompute/vir/variant_storage/master/split/regular/5iter_allvariants_filtered.rareremove.deploidcorrected.notrelevantremoved.nopirvirvariants.ann.{}.vcf'.format(chromname)
	callset = allel.read_vcf(vcfname)

	allel.vcf_to_hdf5(vcfname, vcfname + '.h5',fields='*', overwrite=True)

	callset = h5py.File(vcfname + '.h5', mode='r')


	df_samples = pandas.read_csv(args.popfile, sep='\t', names=['sample', 'country', 'population'])
	pos_all = allel.SortedIndex(callset['variants']['POS'])
	genotype_all = allel.GenotypeChunkedArray(callset['calldata']['GT'])
	subset = []


	pop2 = 'CV'
	pop1 = 'MT'
	pop3 = 'MP'


	subpops = {
			pop1: df_samples[df_samples.population == pop1].index,
			pop2: df_samples[df_samples.population == pop2].index,
			pop3: df_samples[df_samples.population == pop3].index,

	}

	acs = genotype_all.count_alleles_subpops(subpops)

	acu = allel.AlleleCountsArray(acs[pop1][:] + acs[pop2][:])
	flt = (acu.max_allele() == 1)
	pos = pos_all.compress(flt)
	ac1 = allel.AlleleCountsArray(acs[pop1].compress(flt, axis=0)[:, :2])
	ac2 = allel.AlleleCountsArray(acs[pop2].compress(flt, axis=0)[:, :2])
	# ac3 = allel.AlleleCountsArray(acs[pop3].compress(flt, axis=0)[:, :2])
	genotype = genotype_all.compress(flt, axis=0)

	plot_fst(ac1, ac2, pos, chromname)

print len(totset)

newfle = open('/home/vdp5/projects/vivax_cambodia/data/poptests/fst/MT-CV_hudsonfst.txt', 'w')

newfle.write('snp\tbp\tchrom\tFST\n')


for item in totset:
	newfle.write('{}\n'.format('\t'.join(item)))

newfle.close()


newfle = open('/home/vdp5/projects/vivax_cambodia/data/poptests/fst/MT-CV_hudsonfst_topset.txt', 'w')


percentile  = int(float(len(totset)) * 0.001) + 1


for beta in totset:
	beta[-1] = float(beta[-1])


totset = sorted(totset, key=lambda x: x[-1], reverse=True)


print len(totset)

wanted = totset[:percentile]


for item in wanted:
	tmp = item
	tmp[-1] = str(tmp[-1])
	newfle.write('{}\n'.format(tmp[0]))

newfle.close()