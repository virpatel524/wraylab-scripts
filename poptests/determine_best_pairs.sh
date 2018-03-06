bcftools query -l $1 > /tmp/samples.txt
source ~/.bash_profile

while read p; do
	java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R $PVP01REF -V ${1} -o /home/vdp5/tmp/${p}.tmp.vcf -sn ${p}
	
	data="""
import vcf
vcf_reader = vcf.Reader(open('/home/vdp5/tmp/${p}.tmp.vcf', 'r'))
vcf_writer = vcf.Writer(open('/home/vdp5/tmp/${p}.fin.vcf', 'w'), vcf_reader)



for record in vcf_reader:
	if record.genotype('${p}')['GT'] == './.':
		continue
	else:
		vcf_writer.write_record(record)


vcf_writer.close()
"""

	echo "${data}" > /tmp/prepscript_${p}.py
	python2.7 /tmp/prepscript_${p}.py
	rm -rf /home/vdp5/tmp/${p}.tmp.vcf
	rm -rf /tmp/prepscript_${p}.sh


	vcfintersect -i /home/vdp5/tmp/${p}.fin.vcf ${1} -r $PVP01REF > /home/vdp5/tmp/collective.${p}.vcf
	rtg vcfstats /home/vdp5/tmp/collective.${p}.vcf > /home/vdp5/tmp/collective.${p}.stats
	rm -rf /home/vdp5/tmp/${p}.fin.vcf

data="""
import csv
import argparse
import numpy as np
import os


datafile = list(csv.reader(open('/home/vdp5/tmp/collective.${p}.stats'),delimiter='\t'))

sampname_missing = {}


samplst = []

for alpha in datafile:
	if len(alpha) == 0: continue
	if 'Sample Name' in alpha[0]:
		sampname = alpha[0].split(' ')[-1]
		samplst.append(sampname)
	if 'Missing Genotype' in alpha[0]:
		sampname_missing[sampname] = int(alpha[0].split(' ')[-1])

sample_cats = list(csv.reader(open('${2}'),delimiter='\t'))

whoami = ''


for i in range(len(sample_cats)):
	if samplst[i] == '${p}':
		whoami = sample_cats[i][0]


eligible_samps = []

for i in range(len(sample_cats)):
	if samplst[i] == '${p}': continue
	if sample_cats[i][0] == whoami:
		eligible_samps.append(samplst[i])

lowest = eligible_samps[:4]

lowest.sort(cmp=lambda x,y: cmp(sampname_missing[y], sampname_missing[x]))

for alpha in eligible_samps:
	if sampname_missing[alpha] <= sampname_missing[lowest[0]]:
		lowest[0] = alpha
		lowest.sort(cmp=lambda x,y: cmp(sampname_missing[y], sampname_missing[x]))

print 'java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -R ${PVP01REF} -V /home/vdp5/tmp/collective.${p}.vcf -o /home/vdp5/tmp/collective.${p}.final4.vcf -sn ${p} -sn {} -sn {} -sn {} -sn {}'.format(lowest[0], lowest[1], lowest[2], lowest[3])
	""" 

	echo "${data}" > /tmp/prepscript_${p}.py
	output=$(python2.7 /tmp/prepscript_${p}.py)
	eval $output
	rm -rf /home/vdp5/tmp/collective.${p}.vcf

done < /tmp/samples.txt 