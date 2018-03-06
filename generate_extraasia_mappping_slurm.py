import csv

vir = """#!/bin/bash
#SBATCH --job-name=test
#SBATCH --ntasks=1
#SBATCH --mem=16G
#SBATCH --mail-user=vdp5@duke.edu
#SBATCH -o  /home/vdp5/slurm_out/{}_bwa.script.out
SCRATCH=/gpfs/fs0/data/wraycompute/vdp5/scratch/$SLURM_JOB_ID
mkdir -p $SCRATCH


module load bwa 
module load samtools

srun bwa mem -M -t 4 -v 2 -A 2 -L 15 -U 9 -T 75 -k 19 -w 100 -d 100 -r 1.5 -c 10000 -B 4 -O 6 -E 1 {} {} {} | samtools view  -Sb - | samtools sort - -o {}.bam
sbatch -o /home/vdp5/slurm_out/{}.script.out /home/vdp5/slurm_scripts/nyu_gatk_pipeline.sh /gpfs/fs0/data/wraycompute/vdp5/bin/picard.jar /gpfs/fs0/data/wraycompute/vdp5/bin/GenomeAnalysisTK.jar /gpfs/fs0/data/wraycompute/vdp5/reference_data/PVP01.fasta {}

rm -rf $SCRATCH
"""

fle = list(csv.reader(open('/nfs/wraycompute/vir/allsamps.txt'),delimiter='\t'))

for file in fle:
	zeta = file[0]
	base = zeta[:-2]
	output = '/gpfs/fs0/data/wraycompute/vdp5/mapped/{}.sorted'.format(base)
	newfle = open('mapping_scripts/{}_map_script_slurm.sh'.format(base), 'w')
	newfle.write(vir.format(base, '/gpfs/fs0/data/wraycompute/vdp5/reference_data/PVP01.fasta', '/gpfs/fs0/data/wraycompute/vdp5/rest_samples_gz/{}_1.fastq.gz'.format(base), '/gpfs/fs0/data/wraycompute/vdp5/rest_samples_gz/{}_2.fastq.gz'.format(base), output, base, output + '.bam'))

