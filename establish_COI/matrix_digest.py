#gives list of double multiplicity infections based on a matrix of genotypes. 
# see wiki for protocol. 


import csv 
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

data = list(csv.reader(open('/home/vdp5/projects/vivax_cambodia/data/var_processing/5iter_6.6.17.txt'),delimiter='\t'))
data = data[1:]


badlst = open('/home/vdp5/projects/vivax_cambodia/data/var_processing/multiplicity_clear.txt', 'w')


count1 = 0
count2 = 0

matrix_percentages = []

for alpha in data:
	counter_all = 0
	counter_hetero = 0
	counter_zeros = 0
	for zeta in alpha[1:]:
		if zeta == '-1':
			counter_zeros += 1
			counter_all += 1
		if zeta == '1' or zeta == '0':
			counter_all += 1
			continue
		if zeta == '0.5':
			counter_all += 1
			counter_hetero += 1

	het = float(counter_hetero) / float(counter_all)
	no = float(counter_zeros) / float(counter_all)
	if counter_hetero < 12500:
		matrix_percentages.append(counter_hetero)
		count1 += 1
	else:
		badlst.write('{}\n'.format(alpha[0]))
		count2 += 1


data = sorted(matrix_percentages)
zeta = range(1, len(data) + 1)


plt.plot(zeta, data)
plt.ylabel('Quantity')
plt.xlabel(' Heterozygotes out of Total Variant Calls')
plt.title('Heterozygote Variant Calls in Vivax Samples Examined')
plt.xlim([0, len(zeta) + 1])
plt.savefig('/home/vdp5/projects/vivax_cambodia/data/figures/samples_heterozygous_nums.pdf')



