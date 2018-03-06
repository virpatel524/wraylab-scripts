# obtains coordinates for vir genes for use in GATK filter programs


newset = []


import csv
from Bio import SeqIO
for seq_record in SeqIO.parse("/newhome/vdp5/data/reference_genomes/PVP01.gbk", "genbank"):
	chrom =  seq_record.name
	for seq_feature in seq_record.features:
		if seq_feature.type == 'CDS':
			if 'product' in seq_feature.qualifiers:
				if 'PIR' in seq_feature.qualifiers['product'][0] or 'VIR' in seq_feature.qualifiers['product'][0]:
					if float(list(seq_feature.location)[0]) <  float(list(seq_feature.location)[-1]):
						print '{}:{}-{}'.format(chrom, list(seq_feature.location)[0], list(seq_feature.location)[-1])
					else:
						newset.append('{}:{}-{}'.format(chrom, list(seq_feature.location)[-1], list(seq_feature.location)[0]))
					

newfle = open('../../data/low_comp/vir_gene_coord.list', 'w')

for zeta in newset:
	newfle.write(zeta + '\n')

newfle.close()