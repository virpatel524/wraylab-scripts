import os
import csv
import argparse
import sys
import operator, math
import shutil
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--sample', help="what directory to search")

translate = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/extradata/numchrom_to_pvp01.txt'),delimiter='\t'))

transdict = {}

for alpha in translate:
	transdict[alpha[0]] = alpha[1]


args = parser.parse_args()

datatotal = []


for filename in os.listdir(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12', args.sample)):
	if 'norm' in filename:
		data = list(csv.reader(open(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12', args.sample, filename)),delimiter='\t'))[1:]
		chrom = filename.split('.')[-4]
		for it in data:
			datatotal.append([chrom, int(it[1]), abs(float(it[-2]))])


if not os.path.exists(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12',args.sample)):
	os.mkdir(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12',args.sample))


newfle = open(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12',args.sample, 'master.100bin.txt'), 'w')
pathtable = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12',args.sample, 'master.100bin.txt')
pathkeep = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12',args.sample, 'manhattan-plot-ihh12.pdf')

datatotal = sorted(datatotal, key=lambda x: x[2], reverse=True)

newfle.write('snp\tbp\tchrom\tpvalue\n')

for item in datatotal:
	print item
	newfle.write('{}\t{}\t{}\t{}\n'.format('{}_{}'.format(item[0], item[1]), item[1], transdict[item[0]], item[2]))

newfle.close()

newstr = 'Rscript /newhome/vdp5/projects/vivax_cambodia/scripts/poptests/ihh12/manhattan.R {} {}'.format(pathtable, pathkeep)
print newstr
process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
process.wait()