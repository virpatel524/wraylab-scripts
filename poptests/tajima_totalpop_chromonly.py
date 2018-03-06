import csv
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--tajima')
args = vars(parser.parse_args())
print args


data = list(csv.reader(open(args['tajima']),delimiter='\t'))



dictforchrom = {}
placehodlerdict = {}
chrom = ''

for alpha in data[1:]:
	if alpha[0] != chrom:
		newlst = []
		if chrom != '':
			for beta in placehodlerdict:
				tmp = [float(a) for a in placehodlerdict[beta]]
				meanie = np.mean(tmp)
				newlst.append([beta, meanie])
			dictforchrom[chrom] = newlst
		placehodlerdict = {}
		chrom = alpha[0]
		placehodlerdict.setdefault(alpha[1], []).append(alpha[-1])
	else:
		placehodlerdict.setdefault(alpha[1], []).append(alpha[-1])


for alpha in dictforchrom:
	da = dictforchrom[alpha]
	da.sort(key=lambda x: x[0])
	nested1 = []
	nested2 = []

	for beta in da:
		nested1.append(float(beta[0]))
		nested2.append(float(beta[1]))

	plt.scatter(nested1, nested2)

	plt.xlabel('Chromosome Site')
	plt.ylabel('Tajima D')

	plt.title('{}'.format(alpha))

	plt.savefig('/home/vdp5/projects/vivax_cambodia/data/poptests/figures_tajima/{}_tajima.pdf'.format(alpha))
	plt.close()


