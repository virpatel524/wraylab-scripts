import csv
import os 
import sys 

data = list(csv.reader(open('../data/other/new_sample_sra.txt'),delimiter='\t'))

newfle = open('download_remaining_samples.sh', 'w')
rename = open('rename_remaining_samples.sh', 'w')
for alpha in data:
	counter = 1
	for theta in alpha[1:]:
		newfle.write('fastq-dump.2.8.0 --split-3 -gzip {}\n'.format(theta))
		rename.write('rename {} {}_{} *\n'.format(theta, alpha[0], counter))
		counter += 1
newfle.close()
rename.close()