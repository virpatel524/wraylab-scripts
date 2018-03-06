import csv 
import os

onlyfiles = [os.path.join('/home/vdp5/projects/vivax_cambodia/data/alternate_reference', f) for f in os.listdir('/home/vdp5/projects/vivax_cambodia/data/alternate_reference')]
totalmatrix = []
for alpha in onlyfiles:
	data = list(csv.reader(open(alpha),delimiter='\t'))
	for zeta in data:
		if '>' in zeta[0]:
			sample = alpha.split('/')[-1].split('_')[0]
			totalmatrix.append('>{}_{}'.format(sample, 'LT635625'))
		else:
			totalmatrix.append(zeta[0])


newfle = open('/home/vdp5/projects/vivax_cambodia/data/alternate_reference/allcambodia_samples_LT635625', 'w')
for alpha in totalmatrix:
	newfle.write('{}\n'.format(alpha))

newfle.close()