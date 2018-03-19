import os
import sys
import csv
import argparse
import operator


parser = argparse.ArgumentParser()
parser.add_argument('--nslfile', help="VCF file for use")
parser.add_argument('--ihsfile', help="VCF file for use")
args = parser.parse_args()


ihsnsl_concord = {}


nsldata = list(csv.reader(open(args.nslfile),delimiter='\t'))
ihsdata = list(csv.reader(open(args.ihsfile),delimiter='\t'))


ihsdict = {}

for beta in ihsdata[1:]:
	chrom = beta[0].split('_')[0]
	locus = beta[0].split('_')[-1]
	ihsdict.setdefault(chrom, []).append([int(locus), float(beta[-1])])

mergeddictihs = {}

nsldict = {}
nsltots = []

for beta in nsldata[1:]:
	chrom = beta[0].split('_')[0]
	locus = beta[0].split('_')[-1]
	nsldict.setdefault(chrom, []).append([int(locus), float(beta[-1])])
	nsltots.append(['{}_{}'.format(chrom, locus), float(beta[-1])])


ihstots = []

for beta in ihsdict:
	ihsdict[beta ] = sorted(ihsdict[beta], key=lambda x: x[0])
	dathold = ihsdict[beta]
	masternewdict = {}
	for i in range(0,len(dathold) - 1):
		masternewdict['{}-{}'.format(dathold[i][0], dathold[i + 1][0])] = dathold[i][1] + dathold[i + 1][1]/2.0
		newset = ['{}:{}-{}'.format(beta,dathold[i][0], dathold[i + 1][0]) , dathold[i][1] + dathold[i + 1][1]/2.0]
		ihstots.append(newset)

	mergeddictihs[beta] = masternewdict


nsltots = sorted(nsltots, key=lambda x: x[1], reverse=True)
ihstots = sorted(ihstots, key=lambda x: x[1], reverse=True)

top1percentile_nsl = int(float(len(nsltots)) * 0.02)
top1percentile_ihs = int(float(len(ihstots)) * 0.02)

nsl_top = nsltots[:top1percentile_nsl]
ihs_top = ihstots[:top1percentile_ihs]


print nsl_top

topnsl_loci = [a[0] for a in nsl_top]
topihs_loci = [a[0] for a in ihs_top]




counter = 0 



for beta in nsldict:
	nslvals = nsldict[beta]
	ihsvals = mergeddictihs[beta]
	for nsl in nslvals:
		for kirko in ihsvals:
			ihsbot = int(kirko.split('-')[0])
			ihstop = int(kirko.split('-')[1])
			if nsl[0] > ihsbot and nsl[0] < ihstop:
				val = '{}_{}'.format(beta, nsl[0])
				relformat_ihs = '{}:{}'.format(beta, kirko)
				if val in topnsl_loci and ihsvals[kirko] > 2:
					print 'help me god'
				ihsnsl_concord['{}_{}'.format(beta, nsl[0])] = [nsl[1], ihsvals[kirko]]
				



