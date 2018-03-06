import os
import csv
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for input")
parser.add_argument('--outvcf', help="output name of vcf")
args = parser.parse_args()

dataset = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/extradata/numchrom_to_pvp01.txt'),delimiter='\t'))


normie2num = {}

for beta in dataset:
	normie2num[beta[0]] = beta[1]

keepmein = ''

for beta in normie2num:
	keepmein += '-L {} '.format(beta)


newstr = 'java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -V {} -R $PVP01REF -o /newhome/vdp5/tmp/holdemvariants.vcf {}'.format(args.vcffile, keepmein)
process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
process.wait()

newvcf = open('{}'.format(args.outvcf), 'w')

readstuff = list(csv.reader(open('/newhome/vdp5/tmp/holdemvariants.vcf'),delimiter='\t'))

for beta in readstuff:
	holdittogether = '\t'.join(beta)
	for alpha in normie2num:
		holdittogether =  holdittogether.replace(alpha, normie2num[alpha])
	newvcf.write(holdittogether + '\n')

newvcf.close()

newstr = 'rm -rf /newhome/vdp5/tmp/holdemvariants.vcf'.format(args.outvcf)
process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
process.wait()

