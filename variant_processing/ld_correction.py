import os 
import csv
import sys

outputfle = open('/home/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/ld_keepers_chromcorrected.list','w')


for filename in os.listdir('/nfs/wraycompute/vir/variant_storage/ld_output'):
	holder = os.path.join('/nfs/wraycompute/vir/variant_storage/ld_output', filename)
	chro = filename.split('_')[0]
	data = list(csv.reader(open(holder),delimiter='\t'))[1:]

	for alpha in data:
		marker =  alpha[0].split(' ')[1]
		outputfle.write('{}:{}-{}\n'.format(chro[3:], marker, marker))

outputfle.close()



