# 10/25/17 | 4:54 PM
# Seems as though the sample names that were included in our BAM files accidentally featured sorted.bam in their file names, which is an issue since the population files do not feature the .sorted.bam designation
# So hopefully this script corrects those regions

import csv
import os

txt = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/other/freebayes_10.19.17.txt'),delimiter='\t'))

newset = []

for alpha in txt:
	newset.append([alpha[0] + '.sorted.bam', alpha[1]])


newfle = open('/newhome/vdp5/projects/vivax_cambodia/data/other/freebayes_10.19.17.txt', 'w')

for alpha in newset:
	newfle.write('{}\t{}\n'.format(alpha[0], alpha[1]))


newfle.close()