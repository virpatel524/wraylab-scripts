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
import allel
import argparse
import h5py


def plot_fst(ac1, ac2, pos, outputtitle, miniput, blen=100):
    
    fst, se, vb, _ = allel.stats.blockwise_hudson_fst(ac1, ac2, blen=blen)
    
    # use the per-block average Fst as the Y coordinate
    y = vb
    

    print y

    # use the block centres as the X coordinate
    x = allel.stats.moving_statistic(pos, statistic=lambda v: (v[0] + v[-1]) / 2, size=blen)
    
    # plot
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.despine(ax=ax, offset=5)
    ax.plot(x, y, 'k-', lw=.5)
    ax.set_ylabel('$F_{ST}$')
    ax.set_xlabel('Chromosome %s position (bp)' % args.chromname)
    ax.set_xlim(0, pos.max())
    plt.savefig('/newhome/vdp5/projects/vivax_cambodia/data/figures/fst/{}.{}.pdf'.format(outputtitle,miniput),bbox_inches='tight')
    


parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for use")
parser.add_argument('--popfile', help="Populations for use")
parser.add_argument('--figname', help="Title output")
parser.add_argument('--chromname', help='Chromosome name')

args = parser.parse_args()


chromlist = list(csv.reader(open('/newhome/vdp5/data/reference_genomes/PVP01.chromosomes'),delimiter='\t'))

newlst = [a[0] for a in chromlist if 'LT' in a[0]] 
callset = allel.read_vcf(args.vcffile)

allel.vcf_to_hdf5(args.vcffile, args.vcffile + '.h5',fields='*', overwrite=True)

callset = h5py.File(args.vcffile + '.h5', mode='r')


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
ac3 = allel.AlleleCountsArray(acs[pop3].compress(flt, axis=0)[:, :2])
genotype = genotype_all.compress(flt, axis=0)



plot_fst(ac1, ac2, pos, args.figname, '{}-{}'.format(pop1, pop2))
plot_fst(ac1, ac3, pos, args.figname, '{}-{}'.format(pop1, pop3))
plot_fst(ac2, ac3, pos, args.figname, '{}-{}'.format(pop2, pop3))
