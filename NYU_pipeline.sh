## functions 

function emailme()
{
	echo $1 > /home/vdp5/other/mailscripts/mailmessage.txt
	sendmail virpatel3@gmail.com < /home/vdp5/other/mailscripts/mailmessage.txt
}

ref="/home/vdp5/data/reference_genomes/PVP01.fasta"


function disbgzip()
{
    for alpha in $1/*final_variants*.vcf; do
        bgzip $alpha
    done
}

function distabix()
{
    for alpha in $1/*final_variants*.vcf.gz; do
        tabix -p vcf $alpha
    done
}


function AddOrReplaceReadGroups ()
{
	java -jar /home/vdp5/source_code/picard.jar AddOrReplaceReadGroups INPUT=$1 OUTPUT=readgroups.bam RGID=1 RGLB=$base RGPL=illumina RGPU=unit1 RGSM=$base

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
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T HaplotypeCaller  -R $ref -I realigned_reads.bam -o raw_variants.vcf

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

function PrintReads ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T PrintReads -R $ref -I realigned_reads.bam -BQSR recal_data.table -o recal_reads.bam

}

function HaplotypeCaller2 ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T HaplotypeCaller  -R $ref -I recal_reads.bam -o raw_variants_recal.vcf

}


function VariantFiltration2 ()
{
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T VariantFiltration -R $ref -V raw_variants_recal.vcf --filterExpression 'QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0 || SOR > 10.0' --filterName "basic_filter" -o filtered_final.vcf
	java -jar /home/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R $ref -V  filtered_final.vcf -ef  -o ${base}_variants.vcf
	mv ${base}_variants.vcf ../../variant_files/
	rm -rf /home/vdp5/projects/vivax_cambodia/data/nyu_pipeline_results/$base
}





zeta=$(basename $1)
IFS='_' read -ra ADDR <<< $zeta
base=${ADDR[0]}

touch /home/vdp5/projects/vivax_cambodia/logs/nyu_run.log_${base}
logfle=/home/vdp5/projects/vivax_cambodia/logs/nyu_run.log_${base}
cd /home/vdp5/projects/vivax_cambodia/data/nyu_pipeline_results
mkdir $base
cd $base
CollectInsertSizeMetrics $1
echo "CollectInsertSizeMetrics" >> $logfle
AddOrReplaceReadGroups $1 $base
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
VariantFiltration2
echo "VariantFiltration2" >> $logfle

