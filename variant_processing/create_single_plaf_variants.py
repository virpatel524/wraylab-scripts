import subprocess
import os 
import sys
import csv
import argparse

stem = '/nfs/wraycompute/vir/seperated_variantfiles/'

parser = argparse.ArgumentParser()
parser.add_argument('--stem', help="set that youll iterate through")
args = parser.parse_args()


for alpha in os.listdir('/nfs/wraycompute/vir/seperated_variantfiles/'):
	flename = os.path.join(stem, alpha)
	if args.stem not in flename: continue
	sampname = flename.split('/')[-1].split('_refined')[0]
	process = subprocess.Popen('java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -o /nfs/wraycompute/vir/seperated_variantfiles/{}_alone.vcf -R /home/vdp5/data/reference_genomes/PVP01.fasta -V /nfs/wraycompute/vir/seperated_variantfiles/{}_refined.vcf -sn {}'.format(sampname, sampname, sampname), shell=True, stdout=subprocess.PIPE)
	process.wait()
