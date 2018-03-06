import csv

vir = """
#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --ntasks=1
#SBATCH --mem=51700K
#SBATCH --mail-user=vdp5@duke.edu
SCRATCH=/data/wraycompute/vdp5/scratch/$SLURM_JOB_ID
bwa mem {} {} {} -M  -v 2 -A 2 -L 15 -U 9 -T 75 -k 19 -w 100 -d 100 -r 1.5 -c 10000 -B 4 -O 6 -E 1 | samtools view  -Sb - | samtools sort - {} 

rm -rf $SCRATCH
"""

fle = list(csv.reader(open('/nfs/wraycompute/vir/hi/restfiles.txt'),delimiter='\t'))

for file in fle:
	zeta = file[0].split('.')
	if zeta[1] != 'txt':
		zeta = zeta[0]
		base = zeta[:-2]
		output = '/data/wraycompute/vdp5/mapped/{}.sorted'.format(base)
		newfle = open('mapping_scripts/{}_map_script_slurm.sh'.format(base), 'w')
		newfle.write(vir.format('/gpfs/fs0/data/wraycompute/vdp5/reference_data/PVP01.fasta', '/gpfs/fs0/data/wraycompute/vdp5/rest_samples_gz/{}_1.tar.gz'.format(base), '/data/wraycompute/vdp5/rest_samples_gz/{}_2_tar.gz'.format(base), output))

