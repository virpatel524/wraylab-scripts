## functions 

ref="/home/vdp5/data/reference_genomes/PVP01.fasta"



function AddOrReplaceReadGroups ()
{
	java -jar /home/vdp5/source_code/picard.jar AddOrReplaceReadGroups INPUT=$1 OUTPUT=readgroups.bam RGID=1 RGLB=bb016 RGPL=illumina RGPU=unit1 RGSM=bb016

}
# function CollectInsertSizeMetrics ()
# {
# 	java -jar /home/vdp5/source_code/picard.jar CollectInsertSizeMetrics INPUT=$1 OUTPUT=insert_metrics.txt HISTOGRAM_FILE=insert_size_histogram.pdf
# }

function MarkDuplicates ()
{

	java -jar /home/vdp5/source_code/picard.jar MarkDuplicates INPUT=readgroups.bam OUTPUT=dedup_reads.bam METRICS_FILE=metrics.txt
}

function BuildBamIndex ()
{
	java -jar /home/vdp5/source_code/picard.jar BuildBamIndex INPUT=dedup_reads.bam
}

function RealignerTargetCreator ()
{

	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T RealignerTargetCreator -R /home/vdp5/data/reference_genomes/PVP01.fasta -I dedup_reads.bam -o realignment_targets.list

}


function IndelRealigner ()
{
java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T IndelRealigner -R $ref -I dedup_reads.bam -targetIntervals realignment_targets.list -o realigned_reads.bam

}

function HaplotypeCaller ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T HaplotypeCaller -R $ref -I realigned_reads.bam -nct 30 -o raw_variants.vcf

}

function SelectVariants ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R $ref -V raw_variants.vcf -selectType SNP -o raw_snps.vcf
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R $ref -V raw_variants.vcf -selectType INDEL -o raw_indels.vcf



}


function VariantFiltration ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T VariantFiltration -R $ref -V raw_snps.vcf --filterExpression 'QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0 || SOR > 4.0' --filterName "basic_snp_filter" -o filtered_snps.vcf
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T VariantFiltration -R $ref -V raw_indels.vcf --filterExpression 'QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0 || SOR > 10.0' --filterName "basic_indel_filter" -o filtered_indels.vcf


}

function BaseRecalibrator ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T BaseRecalibrator -R $ref -I realigned_reads.bam -knownSites filtered_snps.vcf -knownSites filtered_indels.vcf -o recal_data.table
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T BaseRecalibrator -R $ref -I realigned_reads.bam -knownSites filtered_snps.vcf -knownSites filtered_indels.vcf -BQSR recal_data.table -o post_recal_data.table

}

function AnalyzeCovariates ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T AnalyzeCovariates -R $ref -before recal_data.table -after post_recal_data.table -plots recalibration_plots.pdf

}

# function PrintReads ()
# {
# 	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T PrintReads -R $ref -I realigned_reads.bam -BQSR recal_data.table -o recal_reads.bam

# }

function HaplotypeCaller2 ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T HaplotypeCaller -R $ref -nct 30 -I recal_reads.bam -o raw_variants_recal.vcf

}

function SelectVariants2 ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R $ref -V raw_variants_recal.vcf -selectType SNP -o raw_snps_recal.vcf
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R $ref -V raw_variants_recal.vcf -selectType INDEL -o raw_indels_recal.vcf



}

function VariantFiltration2 ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T VariantFiltration -R $ref -V raw_snps_recal.vcf --filterExpression 'QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0 || SOR > 4.0' --filterName "basic_snp_filter" -o filtered_snps_final.vcf
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T VariantFiltration -R $ref -V raw_indels_recal.vcf --filterExpression 'QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0 || SOR > 10.0' --filterName "basic_indel_filter" -o filtered_indels_recal.vcf

}





base=$(basename $1)
touch /home/vdp5/projects/vivax_cambodia/logs/nyu_run.log_${base}
logfle=/home/vdp5/projects/vivax_cambodia/logs/nyu_run.log_${base}
cd /home/vdp5/projects/vivax_cambodia/data/nyu_pipeline_results
mkdir $base
cd $base
CollectInsertSizeMetrics $1
echo "CollectInsertSizeMetrics" >> $logfle
AddOrReplaceReadGroups $1
echo "AddOrReplaceReadGroups" >> $logfle
MarkDuplicates
echo "MarkDuplicates" >> $logfle
BuildBamIndex
echo "BuildBamIndex" >> $logfle
RealignerTargetCreator
echo "RealignerTargetCreator" >> $logfle
IndelRealigner
echo "IndelRealigner" >> $logfle
HaplotypeCaller
echo "HaplotypeCaller" >> $logfle
SelectVariants
echo "SelectVariants" >> $logfle
VariantFiltration
echo "VariantFiltration" >> $logfle
BaseRecalibrator
echo "BaseRecalibrator" >> $logfle
AnalyzeCovariates
echo "AnalyzeCovariates" >> $logfle
PrintReads
echo "PrintReads" >> $logfle
HaplotypeCaller2
echo "HaplotypeCaller2" >> $logfle
SelectVariants2
echo "SelectVariants2" >> $logfle
VariantFiltration2
echo "VariantFiltration2" >> $logfle
