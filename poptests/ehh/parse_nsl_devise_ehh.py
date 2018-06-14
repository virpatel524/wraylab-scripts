import os
import sys
import csv
import argparse
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('--mapdir', help="Map dir")
parser.add_argument('--flensl', help="NSL file")
parser.add_argument('--outname', help="Name of output")


args = parser.parse_args()

data = list(csv.reader(open(args.flensl),delimiter='\t'))

newset = []


for beta in data:
	chrom = beta[1]
	newset.append([chrom, beta[2] , float(beta[-1])])



newset.sort(key=lambda x: x[2], reverse=True)


num = int(len(newset) * 0.01)
topnum = int(len(newset) * 0.001) 


firsttopset = newset[:num + 1]
sectopset = newset[:topnum + 1]



numset = []
topnumset = []

for beta in firsttopset:
	chrom = beta[0]
	for alpha in os.listdir(args.mapdir):
		if chrom in alpha:
			mapnombre = os.path.join(args.mapdir, alpha)
			mapdata = list(csv.reader(open(os.path.join(args.mapdir, alpha)),delimiter='\t'))
			for theta in mapdata:
				zoobi = theta[0].split(' ')
				if beta[1] == zoobi[-1]:
					loc = zoobi[1]

	for alpha in os.listdir('/nfs/wraycompute/vir/variant_storage/bychrom/vcf/phased/reg/'):
		if chrom in alpha:
			vcfnombre = os.path.join('/nfs/wraycompute/vir/variant_storage/bychrom/vcf/phased/reg/', alpha)
	numset.append([chrom, loc, beta[1], mapnombre, vcfnombre])






newfle = open(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ehh/dictionary_translate/{}.txt'.format(args.outname)), 'w')


for beta in numset:
	newfle.write('{}\t{}\t{}\n'.format(beta[0], beta[1], beta[2]))

newfle.close()

try: 
	shutil.rmtree('/home/vdp5/projects/vivax_cambodia/data/poptests/ehh/ehh_output/{}'.format(args.outname))
except:
	x = 5

os.mkdir('/home/vdp5/projects/vivax_cambodia/data/poptests/ehh/ehh_output/{}'.format(args.outname))


newfle = open('/home/vdp5/projects/vivax_cambodia/data/poptests/ehh/scripts-ehh/{}.sh'.format(args.outname), 'w')

for beta in numset:
	newfle.write('selscan --keep-low-freq --trunc-ok --map {} --vcf {} --ehh {} --out /home/vdp5/projects/vivax_cambodia/data/poptests/ehh/ehh_output/{}/{}_{}\n'.format(beta[3], beta[4], beta[1], args.outname, beta[0], beta[2]))

newfle.close()

