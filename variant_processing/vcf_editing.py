#!/bin/env python2.7

import vcf
import argparse
import sys 
import os


sys.path.append(os.getcwd()) 

parser = argparse.ArgumentParser()
parser.add_argument('--vcf_file', help="VCF file for use")
parser.add_argument('--name', help='name for file')

args = parser.parse_args()


vcf_reader = vcf.Reader(open(args.vcf_file, 'r'))
vcf_writer = vcf.Writer(open('{}'.format(args.name), 'w'), vcf_reader)




counter_low = 0
counter_total = 0


#1percent filtering

total_good = 0
total_all = 0



remaining_good = []

for record in vcf_reader:
	total_number_of_reads = {}
	homalt = record.get_hom_alts()
	hets = record.get_hets()
	homref = record.get_hom_refs()

	for alpha in homref:
		tmp = alpha.data[0].split('/')
		allele = []

		for beta in tmp:
			allele.append(int(beta))

		for beta in allele:
			if beta not in total_number_of_reads:
				total_number_of_reads[beta] = 0

		for i in range(len(allele)):
			total_number_of_reads[allele[i]] += alpha.data[1][i]

	for alpha in hets:
		tmp = alpha.data[0].split('/')
		allele = []

		for beta in tmp:
			allele.append(int(beta))

		for beta in allele:
			if beta not in total_number_of_reads:
				total_number_of_reads[beta] = 0

		for i in range(len(allele)):
			total_number_of_reads[allele[i]] += alpha.data[1][i]


	for alpha in homref:
		tmp = alpha.data[0].split('/')
		allele = []

		for beta in tmp:
			allele.append(int(beta))

		for beta in allele:
			if beta not in total_number_of_reads:
				total_number_of_reads[beta] = 0

		for i in range(len(allele)):
			total_number_of_reads[allele[i]] += alpha.data[1][i]

	tot = 0

	for alpha in total_number_of_reads:
		tot += total_number_of_reads[alpha] 

	for alpha in total_number_of_reads:
		if alpha == 0:
			continue
		if tot == 0:
			continue
		zeta = (float(total_number_of_reads[alpha]) / float(tot)) * 100
		if zeta > 1:
			vcf_writer.write_record(record)
			total_good += 1
			remaining_good.append(record)
		elif total_number_of_reads[alpha] > 10:
			vcf_writer.write_record(record)
			total_good += 1
			remaining_good.append(record)
		total_all += 1
		



tmp =  float(total_good) / float(total_all)


gt_matrix = {}


for record in remaining_good:
	entry_name = '{}:{}-{}'.format(record.CHROM, record.start, record.end - 1)
	adder_entry = []
	for sample in record.samples:
		tmp =  sample.data[2]
		if tmp == None:
			adder_entry.append('0')
			continue
		if sample.gt_type != None:
			adder_entry.append('1')
		else:
			adder_entry.append('0')
	gt_matrix[entry_name] = adder_entry





vcf_writer.close()