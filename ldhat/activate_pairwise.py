import os
import sys
import csv
import subprocess

for alpha in os.listdir('/home/vdp5/projects/vivax_cambodia/data/ldhat/fasta_alignemnts/'):
	if 'reduced' in alpha:
		splitter = '/home/vdp5/projects/vivax_cambodia/data/ldhat/fasta_alignemnts/' + '.'.join(alpha.split('.')[:-4]) + '.'
		newstr = 'convert -seq {} -prefix {}'.format(os.path.join('/home/vdp5/projects/vivax_cambodia/data/ldhat/fasta_alignemnts/',alpha), splitter)
		print newstr
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()
		print 'two'

		newstr = 'pairwise -seq {} -loc {} -prefix {}'.format(splitter + 'sites.txt', splitter + 'locs.txt', splitter )
		print newstr
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

