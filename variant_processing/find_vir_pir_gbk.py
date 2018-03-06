#finds VIR and PIR genes in PVP01 GBK files

# 01/08/18 | 4:44 PM
from Bio import SeqIO
import argparse
import os
import sys
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for use")
parser.add_argument('--output', help='output file for use')
args = parser.parse_args()



listbadders = []

newdata = open('/home/vdp5/projects/vivax_cambodia/data/txt_files/extradata/pir_virgenes.txt','w')

for gb_record in SeqIO.parse(open('/newhome/vdp5/data/reference_genomes/PVP01.gbk',"r"), "genbank"):
	for alpha in gb_record.features:
		if alpha.type == 'CDS':
			try:
				if 'PIR' in alpha.qualifiers['note'][0] or 'VIR' in alpha.qualifiers['note'][0]:
					# print alpha.qualifiers
					listbadders.append(alpha.qualifiers['locus_tag'][0])
			except:
				x = 5
			try: 
				if 'PIR' in alpha.qualifiers['product'][0] or 'VIR' in alpha.qualifiers['product'][0]:
					# print alpha.qualifiers
					listbadders.append(alpha.qualifiers['locus_tag'][0])
			except: 
				x = 5

listbadders = list(set(listbadders))
for alpha in listbadders:
        newdata.write(alpha + '\n')

newdata.close()

setoutput = []

for alpha in listbadders:
        setoutput.append('(ANN[*].GENE = \'{}\')'.format(alpha))

newstr = 'java -jar /newhome/vdp5/source_code/snpEff/SnpSift.jar filter "{}" {} > {}'.format(' || '.join(setoutput), args.vcffile, args.output)

new = open('/home/vdp5/projects/vivax_cambodia/scripts/variant_processing/really_do_pirvir_processing.sh', 'w')

new.write(newstr + '\n')

new.close()



                                
