# editign the config names in the vcf file generated so that snpEff can
# match the scaffold names to genbank annotations.

import os
import sys
import csv
import fileinput

parse_data = list(
    csv.reader(open('../data/other/raw_contigs_ef_file'), delimiter='\t'))

filedata = None
with open('../data/merged_vcf_snp/ef_pass_merge_sorted.vcf', 'r') as file:
    filedata = file.read()

replacerdict = {}

for line in parse_data:
    if 'ID=LT' in line[0]:
        continue
    else:
        datumold = line[0].split(',')[0].split('=')[-1]
        datumnew = datumold.split('.')[0]
        replacerdict[datumold] = datumnew

for alpha in replacerdict:
    filedata = filedata.replace(alpha, replacerdict[alpha])

with open('../data/merged_vcf_snp/ef_pass_merge_sorted.vcf', 'w') as file:
    file.write(filedata)
