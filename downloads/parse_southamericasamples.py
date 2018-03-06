import os 
import csv


data = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/other/hupalo_samples_data.txt'),delimiter='\t'))

starterdata = """#!/bin/bash
#SBATCH --job-name=launchstuff
#SBATCH --ntasks=1
#SBATCH --mem=6G
#SBATCH --mail-user=vdp5@duke.edu
#SBATCH --output=test.tmp
SCRATCH=/data/wraycompute/vdp5/scratch/$SLURM_JOB_ID
source /gpfs/fs0/home/vdp5/.bash_profile
cd /data/wraycompute/vdp5/random_gz"""


for alpha in data:
	newfle = open('/home/vdp5/projects/vivax_cambodia/data/script_create/dl_sa/{}_dlscript.sh'.format(alpha[0]),'w')
	newfle.write(starterdata + '\n')
	newfle.write('fastq-dump.2 --gzip --split-files {}\n'.format(alpha[2]))
	newfle.write('rename {} {} *'.format(alpha[2], alpha[0]))
	newfle.close()

