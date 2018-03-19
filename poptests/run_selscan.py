import os
import csv
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mapdir', help="Directory for play")
parser.add_argument('--vcfdir', help="Directory for play")
parser.add_argument('--popname', help="Directory for play")


args = parser.parse_args()

if not os.path.exists(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihs', args.popname)):
	os.makedirs(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihs', args.popname))

if not os.path.exists(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/pi', args.popname)):
	os.makedirs(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/pi', args.popname))

if not os.path.exists(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12', args.popname)):
	os.makedirs(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12', args.popname))

if not os.path.exists(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl', args.popname)):
	os.makedirs(os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl', args.popname))



for alpha in os.listdir('{}'.format(args.mapdir)):
	if '.map' in alpha:
		splitter = os.path.join(args.mapdir, '.'.join(alpha.split('.')[:-1]) + '.')
		splitter_ihs = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihs', args.popname, '.'.join(alpha.split('.')[:-1]))
		splitter_ehh = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ehh', args.popname, '.'.join(alpha.split('.')[:-1]))
		splitter_pi = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/pi', args.popname, '.'.join(alpha.split('.')[:-1]))
		splitter_ihh12 = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12', args.popname, '.'.join(alpha.split('.')[:-1]))
		splitter_xpehh = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/xp-ehh', args.popname, '.'.join(alpha.split('.')[:-1]))
		splitter_nsl = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl', args.popname, '.'.join(alpha.split('.')[:-1]))

		chrom = splitter.split('.')[-3]
		vcfstor = args.vcfdir
		vcfwewant = ''
		for beta in os.listdir(vcfstor):
			if chrom in beta and beta[-2:] == 'gz':
				vcfwewant = os.path.join(vcfstor, beta)

		newstr = 'selscan --threads 8 --ihs --map {} --vcf {} --out {} '.format(os.path.join(args.mapdir, alpha), vcfwewant, splitter_ihs)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

		newstr = 'selscan --threads 8 --nsl  --vcf {} --out {} '.format(vcfwewant, splitter_nsl)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()


		# newstr = 'selscan --threads 8 --pi --map {} --vcf {} --out {} '.format(os.path.join(args.mapdir, alpha), vcfwewant, splitter_pi)
		# process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		# process.wait()

		newstr = 'selscan --threads 8 --ihh12 --map {} --vcf {} --out {} '.format(os.path.join(args.mapdir, alpha), vcfwewant, splitter_ihh12)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

		splitter = os.path.join(args.mapdir, '.'.join(alpha.split('.')[:-1]) + '.')
		splitter_ihs = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihs', args.popname)
		splitter_ehh = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ehh', args.popname)
		splitter_pi = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/pi', args.popname)
		splitter_ihh12 = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12', args.popname)
		splitter_xpehh = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/xp-ehh', args.popname)
		splitter_nsl = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/nsl', args.popname)

print splitter_ihh12

newstr = 'norm --ihh12 --files {}/*out '.format(splitter_ihh12)
process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
process.wait()

newstr = 'norm --ihs --files {}/*out '.format(splitter_ihs)
process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
process.wait()

newstr = 'norm --nsl --files {}/*out '.format(splitter_nsl)
process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
process.wait()