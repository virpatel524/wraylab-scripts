pvp01="/home/vdp5/data/reference_genomes/PVP01.fasta"
pvc01="/home/vdp5/data/reference_genomes/PVC01.fasta"
pvt01="/home/vdp5/data/reference_genomes/PVT01.fasta"


fastq1="/home/vdp5/data/cambodia_samples/sequences_gz/OM270-BiooBarcode16_CCGTCC_R1.fastq.gz"
fastq2="/home/vdp5/data/cambodia_samples/sequences_gz/OM270-BiooBarcode16_CCGTCC_R2.fastq.gz"
finalout="/home/vdp5/projects/vivax_cambodia/data/testing_mapping_quality/"



# bwa mem ${pvp01} ${fastq1} ${fastq2} | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvp01_bwa &
# bwa mem ${pvc01} ${fastq1} ${fastq2} | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvc01_bwa &
# bwa mem ${pvt01} ${fastq1} ${fastq2} | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvt01_bwa &

# bowtie2 -x /home/vdp5/data/reference_genomes/PVP01 -1 ${fastq1} -2 ${fastq2} --dovetail | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvp01_bowtie_dovetail &
# bowtie2 -x /home/vdp5/data/reference_genomes/PVC01 -1 ${fastq1} -2 ${fastq2} --dovetail | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvc01_bowtie_dovetail &
# bowtie2 -x /home/vdp5/data/reference_genomes/PVT01 -1 ${fastq1} -2 ${fastq2} --dovetail | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvt01_bowtie_dovetail &

# bowtie2 -x /home/vdp5/data/reference_genomes/PVP01 -1 ${fastq1} -2 ${fastq2}  | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvp01_bowtie &
# bowtie2 -x /home/vdp5/data/reference_genomes/PVC01 -1 ${fastq1} -2 ${fastq2}  | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvc01_bowtie &
# bowtie2 -x /home/vdp5/data/reference_genomes/PVT01 -1 ${fastq1} -2 ${fastq2}  | samtools view  -Sb - | samtools sort - ${finalout}_OM270_pvt01_bowtie &

qualimap_bam ${finalout}OM270_pvp01_bwa.bam ${finalout} OM270_pvp01_bwa_qualimap.pdf &
qualimap_bam ${finalout}OM270_pvc01_bwa.bam ${finalout} OM270_pvc01_bwa_qualimap.pdf &
qualimap_bam ${finalout}OM270_pvt01_bwa.bam ${finalout} OM270_pvt01_bwa_qualimap.pdf &

qualimap_bam ${finalout}OM270_pvp01_bowtie_dovetail.bam ${finalout} OM270_pvp01_bowtie_dovetail_qualimap.pdf &
qualimap_bam ${finalout}OM270_pvc01_bowtie_dovetail.bam ${finalout} OM270_pvc01_bowtie_dovetail_qualimap.pdf &
qualimap_bam ${finalout}OM270_pvt01_bowtie_dovetail.bam ${finalout} OM270_pvt01_bowtie_dovetail_qualimap.pdf &

qualimap_bam ${finalout}OM270_pvp01_bowtie.bam ${finalout} OM270_pvp01_bowtie_qualimap.pdf &
qualimap_bam ${finalout}OM270_pvc01_bowtie.bam ${finalout} OM270_pvc01_bowtie_qualimap.pdf &
qualimap_bam ${finalout}OM270_pvt01_bowtie.bam ${finalout} OM270_pvt01_bowtie_qualimap.pdf &
