#!/bin/bash
#SBATCH --job-name=test
#SBATCH --ntasks=1
#SBATCH --mem=16G
#SBATCH --mail-user=vdp5@duke.edu
#SBATCH -o  /home/vdp5/slurm_out/OM208_bwa.script.out
SCRATCH=/gpfs/fs0/data/wraycompute/vdp5/scratch/$SLURM_JOB_ID
mkdir -p $SCRATCH


module load bwa 
module load samtools

srun bwa mem -M -t 4 -v 2 -A 2 -L 15 -U 9 -T 75 -k 19 -w 100 -d 100 -r 1.5 -c 10000 -B 4 -O 6 -E 1 /gpfs/fs0/data/wraycompute/vdp5/reference_data/PVP01.fasta /gpfs/fs0/data/wraycompute/vdp5/rest_samples_gz/OM208_1.fastq.gz /gpfs/fs0/data/wraycompute/vdp5/rest_samples_gz/OM208_2.fastq.gz | samtools view  -Sb - | samtools sort - -o /gpfs/fs0/data/wraycompute/vdp5/mapped/OM208.sorted.bam
sbatch -o /home/vdp5/slurm_out/OM208.script.out /home/vdp5/slurm_scripts/nyu_gatk_pipeline.sh /gpfs/fs0/data/wraycompute/vdp5/bin/picard.jar /gpfs/fs0/data/wraycompute/vdp5/bin/GenomeAnalysisTK.jar /gpfs/fs0/data/wraycompute/vdp5/reference_data/PVP01.fasta /gpfs/fs0/data/wraycompute/vdp5/mapped/OM208.sorted.bam

rm -rf $SCRATCH
